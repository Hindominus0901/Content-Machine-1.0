"""Tests for evals/run.py: run packets, case assertions and grading, on the temp repo of test_graders."""
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

from test_graders import TAG, TempRepo

REPO = Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("cm_run", REPO / "evals" / "run.py")
run = importlib.util.module_from_spec(_spec)
sys.modules["cm_run"] = run
_spec.loader.exec_module(run)

CASES = r'''
[meta]
module = "message"
edition = "en"
written_by = "qa-role"

[[case]]
id = "message.en.001"
kind = "D"
persona = "test-coach"
lanes = ["S1", "floor"]
title = "The Map is 4 lines and one OK"
context = "Day 0 after the missing facts."
input = """Tuesday."""
contains = ["KNOWN FOR:"]
not_contains = ["NOT NOW"]
regex = ['(?m)^YOUR VOICE:']
not_regex = ['(?m)^\W*✓ Checked:']
verdict = ""
invariants = ["I1", "I5"]
max_words = 120
max_chars = 0
max_questions = 1
notes = "the Map"

[[case]]
id = "message.en.002"
kind = "D"
persona = "test-coach"
lanes = ["S1"]
title = "A Ready piece prints only its content"
context = ""
input = """[turn 1] write me a reel
[turn 2] thanks"""
contains = []
not_contains = []
regex = ['FILM TODAY']
not_regex = []
verdict = "Ready"
invariants = ["I3"]
max_words = 0
max_chars = 0
max_questions = 1
notes = "scope: transcript · the piece is in an earlier reply"

[[case]]
id = "message.en.003"
kind = "P"
persona = "test-coach"
lanes = ["S1"]
title = "judged"
context = ""
input = "x"
standard = "message-map"
critical = []
min_score = 8
notes = ""

[[case]]
id = "message.en.004"
kind = "D"
persona = "test-coach"
lanes = ["S0"]
title = "S0 only"
context = ""
input = "Start"
verdict = "Hard stop"
invariants = []
notes = ""
'''

MAP_REPLY = (TAG + "Your Map\n\nKNOWN FOR: I help women 45+ land a new role in 8–12 weeks.\n"
             "3 TOPICS: coffee first · your 24 years count · ask for 20 minutes\nYOUR WORD: CHAPTER\n"
             "YOUR VOICE: plain · dry · warm · talks to them as \"you\"\n\n"
             "We'll run this for 4 weeks. OK, or change a line.\n\nNEXT → Say OK, or change a line.")
PIECE = (TAG + "Film today\n\nFILM TODAY (under 30 s)\nOn-screen: Coffee before resume\n"
         "First line: \"Stop applying. Ask for 20 minutes.\"\n\nNEXT → Film it now.")


class RunPackets(TempRepo):
    def setUp(self):
        super().setUp()
        self.write("evals/cases/message.en.toml", CASES)
        kitdir = self.root / "kit"
        kitdir.mkdir()
        (kitdir / "1-INSTRUCTIONS.txt").write_text("instructions", encoding="utf-8")
        (kitdir / "CONTENT-MACHINE-EN.md").write_text("method", encoding="utf-8")
        self.kit = ({"instructions": kitdir / "1-INSTRUCTIONS.txt", "method": kitdir / "CONTENT-MACHINE-EN.md",
                     "phone": kitdir / "PHONE-STARTER.txt"}, "abc123")
        self.out = self.root / "out"

    def packets(self, **kw):
        args = dict(suite="day0", edition="en", lane="S1", persona_ids=[], out_root=self.out, kit=self.kit,
                    today="2026-10-06")
        args.update(kw)
        return run.make_packets(self.root, **args)

    def test_day0_packet_per_persona_and_repeat(self):
        made = self.packets(repeat=2, tag="p2")
        self.assertEqual([d.name for d in made], ["p2-day0-en-test-coach-S1-r1", "p2-day0-en-test-coach-S1-r2"])
        meta = json.loads((made[0] / "meta.json").read_text(encoding="utf-8"))
        self.assertEqual(meta, {"persona": "en/test-coach", "edition": "en", "lane": "S1", "build_sha": "abc123",
                                "suite": "day0", "repeat": 1})
        kit = sorted(p.name for p in (made[0] / "packet" / "kit").iterdir())
        self.assertEqual(kit, ["1-INSTRUCTIONS.txt", "CONTENT-MACHINE-EN.md"])
        coach = (made[0] / "packet" / "COACH.md").read_text(encoding="utf-8")
        self.assertIn("Never read `expected.toml`", coach)
        self.assertIn("evals/personas/en/test-coach", coach)
        machine = (made[0] / "packet" / "MACHINE.md").read_text(encoding="utf-8")
        self.assertIn("2026-10-06", machine)
        self.assertNotIn("expected", machine)

    def test_s0_has_no_method_file(self):
        made = self.packets(lane="S0")
        self.assertEqual([p.name for p in (made[0] / "packet" / "kit").iterdir()], ["1-INSTRUCTIONS.txt"])
        self.assertIn("compact mode", (made[0] / "packet" / "MACHINE.md").read_text(encoding="utf-8"))

    def test_refusals(self):
        with self.assertRaisesRegex(run.RunError, "S3"):
            self.packets(lane="S3")
        with self.assertRaisesRegex(run.RunError, "not found"):
            self.packets(persona_ids=["nobody"])
        self.packets()
        with self.assertRaisesRegex(run.RunError, "exists"):
            self.packets()
        with self.assertRaisesRegex(run.RunError, "--module"):
            self.packets(suite="cases")

    def test_cases_packets_skip_p_cases_and_other_lanes(self):
        made = self.packets(suite="cases", module="message")
        self.assertEqual([d.name for d in made], ["message_en_001-S1-r1", "message_en_002-S1-r1"])
        coach = (made[1] / "packet" / "COACH.md").read_text(encoding="utf-8")
        self.assertIn("Turn 1:\n\n```text\nwrite me a reel\n```", coach)
        self.assertIn("Turn 2:\n\n```text\nthanks\n```", coach)
        self.assertNotIn("FILM TODAY", coach)                  # assertions never reach the simulator
        meta = json.loads((made[0] / "meta.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["case"], "message.en.001")
        with self.assertRaisesRegex(run.RunError, "not found"):
            self.packets(suite="cases", module="message", case_ids=["message.en.999"])


class CaseAssertions(TempRepo):
    def setUp(self):
        super().setUp()
        self.write("evals/cases/message.en.toml", CASES)

    def grade_case(self, case_id: str, turns: list[tuple]) -> dict:
        d = self.run_dir(turns, case=case_id)
        return run.grade_run(d, self.root)

    def test_map_case_passes_and_session_checks_do_not_count(self):
        g = self.grade_case("message.en.001", [("coach", "Tuesday."), ("machine", MAP_REPLY)])
        self.assertTrue(g["case"]["pass"], g["case"])
        self.assertIn("day0_timing", g["info_failed"])          # no film step in a slice of a session
        self.assertNotIn("day0_timing", g["failed"])
        self.assertTrue(g["pass"], g["failed"])
        self.assertTrue(json.loads((self.root / "evals" / "runs" / g["run"] / "grades.json")
                                   .read_text(encoding="utf-8"))["pass"])

    def test_old_map_fails_its_assertions(self):
        old = MAP_REPLY.replace("YOUR VOICE:", "NOT NOW:") + "\n✓ Checked: your words"
        g = self.grade_case("message.en.001", [("coach", "Tuesday."), ("machine", old)])
        fails = " ".join(g["case"]["failures"])
        self.assertIn('not_contains "NOT NOW"', fails)
        self.assertIn("regex", fails)
        self.assertIn("not_regex", fails)
        self.assertFalse(g["pass"])

    def test_limits_and_listed_invariants(self):
        two_q = MAP_REPLY.replace("We'll run this", "Is this you? Does it fit? We'll run this")
        g = self.grade_case("message.en.001", [("coach", "Tuesday."), ("machine", two_q)])
        fails = " ".join(g["case"]["failures"])
        self.assertIn("questions (max 1)", fails)
        self.assertIn("I5 failed", fails)

    def test_ready_verdict_means_no_status_line(self):
        turns = [("coach", "write me a reel"), ("machine", PIECE), ("coach", "thanks"),
                 ("machine", TAG + "Next\n\nGood luck with it.\n\nNEXT → Say 'next' tomorrow.")]
        g = self.grade_case("message.en.002", turns)
        self.assertEqual(g["case"]["scope"], "transcript")
        self.assertTrue(g["case"]["pass"], g["case"])
        noisy = PIECE.replace("\n\nNEXT", "\nReady to film · I'd post it: your words\n\nNEXT")
        turns2 = [("coach", "write me a reel"), ("machine", noisy), ("coach", "thanks"),
                  ("machine", TAG + "Next\n\nReady to film · I'd post it: your words\n\nNEXT → Say 'next'.")]
        g2 = self.grade_case("message.en.002", turns2)
        self.assertFalse(g2["case"]["pass"])
        self.assertTrue(any(f.startswith("verdict Ready") for f in g2["case"]["failures"]), g2["case"])

    def test_hard_stop_verdict_needs_the_line(self):
        g = self.grade_case("message.en.004", [("coach", "Start"), ("machine", TAG + "Setup\n\nHi.\n\nNEXT → Talk.")])
        self.assertIn("verdict Hard stop", " ".join(g["case"]["failures"]))
        ok = (TAG + "Post\n\nNot writing \"guaranteed job\": no proof. Give me the real result and I'll write it."
              "\n\nNEXT → Tell me the real result.")
        self.assertTrue(self.grade_case("message.en.004", [("coach", "Start"), ("machine", ok)])["case"]["pass"])

    def test_scope_each_reply(self):
        case = {"id": "x", "kind": "D", "notes": "scope: each reply · …", "contains": ["KNOWN FOR"],
                "not_contains": ["praise"], "max_questions": 1}
        d = self.run_dir([("coach", "a"), ("machine", MAP_REPLY), ("coach", "b"),
                          ("machine", TAG + "x\n\nWhat? Why? How?\n\nNEXT → go.")])
        res = run.check_case(case, run.graders.load_run(d, self.root))
        self.assertEqual(res["scope"], "each")
        self.assertEqual(len(res["failures"]), 1)
        self.assertIn("questions", res["failures"][0])

    def test_summary_table(self):
        g = self.grade_case("message.en.001", [("coach", "Tuesday."), ("machine", MAP_REPLY)])
        table = run.summary_rows([g])
        self.assertIn("| Run | Persona | Lane |", table)
        self.assertIn("| en/test-coach |", table)


if __name__ == "__main__":
    unittest.main()
