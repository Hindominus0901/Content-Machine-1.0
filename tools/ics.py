#!/usr/bin/env python3
"""Weekly calendar reminders as an RFC 5545 .ics file.

    python3 tools/ics.py --edition vn [--talk-day Mon] [--talk-time 09:00]
                         [--friday-time 16:00] [--start 2026-10-05] [--out reminders.ics]

Two weekly events by default: the talk day and the Friday numbers reminder.
Times are floating local times (no TZID), so a reminder set for 09:00 rings at
09:00 wherever the coach's phone is. Text comes from the edition's strings
(ics.talk.summary, ics.talk.description, ics.friday.summary,
ics.friday.description) when present. Output uses CRLF line endings, folds
lines at 75 octets, and derives each UID from the event's content, so the same
input always gives the same file.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cmlib  # noqa: E402
from cmlib import CMError  # noqa: E402

PRODID = "-//Content Machine//Reminders//EN"
DAYS = ("MO", "TU", "WE", "TH", "FR", "SA", "SU")
DAY_ALIASES = {name: i for i, name in enumerate(DAYS)}
DAY_ALIASES.update({n: i for i, n in enumerate(("mon", "tue", "wed", "thu", "fri", "sat", "sun"))})
DAY_ALIASES.update({n: i for i, n in enumerate(
    ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"))})
MAX_OCTETS = 75

# Fallback text when an edition has no ics.* strings yet.
DEFAULT_TEXT = {
    "ics.talk.summary": "Weekly Talk",
    "ics.talk.description": 'Open Content Machine, newest chat, and say "next".',
    "ics.friday.summary": "Friday numbers",
    "ics.friday.description": 'Open Content Machine, newest chat, and say "my numbers".',
}


def weekday_index(day) -> int:
    if isinstance(day, int) and 0 <= day <= 6:
        return day
    key = str(day).strip()
    idx = DAY_ALIASES.get(key.upper(), DAY_ALIASES.get(key.lower()))
    if idx is None:
        raise ValueError(f"unknown weekday '{day}'")
    return idx


def escape_text(value: str) -> str:
    """TEXT value escaping (RFC 5545 §3.3.11)."""
    return (value.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,")
            .replace("\r\n", "\\n").replace("\n", "\\n"))


def fold(line: str) -> list[str]:
    """Split one content line into chunks of at most 75 octets, never inside a UTF-8 character."""
    out: list[str] = []
    current, size, limit = "", 0, MAX_OCTETS
    for ch in line:
        n = len(ch.encode("utf-8"))
        if size + n > limit:
            out.append(current)
            current, size, limit = "", 0, MAX_OCTETS - 1   # continuation lines start with a space
        current += ch
        size += n
    out.append(current)
    return [out[0]] + [" " + part for part in out[1:]]


def unfold(text: str) -> list[str]:
    """Content lines of an .ics text with folding undone (for checks and tests)."""
    lines: list[str] = []
    for raw in text.split("\r\n"):
        if raw.startswith((" ", "\t")) and lines:
            lines[-1] += raw[1:]
        elif raw:
            lines.append(raw)
    return lines


def _first_on_or_after(start: dt.date, weekday: int) -> dt.date:
    return start + dt.timedelta(days=(weekday - start.weekday()) % 7)


def _parse_time(value) -> dt.time:
    if isinstance(value, dt.time):
        return value
    hh, _, mm = str(value).partition(":")
    return dt.time(int(hh), int(mm or 0))


def _parse_date(value) -> dt.date:
    if value is None:
        return dt.date.today()
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


def _fixed_offset(tz: str, around: dt.date) -> str:
    """'+0700' for a zone without daylight saving; ValueError otherwise."""
    from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
    try:
        zone = ZoneInfo(tz)
    except (ZoneInfoNotFoundError, ValueError):
        raise ValueError(f"unknown time zone '{tz}'")
    probes = [dt.datetime.combine(around + dt.timedelta(days=d), dt.time(12), zone) for d in range(0, 366, 30)]
    offsets = {p.utcoffset() for p in probes}
    if len(offsets) != 1:
        raise ValueError(f"time zone '{tz}' has daylight saving; use floating times")
    minutes = int(offsets.pop().total_seconds() // 60)
    sign = "+" if minutes >= 0 else "-"
    return f"{sign}{abs(minutes) // 60:02d}{abs(minutes) % 60:02d}"


def make_ics(events: list[dict], tz_floating: bool = True, tz: str | None = None) -> str:
    """Build a VCALENDAR with one weekly VEVENT per event.

    Each event: summary (required), description, weekday ("Mon", "MO", 0-6),
    time ("HH:MM"), duration_minutes (default 15), start (date or ISO string;
    the first occurrence is the first matching weekday on or after it; default
    today) and alarm_minutes (minutes before; default 0; None for no alarm).
    With tz_floating=False, `tz` names a fixed-offset zone (e.g.
    Asia/Ho_Chi_Minh) and times carry its TZID plus a VTIMEZONE.
    """
    if not tz_floating and not tz:
        raise ValueError("tz is required when tz_floating is False")
    body: list[str] = []
    first_dates: list[dt.date] = []
    for ev in events:
        summary = cmlib.nfc(str(ev["summary"])).strip()
        if not summary:
            raise ValueError("event summary is empty")
        description = cmlib.nfc(str(ev.get("description") or "")).strip()
        day = weekday_index(ev.get("weekday", "MO"))
        at = _parse_time(ev.get("time", "09:00"))
        first = _first_on_or_after(_parse_date(ev.get("start")), day)
        first_dates.append(first)
        start = dt.datetime.combine(first, at).strftime("%Y%m%dT%H%M%S")
        duration = int(ev.get("duration_minutes", 15))
        rrule = f"FREQ=WEEKLY;BYDAY={DAYS[day]}"
        dtstart = f"DTSTART:{start}" if tz_floating else f"DTSTART;TZID={tz}:{start}"
        uid_src = "\x1f".join([summary, description, start, rrule, str(duration), "" if tz_floating else tz])
        uid = hashlib.sha256(uid_src.encode("utf-8")).hexdigest()[:24] + "@content-machine"
        body += [
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTAMP:{first.strftime('%Y%m%d')}T000000Z",
            dtstart,
            f"DURATION:PT{duration}M",
            f"RRULE:{rrule}",
            f"SUMMARY:{escape_text(summary)}",
        ]
        if description:
            body.append(f"DESCRIPTION:{escape_text(description)}")
        alarm = ev.get("alarm_minutes", 0)
        if alarm is not None:
            body += [
                "BEGIN:VALARM",
                "ACTION:DISPLAY",
                f"DESCRIPTION:{escape_text(summary)}",
                f"TRIGGER:-PT{int(alarm)}M" if int(alarm) else "TRIGGER:PT0S",
                "END:VALARM",
            ]
        body.append("END:VEVENT")

    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", f"PRODID:{PRODID}", "CALSCALE:GREGORIAN", "METHOD:PUBLISH"]
    if not tz_floating:
        offset = _fixed_offset(tz, min(first_dates) if first_dates else dt.date.today())
        lines += ["BEGIN:VTIMEZONE", f"TZID:{tz}", "BEGIN:STANDARD", "DTSTART:19700101T000000",
                  f"TZOFFSETFROM:{offset}", f"TZOFFSETTO:{offset}", "END:STANDARD", "END:VTIMEZONE"]
    lines += body + ["END:VCALENDAR"]
    folded = [part for line in lines for part in fold(line)]
    return "\r\n".join(folded) + "\r\n"


def edition_text(edition, key: str) -> str:
    """A strings key rendered for the help target, or the English fallback."""
    if edition is not None and key in edition.strings:
        ctx = cmlib.make_ctx(edition, "help", path=f"strings/{edition.id}.toml")
        return cmlib.nfc(cmlib.render_text(edition.strings[key], ctx)).strip()
    return DEFAULT_TEXT[key]


def default_events(edition=None, talk_day="Mon", talk_time="09:00", friday_time="16:00", start=None) -> list[dict]:
    """The two Day-0 reminders: the weekly talk and the Friday numbers."""
    return [
        {"summary": edition_text(edition, "ics.talk.summary"),
         "description": edition_text(edition, "ics.talk.description"),
         "weekday": talk_day, "time": talk_time, "duration_minutes": 15, "start": start},
        {"summary": edition_text(edition, "ics.friday.summary"),
         "description": edition_text(edition, "ics.friday.description"),
         "weekday": "FR", "time": friday_time, "duration_minutes": 5, "start": start},
    ]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Write weekly talk-day and Friday reminders as .ics.")
    ap.add_argument("--edition", choices=list(cmlib.EDITIONS), default="en")
    ap.add_argument("--talk-day", default="Mon")
    ap.add_argument("--talk-time", default="09:00")
    ap.add_argument("--friday-time", default="16:00")
    ap.add_argument("--start", help="first week on or after this date (YYYY-MM-DD; default today)")
    ap.add_argument("--tz", help="fixed-offset IANA zone instead of floating time (e.g. Asia/Ho_Chi_Minh)")
    ap.add_argument("--out", type=Path, help="output file (default: stdout)")
    ap.add_argument("--root", type=Path, default=None, help="repo root (default: CM_ROOT or this repo)")
    args = ap.parse_args(argv)
    root = (args.root or cmlib.ROOT).resolve()
    try:
        edition = cmlib.load_edition(args.edition, root)
        events = default_events(edition, args.talk_day, args.talk_time, args.friday_time, args.start)
        text = make_ics(events, tz_floating=not args.tz, tz=args.tz)
    except CMError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    data = text.encode("utf-8")
    if args.out:
        args.out.write_bytes(data)
    else:
        sys.stdout.buffer.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
