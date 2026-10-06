"""Shared runtime-check core (docs/BUILD.md §8; QA spec §2.1-§2.4, §5.2).

Pure functions, standard library only, and no imports from the repo:
tools/build.py inlines this file into the skill's single-file
scripts/ship_lint.py, and evals/graders.py imports it, so the runtime lint and
the transcript graders count the same way.

Languages are "en" and "vn". Every function NFC-normalises its input. Counts:
EN words and VN tiếng are both whitespace tokens that hold a letter or digit.

Keep names here distinct from tools/shiplint.py's own (main, lint_*, load_*,
format_line, PayloadError, PIECE_FIELDS, _sl_*): after inlining they share one
namespace. The copy-run helpers (wf13-inspiration-spec §4 DISTANCE) use the
copy_* / *_copy_note / point_order_mirror / stock_phrase_list names.
"""
from __future__ import annotations

import re
import unicodedata
from typing import NamedTuple

LANGS = ("en", "vn")

# Per-edition numbers (editions/<id>.toml [params]; QA spec §0).
WORD_RATE = {"en": 2.5, "vn": 3.5}          # spoken words (tiếng) per second
MICRO_THRESHOLD = {"en": 40, "vn": 60}      # under this many words: the Micro check
QUOTE_CAP = {"en": 15, "vn": 25}            # longest public quote
HOOK_MAX = {"en": 12, "vn": 18}             # verbal hook length
VERDICT_MAX_WORDS = 20
DROP_MAX_WORDS = 120
BG_POST_MAX_CHARS = 130
ON_SCREEN_MAX_WORDS = 6
WORD_RATE_TOLERANCE = 0.15
SHORT_DEFAULT_MAX_SECONDS = 60
# Copy runs against someone else's post (evals/acceptance.toml [copy] en_words / vn_tieng;
# wf13-inspiration-spec §4 DISTANCE, §6): a shared run this long is a copy.
COPY_RUN_MIN = {"en": 6, "vn": 8}

_ALNUM = re.compile(r"[^\W_]")
UPPER = "A-ZĐÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ"
_QUOTE_MAP = str.maketrans({"“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
                            "‘": "'", "’": "'", "‛": "'"})


# ---------------------------------------------------------------- text basics

def nfc(text: str | None) -> str:
    return unicodedata.normalize("NFC", text or "")


def straight_quotes(text: str) -> str:
    """Curly quotes and guillemets to ASCII quotes (length-preserving)."""
    return text.translate(_QUOTE_MAP)


def strip_diacritics(text: str) -> str:
    """Vietnamese spelling without diacritics, one character per character (đ → d)."""
    out = []
    for ch in nfc(text):
        if ch == "đ":
            out.append("d")
        elif ch == "Đ":
            out.append("D")
        else:
            out.append(unicodedata.normalize("NFD", ch)[0])
    return "".join(out)


def fold(text: str) -> str:
    """Lowercase without diacritics, one character per character (positions line up with `text`)."""
    return "".join(c if len(c.lower()) != 1 else c.lower() for c in strip_diacritics(text))


def count_words(text: str, lang: str = "en") -> int:
    """EN words or VN tiếng: whitespace tokens holding at least one letter or digit."""
    return sum(1 for tok in nfc(text).split() if _ALNUM.search(tok))


def count_tieng(text: str) -> int:
    """VN syllables (tiếng). Vietnamese writes one syllable per whitespace token."""
    return count_words(text, "vn")


def phrase_re(phrase: str, flags: int = re.I) -> re.Pattern:
    """A whole-word, whitespace-tolerant pattern for a literal phrase."""
    body = r"\s+".join(re.escape(part) for part in nfc(phrase).split())
    return re.compile(r"(?<!\w)" + body + r"(?!\w)", flags)


def _phrase_hits(text: str, phrases) -> list[str]:
    text = nfc(text)
    found = []
    for phrase in phrases:
        if phrase not in found and phrase_re(phrase).search(text):
            found.append(phrase)
    return found


def sentences(text: str) -> list[str]:
    """Lines split further at sentence ends (. ! ? … followed by a space)."""
    out = []
    for line in nfc(text).splitlines():
        out.extend(part.strip() for part in re.split(r"(?<=[.!?…])\s+", line) if part.strip())
    return out


def plain_line(line: str) -> str:
    """A line without markdown decoration (quote marks, bullets, emphasis), quotes straightened."""
    s = straight_quotes(nfc(line)).strip()
    s = re.sub(r"^(?:>\s*)+", "", s)
    s = re.sub(r"^(?:[-*+•]\s+)", "", s)
    for _ in range(3):
        stripped = re.sub(r"^(\*\*|__|\*|_)(.*)\1$", r"\2", s).strip()
        stripped = re.sub(r"^(\*\*|__)(.*?)\1", r"\2", stripped).strip()
        if stripped == s:
            break
        s = stripped
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- numbers

class Number(NamedTuple):
    raw: str              # the token as written, prefix and suffix included
    value: float | None   # numeric value with k / tr / triệu / tỷ applied; None for times and dates
    kind: str             # number | money | time | date | id
    percent: bool
    start: int
    end: int
    structural: bool      # a label or list marker (Beat 2, N2, "1)", ≤12), not a claim
    tagged: bool          # inside [NEEDS: …] / [CẦN …] / [guess], or marked "(my guess)"


_DIGITS = re.compile(r"\d+(?:[.,]\d+)*")
_MULT_AFTER = [
    (re.compile(r"\s?(?:triệu|trieu)(?!\w)", re.I), 1e6),
    (re.compile(r"\s?(?:tỷ|tỉ|ty)(?!\w)", re.I), 1e9),
    (re.compile(r"\s?(?:nghìn|ngàn)(?!\w)", re.I), 1e3),
    (re.compile(r"\s?(?:million|mil)(?!\w)", re.I), 1e6),
    (re.compile(r"\s?(?:billion|bn)(?!\w)", re.I), 1e9),
    (re.compile(r"(?:tr|Tr|TR)(?![^\W\d_])"), 1e6),
    (re.compile(r"[kK](?![^\W\d_])"), 1e3),
    # counts as apps print them: "2.1M views", "52,7 N lượt xem" (nghìn), "1,2 Tr" (triệu)
    (re.compile(r"\s?M(?![^\W\d_])"), 1e6),
    (re.compile(r"\s?N(?![^\W\d_])"), 1e3),
    (re.compile(r"\s(?:Tr|TR)(?![^\W\d_])"), 1e6),
]
_MONEY_AFTER = re.compile(r"\s?(?:đồng|dong|vnđ|vnd|usd|dollars?|bucks|đ|₫)(?![^\W\d_])", re.I)
_PERCENT_AFTER = re.compile(r"\s?(?:%|percent(?!\w)|per cent(?!\w)|phần trăm(?!\w))", re.I)
_TAG_SPAN = re.compile(r"\[\s*(?:NEEDS|CẦN|guess|GAP|đoán|ước tính)\b[^\]\n]*(?:\]|$)", re.I | re.M)
_GUESS_AFTER = re.compile(r"\s*(?:\[\s*(?:guess|đoán)\s*\]|\((?:my |mình |em |anh |chị )?(?:guess|đoán)\))", re.I)
STRUCTURE_WORDS = {
    "beat", "beats", "slide", "slides", "line", "step", "part", "take", "hook", "option", "week", "day",
    "chunk", "round", "version", "question", "no", "n", "q", "tip", "point", "idea", "piece", "rung",
    "tuần", "ngày", "bước", "câu", "dòng", "phần", "ý", "cảnh", "lần", "lượt", "tháng", "khóa", "khoá",
    "bài", "tập", "slide", "số",
}


def _num_value(digits: str) -> float:
    """1.990.000 / 1,150 → thousands; 4,99 / 1.5 → decimal (a separator before exactly 3 digits groups)."""
    parts = re.split(r"[.,]", digits)
    whole, frac = parts[0], ""
    for grp in parts[1:]:
        if len(grp) == 3 and not frac:
            whole += grp
        else:
            frac = grp
            break
    return float(whole + ("." + frac if frac else ""))


def _prev_word(text: str, pos: int) -> str:
    m = re.search(r"([^\W\d_]+)\s*[#.:]?\s*$", text[max(0, pos - 24):pos])
    return m.group(1).casefold() if m else ""


# Month-name dates ("Oct 8", "TUE, OCT 13", "Monday, Oct 19", "Oct 6, 2026", "6 Oct 2026", "Oct 12–18") are
# dates, never claims; a lowercase "may" / "march" is a verb ("you may 2x it"), not a month.
_MONTH = (r"(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sep(?:t(?:ember)?)?|"
          r"oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)")
_MONTH_BEFORE = re.compile(r"(?<![^\W\d_])(" + _MONTH + r")\.?\s+$", re.I)
_MONTH_AFTER = re.compile(r"(?:st|nd|rd|th)?\s+(" + _MONTH + r")\.?(?![^\W\d_])", re.I)
# "Oct 13: …" yes; "Oct 8:30", "Oct 25%", "Oct 20k", "Oct 20+" no (a time, a percent, a count)
_DAY_SUFFIX = re.compile(r"(?:st|nd|rd|th)(?![^\W\d_])|(?![\d/%+]|:\d|[^\W\d_])")
_YEAR_AFTER = re.compile(r",?\s+(?:19|20)\d{2}(?!\d)")
_DATE_RANGE_GAP = re.compile(r"\s*[–—-]\s*$")
# A day number that counts something is a claim, not a date: "In October 20 clients joined", "By June 30 women had
# an offer", "May 3 clients said yes", "Oct 8 – 25 women booked".
_COUNT_AFTER = re.compile(
    r"\s+(?:(?:more|new|other|past|paying|happy|real|local|young|older|single|working|busy|former|current|"
    r"extra|total)\s+)?(?:people|persons?|women|men|children|kids|guys|girls|ladies|folks|staff|clients|customers|"
    r"students|members|dads|moms|mums|parents|families|couples|coaches|users|subscribers|followers|readers|viewers|"
    r"leads|calls|sales|sign-?ups|buyers|patients|homeowners|homes|houses|rooms|jobs|offers|interviews|applications|"
    r"hires|deals|projects|orders|bookings|views|likes|comments|shares|reviews|testimonials|lbs|pounds|kilos|kgs?|"
    r"percent|times|teams|companies|businesses|agencies|owners|founders|leaders|managers|employees|workers|"
    r"học viên|khách(?: hàng)?|người)(?![^\W\d_])", re.I)
# "9/10 clients", "3/4 of my clients", "4/5 stars": a ratio, never a day/month date.
_RATIO_AFTER = re.compile(r"\s+of\s+(?:my|our|the|your|their|them|those|these|all|every)(?![^\W\d_])|"
                          r"\s+(?:stars?|ratings?)(?![^\W\d_])|" + _COUNT_AFTER.pattern, re.I)
# US retirement accounts are names, not amounts: 401(k), 401k, 403(b), 457(b). A bare "401k" in a money context
# ("we did 401k in revenue", "made 457k last year") is an amount.
_RETIREMENT = re.compile(r"(?:401|403|457)\s?(?:(\([kKbB]\))|[kKbB](?![^\W\d_]))")
_ACCOUNT_MONEY_BEFORE = re.compile(
    r"(?<![^\W\d_])(?:made|make|makes|making|earned|earn|earns|earning|grossed|cleared|raised|billed|netted|"
    r"brought in|bring in|generated|revenue of|income of|sales of|profit of)\s+$", re.I)
_ACCOUNT_MONEY_AFTER = re.compile(
    r"\s*(?:(?:in|of)\s+)?(?:revenue|sales|income|profit|billings?|bookings|fees|salary|arr|mrr|a\s+(?:year|month)|"
    r"per\s+(?:year|month|yr|mo)|/\s?(?:yr|year|mo|month)|last\s+year|this\s+year)(?![^\W\d_])", re.I)


def _retirement_account(text: str, start: int) -> re.Match | None:
    """401(k), 401k, 403(b), 457(b) at `start`: an account name, unless a bare form reads as money."""
    m = _RETIREMENT.match(text, start)
    if m and not m.group(1) and (_ACCOUNT_MONEY_BEFORE.search(text[max(0, start - 24):start])
                                 or _ACCOUNT_MONEY_AFTER.match(text, m.end())):
        return None
    return m


def _month_word(word: str) -> bool:
    """A month name as written: any case, except a lowercase "may" / "march", which are verbs."""
    return not (word in ("may", "march", "mar"))


_SECONDS_AFTER = re.compile(r"(?:\s*[–—-]\s*\d+(?:[.,]\d+)?)?\s*(?:giây|secs?|seconds?|s)(?![^\W\d_])", re.I)
_SECONDS_BEFORE = re.compile(r"(?<![^\W\d_])(?:giây|seconds?|secs?)\s*(?:thứ\s*)?[#:]?\s*$", re.I)


def _is_timing(text: str, start: int, end: int, kind: str, percent: bool) -> bool:
    """A video timestamp or a seconds mark in a script ("0:15", "3–15 giây", "15–35 s", "giây 35"):
    a beat label, not a claim."""
    raw = text[start:end]
    line_before = text[text.rfind("\n", 0, start) + 1:start]
    if kind == "time":
        return bool(re.fullmatch(r"0{1,2}:\d{2}", raw) or re.search(r"(?<!\d)0{1,2}:\d{2}\s*[–—-]\s*$", line_before))
    if kind != "number" or percent:
        return False
    if _SECONDS_AFTER.match(text, end) or _SECONDS_BEFORE.search(line_before):
        return True
    return raw.endswith("s") and bool(re.search(r"\d\s*[–—-]\s*$", line_before))   # "0–3s"


def _month_date(text: str, start: int, end: int, digits: str, last_date_end: int) -> tuple[int, int] | None:
    """(raw start, end) when the digits are part of a month-name date ("Oct 8", "Oct 6, 2026", "6 Oct 2026",
    "Oct 2026"), or the second day of a range after one ("Oct 12–18"); else None. A day number followed by what it
    counts ("In October 20 clients joined", "Oct 8 – 25 women") is a number, not a date."""
    day = re.fullmatch(r"\d{1,2}", digits) is not None and 1 <= int(digits) <= 31
    year = re.fullmatch(r"(?:19|20)\d{2}", digits) is not None
    if not (day or year):
        return None
    mb = _MONTH_BEFORE.search(text[max(0, start - 12):start])
    if mb and _month_word(mb.group(1)):
        raw_start = start - (len(mb.group(0)))
        if year:
            return raw_start, end
        suffix = _DAY_SUFFIX.match(text, end)
        if suffix is None or (suffix.end() == end and _COUNT_AFTER.match(text, end)):
            return None
        end = suffix.end()
        yr = _YEAR_AFTER.match(text, end)
        return raw_start, yr.end() if yr else end
    if day:
        ma = _MONTH_AFTER.match(text, end)
        if ma and _month_word(ma.group(1)):
            yr = _YEAR_AFTER.match(text, ma.end())
            return start, yr.end() if yr else ma.end()
        if last_date_end >= 0 and _DATE_RANGE_GAP.fullmatch(text[last_date_end:start]):
            suffix = _DAY_SUFFIX.match(text, end)                # "Oct 12–18", "Oct 12th–18th"
            if suffix is not None and not (suffix.end() == end and _COUNT_AFTER.match(text, end)):
                return start, suffix.end()     # the range's second day
    return None


def numbers_in(text: str) -> list[Number]:
    """Every number token: 1.990.000đ, 1,99tr, 99k, $2,400, 30%, 45+, 11:59, 23h59, 13/10, 2026-10-05,
    Oct 8, 6 Oct 2026.

    Ranges ("2–3") give two numbers. Digits glued to letters (N2, B2B, P-3) are ids; so are 401(k), 401k, 403(b).
    """
    text = nfc(text)
    tagged_spans = [(m.start(), m.end()) for m in _TAG_SPAN.finditer(text)]
    out: list[Number] = []
    pos = 0
    last_date_end = -1
    while True:
        m = _DIGITS.search(text, pos)
        if not m:
            break
        start, end = m.start(), m.end()
        pos = end
        digits = m.group(0)
        prev = text[start - 1] if start else ""
        prev2 = text[start - 2] if start > 1 else ""
        kind, value, percent, structural = "number", None, False, False
        retirement = _retirement_account(text, start) if prev != "$" and not (prev and prev.isalnum()) else None
        if retirement:
            raw = text[start:retirement.end()]
            tagged = any(a <= start < b for a, b in tagged_spans)
            out.append(Number(raw, None, "id", False, start, retirement.end(), True, tagged))
            pos = retirement.end()
            continue
        month = _month_date(text, start, end, digits, last_date_end) if not (prev and prev.isalnum()) else None
        if month:
            raw_start, end = month
            tagged = any(a <= raw_start < b for a, b in tagged_spans) or bool(_GUESS_AFTER.match(text[end:]))
            out.append(Number(text[raw_start:end], None, "date", False, raw_start, end, False, tagged))
            pos = last_date_end = end
            continue
        # dates and times first: they swallow their separators
        iso = re.match(r"-\d{1,2}-\d{1,2}(?!\d)", text[end:]) if len(digits) == 4 else None
        dm = re.match(r"(?:/\d{1,4}){1,2}(?![\d/])", text[end:]) if re.fullmatch(r"\d{1,2}", digits) else None
        tm = re.match(r"(?::\d{2}|h\d{2}(?!\d)|h(?![^\W\d_]))", text[end:]) if re.fullmatch(r"\d{1,2}", digits) else None
        if iso:
            kind, end = "date", end + iso.end()
        elif dm and prev != "/" and not _RATIO_AFTER.match(text, end + dm.end()):
            kind, end = "date", end + dm.end()
        elif tm and prev != ":":
            kind, end = "time", end + tm.end()
        else:
            value = _num_value(digits)
        raw_start = start
        if prev and (prev.isalpha() or prev == "_"):
            if prev in "xX×" and not (prev2 and prev2.isalnum()):
                raw_start = start - 1                     # x3, ×2
            else:
                kind, structural = "id", True             # N2, B2B, mp4
        elif prev and prev in "-–" and prev2 and prev2.isupper():
            kind, structural = "id", True                 # P-3, V-12
        elif prev and prev in "$€£":
            kind, raw_start = "money", start - 1
        if kind in ("number", "money"):
            rest = text[end:]
            for pattern, mult in _MULT_AFTER:
                mm = pattern.match(rest)
                if mm:
                    value, end, rest = value * mult, end + mm.end(), text[end + mm.end():]
                    break
            mm = _MONEY_AFTER.match(rest)
            if mm:
                kind, end, rest = "money", end + mm.end(), text[end + mm.end():]
            mm = _PERCENT_AFTER.match(rest)
            if mm:
                percent, end = True, end + mm.end()
            else:
                mm = re.match(r"(?:\+|s\b|st\b|nd\b|rd\b|th\b|[x×](?![^\W\d_]))", rest)
                if mm:
                    end += mm.end()
            if kind == "money" and raw_start == start - 1 and re.match(r"[MB](?![^\W\d_])", text[end:]):
                value, end = value * (1e6 if text[end] == "M" else 1e9), end + 1
        line_start = text.rfind("\n", 0, raw_start) + 1
        before = text[line_start:raw_start]
        after = text[end:end + 2]
        if not structural:
            if re.fullmatch(r"\s*(?:[-*+•]\s+)?\(?", before) and re.match(r"[.)]\s", after + " ") \
                    and kind == "number":
                structural = True                         # list markers "1." "2)"
            elif re.match(r"\)", after) and (not before or before[-1].isspace()) and kind == "number":
                structural = True                         # inline "1) … 2) …"
            elif re.search(r"[≤≥<>]\s*$", before) or (kind == "number" and re.search(r"\b(?:under|max|min)\s*$",
                                                                                         before, re.I)):
                structural = True                         # format instructions (≤12 words, under 30 s)
            elif kind == "number" and _prev_word(text, raw_start) in STRUCTURE_WORDS:
                structural = True                         # Beat 2, Week 1, tuần 1
            elif _is_timing(text, raw_start, end, kind, percent):
                structural = True                         # 0:15, 3–15 giây, giây 35 (video timestamps)
        tagged = any(a <= raw_start < b for a, b in tagged_spans) or bool(_GUESS_AFTER.match(text[end:]))
        out.append(Number(text[raw_start:end], value, kind, percent, raw_start, end, structural, tagged))
        pos = end
    return out


def number_keys(n: Number) -> set:
    if n.kind == "date" and re.search(r"[^\W\d_]{3}", n.raw):         # "Oct 8", "6 Oct 2026"
        words = re.findall(r"[^\W\d_]+|\d+", n.raw.casefold())
        return {("date", " ".join(w[:3] if w.isalpha() else str(int(w)) for w in words))}
    if n.kind in ("time", "date"):
        raw = re.sub(r"\s+", "", n.raw).replace("h", ":")
        raw = re.sub(r"(?<!\d)0(\d)", r"\1", raw)
        return {("raw", raw)}
    if n.value is None:
        return set()
    return {("val", round(n.value, 4), n.percent)}


def allowed_number_keys(allowed) -> frozenset:
    """Match keys for every number inside the allowed strings ("6 năm", "$2,400", "8%")."""
    keys: set = set()
    for item in allowed or ():
        for n in numbers_in(str(item)):
            keys |= number_keys(n)
    return frozenset(keys)


def unsupported_numbers(text: str, allowed) -> list[str]:
    """Claim numbers in `text` (not labels, not tagged [NEEDS]/[guess]) whose value is not in `allowed`.

    `allowed` is an iterable of strings (allowed_numbers entries or source rows) or a key set
    from allowed_number_keys(). Units other than k / tr / triệu / tỷ do not matter: "6 năm" allows 6.
    """
    keys = allowed if isinstance(allowed, frozenset) else allowed_number_keys(allowed)
    out: list[str] = []
    for n in numbers_in(text):
        if n.structural or n.tagged:
            continue
        nk = number_keys(n)
        if nk and not (nk & keys) and n.raw not in out:
            out.append(n.raw)
    return out


# ---------------------------------------------------------------- quotes

class Quote(NamedTuple):
    text: str
    start: int
    end: int
    attributed: bool      # someone is said to have said or written it


_QUOTE_SPAN = re.compile(r'"([^"\n]{1,600})"')
_ATTR_BEFORE = {
    "en": re.compile(r"(?i)\b(?:said|says|told (?:me|us|her|him)|wrote|writes|asked|asks|texted|texts|messaged|"
                     r"commented|comments|replied|replies|emailed|posted|put it|called it|calls it|"
                     r"in (?:her|his|their|my) (?:own )?words|DM'?d|DMed)\b[^.!?\"]{0,20}$"),
    # VN: a real subject (kin + name, a client noun, or a name) before the verb; "Hoặc nhắn" and
    # "Bạn gõ" are instructions to the coach, not quotations.
    "vn": re.compile(r"(?:(?<!\w)(?:[Cc]hị|[Aa]nh|[Ee]m|[Bb]ạn|[Cc]ô|[Cc]hú|[Bb]ác|[Bb]é)\s+[" + UPPER + r"][^\W\d_]+|"
                     r"(?<!\w)(?:khách|học viên|người ta|ai đó|họ|một (?:bạn|chị|anh|người|khách|học viên))(?!\w)|"
                     r"(?<!\w)(?!(?:Hoặc|Cứ|Rồi|Thì|Và|Nếu|Khi|Bạn|Chị|Anh|Em|Mình|Hãy|Cô|Chú|Gõ|Nhắn|Bấm|Gửi)(?!\w))"
                     r"[" + UPPER + r"][^\W\d_]+)\s+(?:\w+\s+){0,3}?(?:đã |từng |có )?(?:nói|bảo|nhắn|kể|hỏi|viết|"
                     r"chia sẻ|bình luận|comment|than|tâm sự|gửi)(?!\w)[^.!?\"]{0,20}$"),
}
_ATTR_AFTER = re.compile(r"^[\s,]*(?:[—–-]\s*[" + UPPER + r"]|(?:she|he|they|[A-Z][a-z]+|a client|my client|"
                         r"one client)\s+(?:said|says|wrote|writes|asked|told me|texted|messaged)\b|(?:chị|anh|em|bạn|"
                         r"khách|học viên|[" + UPPER + r"][^\W\d_]+)\s+(?:ấy\s+)?(?:nói|bảo|nhắn|kể|viết|hỏi)\b)")
# A hypothetical speaker is no attribution: a DM label 'someone asks the price, or "can you do my room"', 'if anyone
# says "too expensive"', 'ai đó hỏi "giá sao"' (review G13). Past tense ("someone told me") stays attributed, and so do
# a reported message ('A reader writes: "…"', unless "if / when" makes it a scenario) and an everyone-says claim
# ('ai cũng nói "…"').
_HYPOTHETICAL_BEFORE = re.compile(
    r"(?i)(?:\b(?:someone|somebody|anyone|anybody|they|people"
    r"|(?:if|when|whenever|once)\s+a (?:buyer|lead|prospect|reader|viewer|follower|stranger))"
    r"\s+(?:\w+\s+)?(?:asks?|says?|messages?|comments?|writes?|DMs?|replies|texts?)\b"
    r"|(?<!\w)(?:ai đó|có ai|người nào|ai(?!\s+(?:cũng|mà chẳng|chả)(?!\w)))\s+(?:\S+\s+){0,2}?"
    r"(?:hỏi|nhắn|comment|nói)(?!\w))[^.!?\"]{0,30}$")
# A short quoted term followed by its meaning ('"insight" là điều khách nghĩ', '"CTA" means …') is a gloss.
_GLOSS_AFTER = re.compile(r"^\s*[,:]?\s*(?:là|nghĩa là|có nghĩa là|tức là|means?|meaning|stands for|is short for|"
                          r"=|→|->)(?!\w)", re.I)


def quotes_in(text: str, lang: str = "en") -> list[Quote]:
    """Double-quoted spans (straight or curly), each marked attributed or not.

    A quoted term of up to 3 words followed by its meaning is a gloss, and words given to a hypothetical speaker
    ('someone asks "…"', 'ai đó hỏi "…"') are a scenario: neither is an attributed quote.
    """
    text = straight_quotes(nfc(text))
    out = []
    for m in _QUOTE_SPAN.finditer(text):
        line_start = text.rfind("\n", 0, m.start()) + 1
        before = text[line_start:m.start()]
        after = text[m.end():text.find("\n", m.end()) if "\n" in text[m.end():] else len(text)]
        attributed = any(p.search(before) for p in _ATTR_BEFORE.values()) or bool(_ATTR_AFTER.match(after))
        if attributed and count_words(m.group(1)) <= 3 and _GLOSS_AFTER.match(after):
            attributed = False
        if attributed and _HYPOTHETICAL_BEFORE.search(before):
            attributed = False
        out.append(Quote(m.group(1), m.start(1), m.end(1), attributed))
    return out


def _quote_norm(text: str) -> str:
    s = straight_quotes(nfc(text)).casefold()
    s = re.sub(r"[^\w\s]", " ", s)
    return " ".join(s.split())


def quote_problem(quote: str, sources, cap: int, lang: str = "en") -> str | None:
    """Why a public quote fails (over the cap, or not verbatim in any source), or None."""
    words = count_words(quote, lang)
    if words > cap:
        return f"quote is {words} {'tiếng' if lang == 'vn' else 'words'} (cap {cap})"
    q = _quote_norm(quote)
    if not q:
        return None
    for src in sources or ():
        if f" {q} " in f" {_quote_norm(src)} ":
            return None
    return "quote not verbatim in the sources"


def quote_ok(quote: str, sources, cap: int, lang: str = "en") -> bool:
    return quote_problem(quote, sources, cap, lang) is None


# ---------------------------------------------------------------- hooks, keyword, praise

HEDGES = {
    "en": ["maybe", "might", "I think", "kind of", "sort of", "perhaps", "could be"],
    "vn": ["có lẽ", "chắc là", "hình như", "mình nghĩ là", "có thể"],
}


def hedges_in_hook(hook: str, lang: str = "en") -> list[str]:
    return _phrase_hits(hook, HEDGES.get(lang, HEDGES["en"]))


def keyword_count(text: str, keyword: str, variants=()) -> int:
    """Occurrences of the keyword, any letter case.

    A span spelled entirely without diacritics also counts (VN "lai ao" = "lãi ảo"); a span with
    different diacritics does not ("lại áo" is another word). `variants` are extra accepted spellings.
    """
    text = nfc(text)
    folded = fold(text)
    spans: set[tuple[int, int]] = set()
    for form in [keyword, *(variants or ())]:
        form = nfc(form).strip()
        if not form:
            continue
        target = form.casefold()
        pattern = phrase_re(fold(form), 0)
        for m in pattern.finditer(folded):
            original = text[m.start():m.end()]
            ok = (" ".join(original.casefold().split()) == " ".join(target.split())
                  or strip_diacritics(original) == original)
            if ok and not any(a < m.end() and m.start() < b for a, b in spans):
                spans.add((m.start(), m.end()))
    return len(spans)


# The ask itself: a CTA verb right before the keyword ("Comment TOO LATE", "message me BADGE", "nhắn mình chữ CỨNG ĐƠ"),
# matched on folded text (no diacritics, lower case).
ASK_BEFORE = (r"(?:comment|cmt|reply|type|dm(?: me)?|message me|text me|binh luan|com"
              r"|(?<!tin )nhan(?: rieng)?(?: [^\W\d_]+)?"             # "tin nhắn" is a noun
              r"|inbox(?: [^\W\d_]+)?|go|ib)\s+(?:(?:the word|chu|tu khoa|tu)\s+)?[\"'“‘]?")
# VN: where an ask's sentence starts: a sentence end, a colon or semicolon, or a new line ("Anh chị nào đang tuyển
# hoài: nhắn tôi chữ TUYỂN HOÀI" keeps the first "tuyển hoài" outside the ask; "Em nào đang ngại chào thì comment
# NGẠI CHÀO" holds it inside).
ASK_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?…:;])\s+|\n")


def caps_or_quoted(text: str, start: int, end: int) -> bool:
    """text[start:end] is a keyword as an ask prints it: in capitals ("TUYỂN HOÀI", "CHAPTER") or in quotes."""
    letters = [c for c in text[start:end] if c.isalpha()]
    if len(letters) >= 2 and all(c.isupper() for c in letters):
        return True
    return start > 0 and text[start - 1] in "\"“'‘"


def keyword_outside_ask(text: str, keyword: str, lang: str = "en", variants=()) -> int:
    """Occurrences of the keyword outside the ask ("keyword once in the body, plus the ask").

    EN: the ask is a CTA verb right before the keyword, so "…you still have your badge, message me BADGE" holds it
    once outside. VN: the ask is the whole sentence holding a CTA verb right before the keyword in capitals or quotes,
    its lead-in too ("Em nào đang ngại chào thì comment NGẠI CHÀO" holds it only in the ask); "tin nhắn" is a noun.
    """
    forms = [f for f in (keyword, *(variants or ())) if nfc(f).strip()]
    if not forms:
        return 0
    kw = "|".join(r"\s+".join(re.escape(w) for w in fold(nfc(f)).split()) for f in forms)
    asks = re.compile(r"(?<!\w)" + ASK_BEFORE + "(" + kw + r")(?!\w)")
    if lang != "vn":
        return max(0, keyword_count(text, keyword, variants) - len(asks.findall(fold(nfc(text)))))
    outside = 0
    for sentence in ASK_SENTENCE_SPLIT_RE.split(nfc(text)):
        sentence = plain_line(sentence)          # fold() keeps positions: the ask's keyword is read in the original
        if any(caps_or_quoted(sentence, m.start(1), m.end(1)) for m in asks.finditer(fold(sentence))):
            continue
        outside += keyword_count(sentence, keyword, variants)
    return outside


STOPWORDS = {
    # EN function words and contractions (apostrophes removed)
    "a", "an", "the", "and", "or", "but", "so", "if", "then", "i", "im", "ive", "id", "ill", "you", "youre",
    "youve", "your", "yours", "we", "were", "our", "us", "it", "its", "is", "are", "was", "be", "been", "am",
    "to", "of", "in", "on", "at", "for", "with", "from", "by", "as", "about", "this", "that", "these",
    "those", "there", "theres", "here", "heres", "my", "me", "he", "she", "they", "them", "theyre", "his",
    "her", "their", "do", "does", "did", "dont", "doesnt", "didnt", "not", "no", "just", "very", "really",
    "what", "whats", "how", "why", "when", "who", "which", "can", "cant", "will", "wont", "would", "should",
    "could", "have", "has", "had", "all", "any", "some", "more", "most", "than", "too", "also", "now",
    "ok", "okay", "oh", "so", "well", "like", "get", "got", "let", "lets",
    # VN function words
    "thì", "là", "mà", "và", "của", "cái", "những", "các", "một", "này", "đó", "ấy", "kia", "ạ", "nhé",
    "nha", "à", "ơi", "với", "cho", "để", "khi", "nếu", "vì", "nên", "có", "được", "đã", "đang", "sẽ",
    "rồi", "cũng", "thế", "vậy", "đi", "nào", "gì", "ai", "đâu", "sao", "lại", "ra", "vào", "lên", "xuống",
    "mình", "bạn", "em", "anh", "chị", "tôi", "các", "mấy", "hả", "hở", "đấy", "nhỉ", "luôn",
}


def hook_stem(text: str) -> str:
    """The first 3 content words of the hook (its first line), lowercased, punctuation stripped."""
    first = next((ln for ln in nfc(text).splitlines() if ln.strip()), "")
    first = straight_quotes(first).casefold().replace("'", "")
    tokens = re.sub(r"[^\w\s]", " ", first).split()
    content = [t for t in tokens if t not in STOPWORDS]
    return " ".join(content[:3])


PRAISE = {
    "en": ["great", "excellent", "amazing", "awesome", "fantastic", "wonderful", "brilliant", "perfect",
           "impressive", "outstanding", "incredible", "superb", "stellar", "phenomenal", "love this",
           "love it", "love that", "well done", "nice work", "good job", "great job", "nailed it",
           "spot on", "beautifully", "beautiful", "powerful", "gold", "killer", "strong work"],
    "vn": ["tuyệt vời", "tuyệt quá", "tuyệt lắm", "xuất sắc", "hay quá", "hay lắm", "rất hay", "quá hay",
           "giỏi quá", "giỏi lắm", "làm tốt lắm", "ấn tượng", "hoàn hảo", "quá đỉnh", "đỉnh quá", "đỉnh thật",
           "đỉnh của chóp", "siêu hay", "chuẩn không cần chỉnh", "quá chuẩn", "thích quá"],
}


def praise_words(text: str, lang: str | None = "en") -> list[str]:
    """Praise words and phrases in `text` (lang None: both lists)."""
    if lang in PRAISE:
        phrases = PRAISE[lang]
    else:
        phrases = PRAISE["en"] + PRAISE["vn"]
    return _phrase_hits(text, phrases)


# ---------------------------------------------------------------- urgency, brackets, verdict lines

_SEAT = r"(?:spots?|seats?|places?|slots?|spaces?|copies|tickets?)"
URGENCY = {
    "en": [
        rf"\b\d+\s+(?:\w+\s+)?{_SEAT}\s+(?:left|remaining)\b",
        rf"\b{_SEAT}\s+(?:left|remaining)\b",
        rf"\b(?:only|just)\s+(?:\d+|one|two|three|four|five|a few|a handful of)\s+(?:\w+\s+)?"
        rf"(?:{_SEAT}|days?|hours?|left)\b",
        r"\b\d+\s+left\b",
        r"\btoday only\b|\bonly today\b|\bonly until\b|\bonly through\b",
        r"\blast (?:chance|call)\b|\blast (?:spots?|seats?|places?)\b|\blast day to\b|"
        r"\blast few (?:spots?|seats?|hours?|days?)\b",
        r"\b(?:cart|doors?|enrol(?:l)?ment|registration|sale|offer|sign-?ups?|applications?)\s+(?:closes?|closing)\b",
        r"\bcloses\s+(?:on|at|tonight|tomorrow|today|in|this|friday|sunday|monday|midnight)\b",
        r"\bclosing\s+(?:soon|tonight|tomorrow|today|on|at)\b",
        r"\bdeadline\b(?=.*(?:\d|tonight|tomorrow|today|midnight|monday|tuesday|wednesday|thursday|friday|"
        r"saturday|sunday))",
        r"\bends (?:tonight|today|tomorrow|at midnight|friday|sunday)\b",
        r"\b(?:price goes up|price rises|before the price)\b",
    ],
    "vn": [
        r"chỉ còn",
        r"(?<!\w)còn\s+(?:\d+|một|hai|ba|vài)\s+(?:\w+\s+)?(?:suất|chỗ|slot|vé|ngày|giờ|tiếng|bạn)(?!\w)",
        r"(?<!\w)suất cuối(?!\w)|(?<!\w)\d+\s+suất(?!\w)|(?<!\w)còn suất(?!\w)|(?<!\w)hết suất(?!\w)",
        r"hạn chót(?=.*(?:\d|hôm nay|tối nay|ngày mai|thứ|chủ nhật|nửa đêm))",
        r"(?<!\w)đóng\s+(?:cổng|link|đăng ký|đăng kí|form|lớp|giỏ|vào|lúc|sau|tối|ngày)(?!\w)",
        r"(?<!\w)(?:hôm nay thôi|duy nhất hôm nay|cơ hội cuối|(?:sắp|trước khi|sẽ) tăng giá)(?!\w)",
    ],
}
_URGENCY_RE = {lang: [re.compile(p, re.I) for p in pats] for lang, pats in URGENCY.items()}


def urgency_lines(text: str, lang: str = "en") -> list[str]:
    """Lines that use an urgency word as urgency (left, only, last, closes, deadline, today only,
    còn, chỉ còn, suất, hạn chót, đóng): "3 seats left" counts, "the only way" does not."""
    patterns = _URGENCY_RE.get(lang, _URGENCY_RE["en"])
    if lang != "en":
        patterns = patterns + _URGENCY_RE["en"]
    out = []
    for line in nfc(text).splitlines():
        if line.strip() and any(p.search(line) for p in patterns):
            out.append(line.strip())
    return out


_NEEDS_RE = re.compile(r"\[\s*(?:NEEDS|CẦN)\b[^\]\n]*(?:\]|$)", re.I | re.M)


def needs_brackets(text: str) -> list[str]:
    """Open [NEEDS: …] / [CẦN BẠN: …] brackets (any pronoun after CẦN; unclosed ones too)."""
    return [m.group(0) for m in _NEEDS_RE.finditer(nfc(text))]


READY_PREFIXES = ("Ready", "Sẵn sàng", "✓ Checked", "✓ Đã kiểm")
_CONDITIONAL_READY = re.compile(r"\bReady\s+(?:after|once|if|when|with)\b|\bSẵn sàng\s+(?:sau khi|nếu|khi)\b",
                                re.I)


def is_ready_line(verdict_line: str, prefixes=READY_PREFIXES) -> bool:
    line = plain_line(verdict_line).casefold()
    return any(line.startswith(nfc(p).casefold()) for p in prefixes)


def conditional_ready(text: str) -> list[str]:
    """'Ready after…' style wording (never allowed: a piece is Ready or it is not)."""
    return [m.group(0) for m in _CONDITIONAL_READY.finditer(nfc(text))]


def ready_with_open_bracket(verdict_line: str, piece_text: str, prefixes=READY_PREFIXES) -> bool:
    """True when a Ready verdict sits on a piece (or a verdict) that still holds an open [NEEDS]."""
    if not is_ready_line(verdict_line, prefixes):
        return False
    return bool(needs_brackets(piece_text) or needs_brackets(verdict_line))


# ---------------------------------------------------------------- claims, names, classes

_PEOPLE_WORDS = {
    "en": r"(?:clients?|students?|customers?|people|women|men|dads|moms|members|buyers)",
    "vn": r"(?:khách|học viên|người|bạn|chị em|mẹ|học trò)",
}
_TIME_WORDS = {
    "en": r"(?:days?|weeks?|months?|lbs?|pounds?|kg|kilos?)",
    "vn": r"(?:ngày|tuần|tháng|kg|ký|cân|lần)",
}
_OUTCOME = {
    "en": [r"\blos[et]\s+(?:\d|weight|fat|pounds|kg|inches|the belly)", r"\bweight\b", r"\bfat\b", r"\bbelly\b", r"\bcured?\b", r"\bheal(?:ed|s)?\b",
           r"\bpain[- ]free\b", r"\bdiabetes\b", r"\bblood pressure\b", r"\btestosterone\b", r"\bTRT\b",
           r"\bhormones?\b", r"\bincome\b", r"\brevenue\b", r"\bsalary\b", r"\b(?:a|her|his|their|my|pay) raise\b", r"\bearn(?:ed|s|ing)?\b",
           r"\bprofit\b", r"\bsix[- ]figures?\b", r"\b[67][- ]figures?\b", r"\bmoney back\b", r"\bguarantee[ds]?\b",
           r"\bdoubled\b", r"\btripled\b", r"\blanded\b", r"\bhired\b", r"\bwent from\b", r"\bjob offer\b",
           r"\bgot (?:the|a|an|her|his|their|my) (?:job |new )?(?:offer|job|role|promotion|raise|clients?)\b"],
    "vn": [r"giảm cân", r"giảm mỡ", r"giảm \d+", r"cân nặng", r"(?<!\w)chữa(?!\w)", r"khỏi bệnh", r"hết đau",
           r"thu nhập", r"doanh thu", r"(?<!\w)lãi(?!\w)", r"lợi nhuận", r"tăng lương", r"kiếm được",
           r"gấp đôi", r"gấp ba", r"hoàn tiền", r"tăng \d+"],
}
_SUPERLATIVE = re.compile(r"(?<!\w)(?:duy nhất|số 1|số một)(?!\w)|(?<!thống )(?<!hợp )(?<!đồng )(?<!đệ )(?<!\w)nhất"
                          r"(?!\s+(?:định|là|quán|thời|trí))(?!\w)|#1\b|\bnumber one\b|\bNo\.\s?1\b", re.I)
_TESTIMONIAL = {
    "en": re.compile(r"\b(?:testimonials?|my client|a client|one client|client of mine|case study|reviews?)\b", re.I),
    "vn": re.compile(r"(?<!\w)(?:học viên|khách hàng của|khách của|khách mình|feedback|cảm nhận|case)(?!\w)", re.I),
}
_PRICE_WORD = re.compile(r"(?<!\w)(?:price|priced|costs?|investment|giá|học phí|chỉ với)(?!\w)", re.I)

IDEA_FORMATS = {"idea", "drop-idea", "hook-options", "hooks", "title-options", "titles", "plan-row",
                "capture-question"}
MICRO_FORMATS = {"background-text", "story-frame", "dm-line", "subject-line", "on-screen-text", "drop-hook",
                 "drop-hooks", "thumbnail"}
CLAIMS_FORMATS = {"offer-post", "client-decision-breakdown", "ad", "sales-email", "dm-flow-price",
                  "launch-p1-seats", "launch-p4", "launch-p5", "launch-p6", "launch-p7", "launch-p8"}
STRUCTURED_FORMATS = {"brand-brain", "brand-card", "character-card", "message-map", "keyword-pick",
                      "season-plan", "research-brief", "weekly-review", "launch-plan"}
FORMAT_ALIASES = {
    "reel": "native-short", "short": "native-short", "shorts": "native-short", "tiktok": "native-short",
    "film-today": "native-short", "clip": "native-short", "bg-post": "background-text",
    "background-text-post": "background-text", "bg": "background-text", "drop": "drop",
    "todays-one-thing": "drop", "dm": "dm-line", "subject": "subject-line", "on-screen": "on-screen-text",
    "ads": "ad", "offer": "offer-post", "brand-brain-v0": "brand-brain",
}


def norm_format(fmt: str | None) -> str:
    f = re.sub(r"[\s_]+", "-", nfc(fmt or "").strip().casefold())
    f = re.sub(r"[^\w-]", "", f)
    return FORMAT_ALIASES.get(f, f)


def money_numbers(text: str) -> list[Number]:
    return [n for n in numbers_in(text) if n.kind == "money" or (n.value is not None and n.value >= 1000
            and re.search(r"(?:k|tr|triệu|tỷ|tỉ|nghìn|ngàn)", n.raw, re.I))]


def result_claims(text: str, lang: str = "en") -> list[str]:
    """Lines that claim a result: a percent (not a discount), a count of clients or people, or an
    outcome word (weight, income, revenue, lãi, doanh thu…) on a line with a number. Prices and
    durations alone are not results."""
    people = re.compile(rf"\d[\d.,]*\+?\s+(?:\w+\s+)?{_PEOPLE_WORDS.get(lang, _PEOPLE_WORDS['en'])}(?!\w)", re.I)
    discount = re.compile(r"%\s*(?:off|discount)|giảm giá|chiết khấu", re.I)
    outcome = [re.compile(p, re.I) for p in _OUTCOME.get(lang, _OUTCOME["en"])]
    out = []
    for line in nfc(text).splitlines():
        nums = [n for n in numbers_in(line) if not n.structural and not n.tagged]
        if not nums:
            continue
        pct = any(n.percent for n in nums) and not discount.search(line)
        if pct or people.search(line) or any(p.search(line) for p in outcome):
            out.append(line.strip())
    return out


def claim_triggers(text: str, lang: str = "en") -> list[str]:
    """Which §2.1 Script-claims triggers the text carries (empty list: none)."""
    text = nfc(text)
    found = []
    nums = [n for n in numbers_in(text) if not n.structural]
    unit = re.compile(rf"\d[\d.,]*\s*(?:%|k\b|tr\b|triệu|tỷ|đ|đồng|[x×]\b)|[$€£]\s?\d|[x×]\s?\d|\d[\d.,]*\+?\s+"
                      rf"(?:\w+\s+)?(?:{_PEOPLE_WORDS['en']}|{_PEOPLE_WORDS['vn']}|{_TIME_WORDS['en']}|"
                      rf"{_TIME_WORDS['vn']})(?!\w)", re.I)
    if nums and unit.search(text):
        found.append("number+result word")
    if _TESTIMONIAL.get(lang, _TESTIMONIAL["en"]).search(text) or any(q.attributed for q in quotes_in(text, lang)):
        found.append("client story or quote")
    if money_numbers(text) or (nums and _PRICE_WORD.search(text)):
        found.append("price")
    if urgency_lines(text, lang):
        found.append("urgency")
    if any(re.search(p, text, re.I) for p in _OUTCOME["en"] + _OUTCOME["vn"]):
        found.append("health/body/income outcome")
    if _SUPERLATIVE.search(text):
        found.append("superlative")
    return found


def output_class(piece_text: str, fmt: str | None, lang: str = "en") -> str:
    """Idea | Micro | Script | Script-claims | Structured, per the QA spec §2.1 trigger list.

    Order: Structured and Idea by format; a listed claims format; Micro by format or length
    (under 40 words EN / 60 tiếng VN; the Micro check covers its claims and urgency); then any
    claims trigger; otherwise Script.
    """
    f = norm_format(fmt)
    if f in STRUCTURED_FORMATS:
        return "Structured"
    if f in IDEA_FORMATS:
        return "Idea"
    if f in CLAIMS_FORMATS or (f == "dm-flow" and money_numbers(piece_text)):
        return "Script-claims"
    if f in MICRO_FORMATS or count_words(piece_text, lang) < MICRO_THRESHOLD.get(lang, 40):
        return "Micro"
    if claim_triggers(piece_text, lang):
        return "Script-claims"
    return "Script"


_NAME = r"[" + UPPER + r"][^\W\d_]+"
_NAME_PATTERNS = {
    "en": [re.compile(rf"\b(?:my client|client|a client named|named|called|coworker|boss|friend)\s+({_NAME})"),
           re.compile(rf"\b({_NAME}),\s+\d{{2}},"),
           re.compile(rf"\b({_NAME})\s+(?:said|says|told|wrote|asked|texted|messaged|landed|got|gets|earned|lost|"
                      rf"went|made|quit|was hired|is now)\b")],
    "vn": [re.compile(rf"(?<!\w)(?:chị|anh|em|bạn|cô|chú|bác|bé|học viên|khách)\s+({_NAME}(?:\s+{_NAME})?)")],
}
_NOT_NAMES = {"I", "She", "He", "They", "We", "You", "It", "This", "That", "My", "Our", "Your", "Monday",
              "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "January", "February",
              "March", "April", "May", "June", "July", "August", "September", "October", "November",
              "December", "Instagram", "Facebook", "TikTok", "LinkedIn", "YouTube", "Zalo", "Google",
              "ChatGPT", "Claude", "Notion", "Reel", "Reels", "Someone", "Everyone", "Nobody", "One"}


def names_in(text: str, lang: str = "en") -> list[str]:
    """Person names the text uses as people (after 'client', before 'said', 'chị Lan' …).

    A heuristic for the "names in cited rows" check; it never guesses at capitalised words
    without a person cue.
    """
    text = nfc(text)
    out = []
    for pattern in _NAME_PATTERNS.get(lang, []) + (_NAME_PATTERNS["en"] if lang != "en" else []):
        for m in pattern.finditer(text):
            name = m.group(1)
            if name.split()[0] not in _NOT_NAMES and name not in out:
                out.append(name)
    return out


# ---------------------------------------------------------------- format budgets

def budget_problems(fmt: str | None, hook: str, body: str, lang: str = "en", seconds: float | None = None,
                    word_rate: float | None = None, limits: dict | None = None) -> list[str]:
    """Length defects for a piece: hook ≤12 words EN / 18 tiếng VN; background-text ≤130 characters;
    DROP ≤120 words; on-screen text ≤6 words; thumbnail 2–4 words; a short within word_rate ×
    seconds ±15% (no seconds given: at most word_rate × 60). `limits` overrides by format:
    {"<format>": {"max_words": n, "min_words": n, "max_chars": n}}.
    """
    f = norm_format(fmt)
    unit = "tiếng" if lang == "vn" else "words"
    spoken = "\n".join(p for p in (hook, body) if p and p.strip())
    words = count_words(spoken, lang)
    out = []
    if hook and hook.strip():
        hook_words = count_words(hook, lang)
        if hook_words > HOOK_MAX.get(lang, 12):
            out.append(f"hook {hook_words} {unit} (max {HOOK_MAX.get(lang, 12)})")
    rule = dict((limits or {}).get(f, {}))
    if not rule:
        if f == "background-text":
            rule = {"max_chars": BG_POST_MAX_CHARS}
        elif f == "drop":
            rule = {"max_words": DROP_MAX_WORDS}
        elif f == "on-screen-text":
            rule = {"max_words": ON_SCREEN_MAX_WORDS}
        elif f == "thumbnail":
            rule = {"min_words": 2, "max_words": 4}
        elif f == "native-short":
            rate = word_rate or WORD_RATE.get(lang, 2.5)
            if seconds:
                target = rate * float(seconds)
                rule = {"min_words": int(target * (1 - WORD_RATE_TOLERANCE)),
                        "max_words": int(round(target * (1 + WORD_RATE_TOLERANCE)))}
            else:
                rule = {"max_words": int(rate * SHORT_DEFAULT_MAX_SECONDS)}
    if "max_chars" in rule:
        chars = len(nfc(spoken).strip())
        if chars > rule["max_chars"]:
            out.append(f"{chars} characters (max {rule['max_chars']})")
    if "max_words" in rule and words > rule["max_words"]:
        out.append(f"{words} {unit} (max {rule['max_words']})")
    if "min_words" in rule and words < rule["min_words"]:
        out.append(f"{words} {unit} (min {rule['min_words']})")
    return out


# ---------------------------------------------------------------- copy runs (someone else's post)

# liked.copy_note (strings) carries the real wording; these are its first-sentence cores, used when
# no note text is given (wf13-inspiration-spec §2 liked.copy_note).
COPY_NOTE_MARKERS = ("follows their post closely", "bám sát bài của họ")


def copy_tokens(text: str | None) -> list[str]:
    """NFC, casefolded, punctuation-stripped tokens (EN words / VN tiếng) for the copy-run check.

    Quotes are straightened, apostrophes inside a word dropped ("don't" → "dont") and digit
    group separators joined ("2,400" → "2400"); every other punctuation mark splits.
    """
    s = straight_quotes(nfc(text)).casefold()
    s = re.sub(r"(?<=\d)[.,](?=\d)", "", s)
    s = re.sub(r"(?<=\w)'(?=\w)", "", s)
    return re.sub(r"[^\w\s]", " ", s).split()


def stock_phrase_list(text: str | None) -> list[str]:
    """The phrases in a locales/<lang>/stock-phrases.txt body: one per line, '#' starts a comment."""
    out = []
    for line in nfc(text).splitlines():
        line = line.strip()
        if line and not line.startswith("#") and line not in out:
            out.append(line)
    return out


def _copy_strip_stock(tokens: list[str], stock: list[list[str]]) -> list[str]:
    """Tokens minus every whole stock phrase (any of them, wherever it occurs)."""
    keep = [True] * len(tokens)
    by_first: dict[str, list[list[str]]] = {}
    for phrase in stock:
        if phrase:
            by_first.setdefault(phrase[0], []).append(phrase)
    for i, tok in enumerate(tokens):
        for phrase in by_first.get(tok, ()):
            if tokens[i:i + len(phrase)] == phrase:
                for j in range(i, i + len(phrase)):
                    keep[j] = False
    return [t for t, k in zip(tokens, keep) if k]


def copy_runs(text: str, source: str, lang: str = "en", n: int | None = None, stock=()) -> list[str]:
    """Runs of ≥n tokens that `text` shares with `source` (someone else's post), in text order.

    n defaults to COPY_RUN_MIN (6 EN words / 8 VN tiếng). Tokens come from copy_tokens(); every
    stock phrase (calls to action, greetings: locales/<lang>/stock-phrases.txt) is removed from
    both sides first, so "link in bio" or "comment bên dưới" never makes or lengthens a run.
    Overlapping shared n-grams merge into one run.
    """
    n = int(n or COPY_RUN_MIN.get(lang, COPY_RUN_MIN["en"]))
    stock_tokens = [copy_tokens(p) for p in (stock or ())]
    a = _copy_strip_stock(copy_tokens(text), stock_tokens)
    b = _copy_strip_stock(copy_tokens(source), stock_tokens)
    if n < 1 or len(a) < n or len(b) < n:
        return []
    grams = {tuple(b[i:i + n]) for i in range(len(b) - n + 1)}
    spans: list[list[int]] = []
    for i in range(len(a) - n + 1):
        if tuple(a[i:i + n]) in grams:
            if spans and i <= spans[-1][1]:
                spans[-1][1] = i + n
            else:
                spans.append([i, i + n])
    out: list[str] = []
    for start, end in spans:
        run = " ".join(a[start:end])
        if run not in out:
            out.append(run)
    return out


def _mirror_units(point: str) -> set:
    """Content units of one point: non-stopword words of 3+ letters plus adjacent-word pairs
    (VN tiếng are short, so the pairs carry most of the meaning)."""
    toks = copy_tokens(point)
    units: set = {t for t in toks if t not in STOPWORDS and len(t) >= 3}
    units |= {(x, y) for x, y in zip(toks, toks[1:]) if not (x in STOPWORDS and y in STOPWORDS)}
    return units


def point_order_mirror(text: str, source: str, min_points: int = 3, share: float = 0.5) -> bool:
    """Best-effort proxy for a mirrored point order (DISTANCE): True when at least `min_points`
    of the source's points (sentences) come back in the text in the same order, each sharing at
    least half of its content units (and 2 or more) with one point of the text, and those points
    make up at least `share` of the shorter side. Topic-free shapes (hook → story → steps) with
    new content do not match: only the source's own points do.
    """
    src = [u for u in (_mirror_units(p) for p in sentences(source)) if len(u) >= 2]
    txt = [u for u in (_mirror_units(p) for p in sentences(text)) if len(u) >= 2]
    if len(src) < min_points or len(txt) < min_points:
        return False
    best = [0] * len(txt)                      # longest in-order chain ending at text point j
    for s in src:
        hits = [j for j, t in enumerate(txt) if len(s & t) >= 2 and len(s & t) >= 0.5 * len(s)]
        new = list(best)
        for j in hits:
            new[j] = max(new[j], 1 + max(best[:j], default=0))
        best = new
    chain = max(best, default=0)
    return chain >= min_points and chain >= share * min(len(src), len(txt))


def copy_note_marker(note: str) -> str:
    """The part of a copy note that marks it: its first sentence without a leading label
    ("Note:", "Lưu ý:", "Note (5 Oct 2026):") and without {slots}."""
    s = nfc(note).strip()
    s = re.sub(r"^[^\s:{}]{1,12}(?:\s+[^\s:{}]{1,12})?\s*(?:\([^)\n]*\))?\s*:\s*", "", s)
    first = next(iter(sentences(s)), "")
    chunks = [c for c in re.split(r"\{[^}]*\}", first) if copy_tokens(c)]
    return max(chunks, key=lambda c: len(copy_tokens(c))).strip(" .!?…") if chunks else ""


def has_copy_note(text: str, note: str | None = None) -> bool:
    """True when `text` carries the copy note: the marker of `note` (the rendered liked.copy_note),
    or, with no note given, one of COPY_NOTE_MARKERS. Case, punctuation and spacing are ignored."""
    markers = [copy_note_marker(note)] if note and note.strip() else list(COPY_NOTE_MARKERS)
    haystack = " " + " ".join(copy_tokens(text)) + " "
    for marker in markers:
        toks = copy_tokens(marker)
        if toks and " " + " ".join(toks) + " " in haystack:
            return True
    return False
