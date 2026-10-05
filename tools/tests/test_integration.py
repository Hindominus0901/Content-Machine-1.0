"""Cross-tool agreement on the real repo files (P1 integration).

tools/cmcore/checks.py ships inside the skill and may not import the repo, so it
hard-codes the per-edition numbers and the verdict prefixes. These tests keep
those copies in step with editions/*.toml and strings/*.toml, and check that the
transcript graders recognise every verdict line the strings define.
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(REPO / "evals"))

import cmlib  # noqa: E402
import graders  # noqa: E402
from cmcore import checks as ck  # noqa: E402

PARAM_COPIES = {            # editions/<id>.toml [params] key -> checks.py copy
    "word_rate": ck.WORD_RATE,
    "micro_threshold": ck.MICRO_THRESHOLD,
    "quote_cap": ck.QUOTE_CAP,
    "hook_max": ck.HOOK_MAX,
    "verdict_max_words": ck.VERDICT_MAX_WORDS,
    "drop_max_words": ck.DROP_MAX_WORDS,
    "bg_post_max_chars": ck.BG_POST_MAX_CHARS,
}
SLOT_VALUES = {"verb": "post", "evidence": "P-1 story", "question": "What price?", "defect": "no hook",
               "n": "N2", "line": "I made 10k", "fact": "number", "step": "Map"}


def fill(text: str) -> str:
    return re.sub(r"\{([a-z_]+)\}", lambda m: SLOT_VALUES.get(m.group(1), "x"), text)


class EditionParamsMatchChecks(unittest.TestCase):
    def test_checks_constants_equal_edition_params(self):
        for ed_id in cmlib.EDITIONS:
            params = cmlib.load_edition(ed_id, REPO).params
            for key, copy in PARAM_COPIES.items():
                with self.subTest(edition=ed_id, param=key):
                    self.assertIn(key, params)
                    want = copy[ed_id] if isinstance(copy, dict) else copy
                    self.assertEqual(params[key], want, f"editions/{ed_id}.toml {key} != tools/cmcore/checks.py")


class CopyChecksMatchAcceptance(unittest.TestCase):
    """checks.py COPY_RUN_MIN and COPY_NOTE_MARKERS are copies too (wf13-inspiration-spec §2, §6)."""

    def test_copy_run_min_equals_acceptance_copy(self):
        copy = cmlib.load_toml(REPO / "evals" / "acceptance.toml")["copy"]
        self.assertEqual(ck.COPY_RUN_MIN, {"en": copy["en_words"], "vn": copy["vn_tieng"]})

    def test_a_stock_phrase_alone_is_never_a_copy_run(self):
        for lang in ck.LANGS:
            path = REPO / "locales" / lang / "stock-phrases.txt"
            if not path.exists():
                continue
            phrases = ck.stock_phrase_list(path.read_text(encoding="utf-8"))
            for phrase in phrases:
                with self.subTest(lang=lang, phrase=phrase):
                    self.assertEqual(ck.copy_runs(phrase, phrase, lang, n=1, stock=phrases), [])

    def test_liked_strings_are_recognised(self):
        """Once strings carry liked.copy_note / liked.cant_open (P2), the graders and the fallback find them."""
        for ed_id in cmlib.EDITIONS:
            strings, _ = graders.load_strings(REPO, ed_id)
            note = strings.get("liked.copy_note", "")
            if note.strip():
                with self.subTest(edition=ed_id, key="liked.copy_note"):
                    self.assertTrue(ck.has_copy_note(note, note))
                    self.assertTrue(ck.has_copy_note(note), "COPY_NOTE_MARKERS no longer match liked.copy_note")
            line = strings.get("liked.cant_open", "")
            if line.strip():
                with self.subTest(edition=ed_id, key="liked.cant_open"):
                    run = type("RunStub", (), {"strings": strings, "lang": ed_id})()
                    pattern = graders._cant_open_pattern(run)
                    self.assertTrue(pattern.search(ck.straight_quotes(fill(line))))


class StringsMatchRuntimeChecks(unittest.TestCase):
    def rendered(self, ed: cmlib.Edition, key: str) -> str:
        return cmlib.render(ed.strings[key], ed, "kit").strip()

    def test_ready_verdicts_use_a_ready_prefix(self):
        for ed_id in cmlib.EDITIONS:
            ed = cmlib.load_edition(ed_id, REPO)
            for key in ("verdict.ready", "verdict.ready_downgraded", "checked.prefix"):
                with self.subTest(edition=ed_id, key=key):
                    line = fill(self.rendered(ed, key))
                    self.assertTrue(ck.is_ready_line(line), f"{key} {line!r} not a Ready line for checks.py")
            for key in ("verdict.needs", "verdict.draft_queued", "verdict.draft_fixable", "verdict.hardstop"):
                with self.subTest(edition=ed_id, key=key):
                    self.assertFalse(ck.is_ready_line(fill(self.rendered(ed, key))))

    def test_needs_tag_is_an_open_bracket(self):
        for ed_id in cmlib.EDITIONS:
            ed = cmlib.load_edition(ed_id, REPO)
            with self.subTest(edition=ed_id):
                self.assertTrue(ck.needs_brackets(fill(self.rendered(ed, "needs.tag"))))

    def test_graders_recognise_every_verdict_and_the_next_line(self):
        for ed_id in cmlib.EDITIONS:
            strings, _ = graders.load_strings(REPO, ed_id)
            matcher = graders.Matcher(strings, ed_id)
            for key in sorted(k for k in strings if k.startswith("verdict.")):
                with self.subTest(edition=ed_id, key=key):
                    kind = matcher.verdict_kind(ck.plain_line(fill(strings[key])))
                    self.assertEqual(kind, key.split(".", 1)[1])
            with self.subTest(edition=ed_id, key="checked.prefix"):
                self.assertEqual(matcher.verdict_kind(ck.plain_line(strings["checked.prefix"] + " numbers, names")),
                                 "checked")
            with self.subTest(edition=ed_id, key="next.prefix"):
                self.assertTrue(matcher.is_next(ck.plain_line(strings["next.prefix"] + " say next")))


if __name__ == "__main__":
    unittest.main()
