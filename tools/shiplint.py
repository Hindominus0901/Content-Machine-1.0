#!/usr/bin/env python3
"""Runtime lint for one batch of pieces: the LINT step of the Ship Check (QA spec §2.2-§2.3).

Ships inside the Claude skill as scripts/ship_lint.py; tools/build.py inlines
tools/cmcore/checks.py so the shipped copy is one self-contained file.

    python3 ship_lint.py batch.json          (or "-" to read stdin)
    python3 ship_lint.py batch.json --json   (adds the output class and defects as JSON)

Input: one JSON object.

    {
      "lang": "en" | "vn",
      "keyword": "CHAPTER",                       chosen signature keyword ("" skips the check)
      "keyword_variants": ["chapter"],            extra accepted spellings (VN: no-diacritic forms
                                                  are accepted automatically)
      "allowed_numbers": ["$2,400"],              numbers allowed in any piece (offer facts)
      "allowed_names": ["Dana"],                  names allowed in any piece (the coach)
      "bank": [{"id": "P-1", "text": "...",       cited rows; P-rows may carry
                "substantiated": true,            "substantiated", "consent" (true/false) and
                "consent": true, "uses": ["posts"]}],   "uses" (posts | ads | case-study)
      "ledger": [{"id": "L-1", "cap": 4, "deadline": "2027-01-20", "enforced": true}],
      "recent_hook_stems": ["not too old"],       the last 10 shipped stems
      "word_rate": 2.5,                           optional; default 2.5 EN / 3.5 VN
      "budgets": {"<format>": {"max_words": 80}}, optional per-format overrides
      "pieces": [{"id": "N2", "format": "native-short", "hook": "...", "body": "...",
                  "caption": "...", "cites": ["P-1"], "verdict_line": "...",
                  "seconds": 30}]                 "seconds" optional (shorts: word_rate ±15%)
    }

Output: one line per piece, in input order:

    N2 PASS
    N3 FAIL: number "90%" not in cited rows; keyword ×0

Checks per piece (the card's LINT line): digits, names and quotes found in the
cited rows; quotes exact and within the quote cap; a result claim needs a cited
P-row marked Substantiated + consent (ads: consent for ads); urgency only with
an enforced Ledger row; keyword exactly once; hook stem new against
recent_hook_stems and the batch; no hedge in the hook; no open [NEEDS] in a
Ready piece and no "Ready after"; the word budget for the format; every cited
ID resolves. Idea and Structured pieces get only the trace checks (numbers,
names, quotes, IDs, brackets).

The output is final and is never re-argued. Exit 0 always (it informs), or 2
when the input is not valid.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cmcore import checks as ck  # noqa: E402  (inlined into scripts/ship_lint.py by tools/build.py)

PIECE_FIELDS = ("hook", "body", "caption")


class PayloadError(ValueError):
    """The batch JSON does not follow the schema in the module docstring."""


def load_payload(raw: str) -> dict:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise PayloadError(f"not JSON: {exc}")
    if not isinstance(data, dict):
        raise PayloadError("top level must be an object")
    if data.get("lang", "en") not in ck.LANGS:
        raise PayloadError(f"lang must be one of {', '.join(ck.LANGS)}")
    pieces = data.get("pieces")
    if not isinstance(pieces, list) or not pieces:
        raise PayloadError("'pieces' must be a non-empty list")
    for key in ("keyword_variants", "allowed_numbers", "allowed_names", "bank", "ledger", "recent_hook_stems"):
        if not isinstance(data.get(key, []), list):
            raise PayloadError(f"'{key}' must be a list")
    for row in data.get("bank", []) + data.get("ledger", []):
        if not isinstance(row, dict) or not str(row.get("id", "")).strip():
            raise PayloadError("every bank and ledger row needs an 'id'")
    seen = set()
    for i, piece in enumerate(pieces):
        if not isinstance(piece, dict) or not str(piece.get("id", "")).strip():
            raise PayloadError(f"piece {i + 1} needs an 'id'")
        if piece["id"] in seen:
            raise PayloadError(f"duplicate piece id '{piece['id']}'")
        seen.add(piece["id"])
        for key in PIECE_FIELDS + ("format", "verdict_line"):
            if not isinstance(piece.get(key, ""), str):
                raise PayloadError(f"piece {piece['id']}: '{key}' must be a string")
        if not isinstance(piece.get("cites", []), list):
            raise PayloadError(f"piece {piece['id']}: 'cites' must be a list")
    return data


def _sl_norm_id(value) -> str:
    """P1, P-1 and p-1 are the same row."""
    s = str(value).strip().upper().replace(" ", "")
    if len(s) > 1 and s[0].isalpha() and s[1:].isdigit():
        s = f"{s[0]}-{s[1:]}"
    return s


def _sl_short(text: str, limit: int = 40) -> str:
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _sl_consent_ok(row: dict, fmt: str) -> bool:
    consent = row.get("consent")
    if not consent:
        return False
    if fmt == "ad":
        uses = row.get("uses")
        if uses is not None:
            return "ads" in [str(u).casefold() for u in uses]
    return True


def lint_piece(piece: dict, data: dict, bank: dict, batch_stems: list) -> tuple[str, list[str]]:
    """(output class, defects) for one piece."""
    lang = data.get("lang", "en")
    fmt = ck.norm_format(piece.get("format"))
    hook = piece.get("hook", "")
    body = piece.get("body", "")
    text = "\n".join(piece.get(k, "") for k in PIECE_FIELDS if piece.get(k, "").strip())
    cls = ck.output_class(text, fmt, lang)
    defects: list[str] = []

    cites = [_sl_norm_id(c) for c in piece.get("cites", [])]
    missing = [c for c in cites if c not in bank and c not in data["_ledger"]]
    if missing:
        defects.append("cited ID does not resolve: " + ", ".join(missing))
    rows = [bank[c] for c in cites if c in bank]
    sources = [str(r.get("text", "")) for r in rows]

    # trace: digits, names, quotes in cited rows
    enforced = [r for r in data["_ledger"].values() if r.get("enforced")]
    ledger_numbers = [str(r.get(k, "")) for r in enforced for k in ("cap", "deadline")]
    allowed = sources + [str(n) for n in data.get("allowed_numbers", [])] + ledger_numbers
    for raw in ck.unsupported_numbers(text, allowed):
        defects.append(f'number "{raw}" not in cited rows')
    known = " ".join(sources + [str(n) for n in data.get("allowed_names", [])]).casefold()
    for name in ck.names_in(text, lang):
        if name.casefold() not in known:
            defects.append(f'name "{name}" not in cited rows')
    cap = ck.QUOTE_CAP.get(lang, 15)
    for q in ck.quotes_in(text, lang):
        if ck.count_words(q.text, lang) < 4 and not q.attributed:
            continue                                   # a term or a command, not a quotation
        problem = ck.quote_problem(q.text, sources, cap, lang)
        if problem:
            defects.append(f'{problem}: "{_sl_short(q.text)}"')

    # verdict line: never Ready with an open bracket, never "Ready after"
    verdict = piece.get("verdict_line", "")
    if verdict and ck.ready_with_open_bracket(verdict, text):
        defects.append("Ready with an open [NEEDS]")
    if ck.conditional_ready(verdict):
        defects.append('conditional "Ready after" wording')
    if verdict and ck.count_words(verdict, lang) > ck.VERDICT_MAX_WORDS:
        defects.append(f"verdict line over {ck.VERDICT_MAX_WORDS} words")

    if cls in ("Idea", "Structured"):
        return cls, defects

    # claims: a result needs a substantiated, consented P-row
    by_sentence = "\n".join(ck.sentences(text))
    claims = ck.result_claims(by_sentence, lang)
    if claims:
        proof = [r for c, r in zip(cites, rows) if c.startswith("P-")
                 and r.get("substantiated") is True and _sl_consent_ok(r, fmt)]
        if not proof:
            defects.append(f'result claim without a Substantiated+consent P-row: "{_sl_short(claims[0])}"')

    # urgency only from an enforced Ledger row (a cited Ledger row must be enforced)
    urgent = ck.urgency_lines(by_sentence, lang)
    if urgent:
        cited_ledger = [data["_ledger"][c] for c in cites if c in data["_ledger"]]
        ok = all(r.get("enforced") for r in cited_ledger) if cited_ledger else bool(enforced)
        if not ok:
            defects.append(f'urgency without an enforced Ledger row: "{_sl_short(urgent[0])}"')

    keyword = str(data.get("keyword", "")).strip()
    if keyword:
        n = ck.keyword_count(text, keyword, data.get("keyword_variants", []))
        if n != 1:
            defects.append(f"keyword ×{n}")

    stem = ck.hook_stem(hook or body)
    recent = {ck.hook_stem(str(s)) for s in data.get("recent_hook_stems", [])}
    if stem and (stem in recent or stem in batch_stems):
        defects.append(f'hook stem "{stem}" used recently')
    if stem:
        batch_stems.append(stem)

    for hedge in ck.hedges_in_hook(hook or next(iter(body.splitlines()), ""), lang):
        defects.append(f'hedge in hook: "{hedge}"')

    for problem in ck.budget_problems(fmt, hook, body, lang, seconds=piece.get("seconds"),
                                      word_rate=data.get("word_rate"), limits=data.get("budgets")):
        defects.append(problem)
    return cls, defects


def lint_payload(data: dict) -> list[dict]:
    """One result per piece: {"id", "class", "result" (PASS | FAIL), "defects"}."""
    bank = {_sl_norm_id(r["id"]): r for r in data.get("bank", [])}
    data = dict(data, _ledger={_sl_norm_id(r["id"]): r for r in data.get("ledger", [])})
    stems: list[str] = []
    results = []
    for piece in data["pieces"]:
        cls, defects = lint_piece(piece, data, bank, stems)
        results.append({"id": str(piece["id"]), "class": cls,
                        "result": "FAIL" if defects else "PASS", "defects": defects})
    return results


def format_line(result: dict) -> str:
    if result["result"] == "PASS":
        return f"{result['id']} PASS"
    return f"{result['id']} FAIL: " + "; ".join(result["defects"])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ship Check LINT for one batch of pieces.")
    parser.add_argument("path", help="batch JSON file, or - for stdin")
    parser.add_argument("--json", action="store_true", help="print results as JSON (adds the output class)")
    args = parser.parse_args(argv)
    try:
        raw = sys.stdin.read() if args.path == "-" else Path(args.path).read_text(encoding="utf-8")
        data = load_payload(raw)
    except (OSError, UnicodeDecodeError, PayloadError) as exc:
        print(f"ship_lint: invalid input: {exc}", file=sys.stderr)
        return 2
    results = lint_payload(data)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for result in results:
            print(format_line(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
