"""Tests for evals/run.py: run packets, case assertions and grading, on the temp repo of test_graders."""
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
import zipfile
from pathlib import Path
from unittest import mock

from test_graders import PERSONA, TAG, TempRepo

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
        self.assertIn("- Today's date: Tuesday 6 October 2026.", machine)
        self.assertNotIn("expected", machine)

    def machine(self, **kw) -> str:
        return (self.packets(**kw)[0] / "packet" / "MACHINE.md").read_text(encoding="utf-8")

    def test_p18_machine_gets_a_real_run_date(self):
        """Retest VG6/G7 P18: "Today's date: the date in the transcript" gave the simulators nothing (no transcript row
        has a date), so EN dated its card 12 Oct while VN used 6 Oct. The packet writes the run's date: --today, the
        persona's day0 (its time kept), else the day the packet is made."""
        self.assertIn("- Today's date: Tuesday 6 October 2026.", self.machine())
        self.write("evals/personas/en/test-coach/persona.toml", 'day0 = "2026-10-12 06:45"\n' + PERSONA)
        self.assertIn("- Today's date: Monday 12 October 2026, 06:45.", self.machine(tag="d0"))     # the persona wins
        self.assertIn("- Today's date: Tuesday 6 October 2026.", self.machine(tag="cs", suite="cases", module="message"))
        self.write("evals/personas/en/test-coach/persona.toml", PERSONA)
        for today in ("", "2026-10-06"):
            with self.subTest(today=today):
                text = self.machine(tag=f"t{len(today)}", today=today)
                self.assertNotIn("the date in the transcript", text)
                self.assertRegex(text, r"- Today's date: (?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) "
                                       r"\d{1,2} [A-Z][a-z]+ \d{4}\.\n")
        # the CLI passes no placeholder either: a bare run (no --today) is dated by run_date()
        with mock.patch.object(run, "make_packets", return_value=[]) as made:
            self.assertEqual(run.main(["--root", str(self.root), "packet", "--suite", "day0", "--edition", "en",
                                       "--lane", "S1"]), 0)
        self.assertEqual(made.call_args.args[-1], "")
        self.assertEqual(run.run_date("2026-10-06"), "Tuesday 6 October 2026")
        self.assertEqual(run.run_date("2026-10-11 20:45"), "Sunday 11 October 2026, 20:45")
        self.assertEqual(run.run_date("6 Oct 2026"), "6 Oct 2026")            # not an ISO date: given as is
        self.assertEqual(run.run_date("2026-13-40"), "2026-13-40")
        self.assertRegex(run.run_date(""), r"^\w+day \d{1,2} \w+ \d{4}$")

    def test_protocol_timing_drafts_and_list_facts(self):
        """Retest G3/VG2 §8: one timing convention (P12), no grading or leak scan on a draft (P13), the persona's
        platform and list said in chunk 1 when the dump prompt asks for them (VP-2)."""
        made = self.packets()
        readme = (made[0] / "packet" / "README.md").read_text(encoding="utf-8")
        coach = (made[0] / "packet" / "COACH.md").read_text(encoding="utf-8")
        for text in (readme, coach):
            self.assertIn("is when the reply arrives", text)                                   # P12
            self.assertIn("the coach's turn + about 0.3 min", text)
            self.assertIn("reading time goes on their next turn", text)
        self.assertIn("Write each machine turn once; never run `grade` or a leak scan on a draft.", readme)   # P13
        self.assertIn("A draft that used a persona fact\n  stays as written and fails the run", readme)
        self.assertIn("If the dump prompt asks where you post and about your list", coach)       # VP-2
        self.assertIn("add it as one sentence at the end of chunk 1", coach)

    def test_protocol_long_chunks_go_in_two_sends(self):
        """Retest VG3/G4 §8 P10: a dump chunk over about 400 words is two sends, split at a paragraph, as the dump
        prompt asks (first sends of 595-871 words made the early win late and the consultant's film-ready 20.3)."""
        made = self.packets()
        step2 = " ".join((made[0] / "packet" / "COACH.md").read_text(encoding="utf-8").split())
        self.assertIn("A chunk over about 400 words (VN tiếng) goes in two sends, split at a paragraph, as the dump "
                      "prompt asks.", step2)
        self.assertIn("one coach turn per send", step2)
        self.assertNotIn("one coach turn each", step2)

    def test_protocol_first_send_ends_by_300_words(self):
        """Retest VG5/G6 §8 P16: chunk 1's first send ends by about 300 words (VN tiếng), about 3 minutes, as the dump
        prompt says "every 2–3 minutes" (Erin's 425-word first send took 4.3 min and made the early win a warning)."""
        step2 = " ".join((self.packets()[0] / "packet" / "COACH.md").read_text(encoding="utf-8").split())
        self.assertIn("Chunk 1's first send ends by about 300 words (VN tiếng), about 3 minutes of talk, at a paragraph "
                      "or sentence end, as the dump prompt says \"every 2–3 minutes\"; the rest of chunk 1 is the next "
                      "send (P16).", step2)
        self.assertIn("A chunk over about 400 words (VN tiếng) goes in two sends", step2)       # P10 still holds

    def test_session_turn_cap_per_edition(self):
        """Retest VG5/G6 §8 G43: the coach side stops after the session budget + 4 turns, VN from session_max_turns_vn
        (11: the xưng hô turn), EN from session_max_turns (10)."""
        self.write("evals/acceptance.toml", "[day0]\nsession_max_turns = 10\nsession_max_turns_vn = 11\n")
        en = " ".join((self.packets()[0] / "packet" / "COACH.md").read_text(encoding="utf-8").split())
        self.assertIn("or after 14 coach turns.", en)
        self.write("evals/personas/vn/test-vn/persona.toml", 'id = "test-vn"\nedition = "vn"\n')
        vn = " ".join((self.packets(edition="vn", tag="vn")[0] / "packet" / "COACH.md").read_text(encoding="utf-8")
                      .split())
        self.assertIn("or after 15 coach turns.", vn)

    def test_protocol_states_the_soft_cut(self):
        """Retest VG4/G5 §8 P15: the round brief told the VN simulators "about 1,500 tiếng"; the packet now states the
        kit's cut from acceptance.toml [day0] (~1,200, pasted posts left out), so a simulator files no kit break over
        a brief that disagrees with the kit."""
        step2 = " ".join((self.packets()[0] / "packet" / "COACH.md").read_text(encoding="utf-8").split())
        self.assertIn("The kit cuts the dump softly past about 1,200 words of your talk, your pasted posts not counted "
                      "(acceptance.toml [day0]).", step2)
        self.write("evals/acceptance.toml", "[day0]\nsession_max_turns = 10\ndump_cut_words_vn = 1100\n")
        self.write("evals/personas/vn/test-vn/persona.toml", 'id = "test-vn"\nedition = "vn"\n')
        made = self.packets(edition="vn", tag="vn")
        step2 = " ".join((made[0] / "packet" / "COACH.md").read_text(encoding="utf-8").split())
        self.assertIn("past about 1,100 tiếng of your talk, your pasted posts not counted", step2)
        # the repo's own thresholds: about 1,200 for both editions, pasted posts left out
        repo = run.load_toml(REPO / "evals" / "acceptance.toml")["day0"]
        self.assertEqual((repo["dump_cut_words_en"], repo["dump_cut_words_vn"]), (1200, 1200))
        text = (REPO / "evals" / "acceptance.toml").read_text(encoding="utf-8")
        self.assertIn("pasted posts left out", text)
        self.assertIn("~1,200 tiếng", text)

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


class FT1Packets(TempRepo):
    """Retest FT1 (qa/runs/retest-ft1/review.md §7 fix 5): the packet ships the edition's Level-ups and, with --plugin,
    the plugin's companion skills; --web lets the machine side search for the background research pass. The packet
    tells which, and meta.json, the run id and the summary say so."""

    def setUp(self):
        super().setUp()
        kitdir = self.root / "kit"
        (kitdir / "Level-ups").mkdir(parents=True)
        (kitdir / "1-INSTRUCTIONS.txt").write_text("instructions", encoding="utf-8")
        (kitdir / "CONTENT-MACHINE-EN.md").write_text("method", encoding="utf-8")
        for name in ("RESEARCH-EN.md", "STRATEGY-EN.md", "LAUNCH-EN.md", "BOARD-EN.md"):
            (kitdir / "Level-ups" / name).write_text(f"# {name}\n§CM-LISTEN steps", encoding="utf-8")
        (kitdir / "Level-ups" / "Board").mkdir()
        (kitdir / "Level-ups" / "Board" / "Bank.csv").write_text("a,b\n", encoding="utf-8")
        zpath = self.root / "plugin.zip"
        with zipfile.ZipFile(zpath, "w") as zf:
            for name in ("skills/content-machine-en/SKILL.md", "skills/cm-research-en/SKILL.md",
                         "skills/cm-strategy-en/SKILL.md", "skills/cm-research-vn/SKILL.md",
                         "skills/content-machine-vn/SKILL.md", "agents/cm-listener.md"):
                zf.writestr(f"content-machine/{name}", f"body of {name}")
            zf.writestr("content-machine/skills/cm-research-en/RESEARCH-EN.md", "the level-up, in the kit already")
            zf.writestr("content-machine/README.md", "readme")
        self.kit = ({"instructions": kitdir / "1-INSTRUCTIONS.txt", "method": kitdir / "CONTENT-MACHINE-EN.md",
                     "phone": kitdir / "PHONE-STARTER.txt",
                     "levelups": sorted((kitdir / "Level-ups").glob("*.md")), "plugin_zip": zpath}, "abc123")
        self.out = self.root / "out"

    def packets(self, **kw):
        args = dict(suite="day0", edition="en", lane="S1", persona_ids=[], out_root=self.out, kit=self.kit,
                    today="2026-10-06")
        args.update(kw)
        return run.make_packets(self.root, **args)

    def tree(self, packet: Path) -> list[str]:
        base = packet / "packet" / "kit"
        return sorted(p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file())

    def machine(self, packet: Path) -> str:
        return (packet / "packet" / "MACHINE.md").read_text(encoding="utf-8")

    def test_the_project_kit_ships_the_level_ups(self):
        [packet] = self.packets()
        self.assertEqual(self.tree(packet), ["1-INSTRUCTIONS.txt", "CONTENT-MACHINE-EN.md", "Level-ups/BOARD-EN.md",
                                             "Level-ups/LAUNCH-EN.md", "Level-ups/RESEARCH-EN.md",
                                             "Level-ups/STRATEGY-EN.md"])           # the .md files, not the board's csv
        text = self.machine(packet)
        self.assertIn("**Level-ups:** `BOARD-EN.md`, `LAUNCH-EN.md`, `RESEARCH-EN.md`, `STRATEGY-EN.md` are project files in "
                      "`kit/Level-ups/`", text)
        self.assertIn("read the §CM- part the job needs, never the whole file", text)
        self.assertEqual(self.tree(self.packets(lane="floor", tag="f")[0])[-1], "Level-ups/STRATEGY-EN.md")

    def test_compact_mode_has_no_level_ups(self):
        [packet] = self.packets(lane="S0")
        self.assertEqual(self.tree(packet), ["1-INSTRUCTIONS.txt"])
        self.assertNotIn("Level-ups", self.machine(packet))

    def test_a_kit_without_level_ups_is_unchanged(self):
        kit = ({k: v for k, v in self.kit[0].items() if k not in ("levelups", "plugin_zip")}, "abc123")
        [packet] = self.packets(kit=kit)
        self.assertEqual(self.tree(packet), ["1-INSTRUCTIONS.txt", "CONTENT-MACHINE-EN.md"])
        self.assertNotIn("Level-ups", self.machine(packet))

    def test_the_web_line_is_lane_aware(self):
        [off] = self.packets()
        text = self.machine(off)
        self.assertIn("- Searching the web is not possible in this run: where the kit says \"search if you can\", you "
                      "can't.", text)
        self.assertNotIn("Web search and page fetch are on", text)
        self.assertNotIn("web", json.loads((off / "meta.json").read_text(encoding="utf-8")))
        [on] = self.packets(web=True, tag="w")
        self.assertEqual(on.name, "w-day0-en-test-coach-S1-web-r1")
        text = self.machine(on)
        self.assertNotIn("Searching the web is not possible", text)
        self.assertIn("**Web search and page fetch are on in this run** (lane option `web`)", text)
        self.assertIn("for the background research pass only (Day 0, §CM-LISTEN", text)
        for rule in ("open a page before you quote it (unopened = unread)", "people by role, never by name or handle",
                     "never log in, post, react, follow, DM or join", "never touch the coach's computer or apps",
                     "\"## Research log\""):
            self.assertIn(rule, text)
        self.assertIn("# Machine side (S1+web)", text)
        self.assertIn("- A link the coach sends is never opened here (unopened = unread).", text)       # I20 still holds
        self.assertEqual(json.loads((on / "meta.json").read_text(encoding="utf-8"))["web"], True)
        readme = (on / "packet" / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Web lane", readme)
        self.assertIn("Add `## Research log` to `notes.md`", readme)
        self.assertNotIn("## Web lane", (off / "packet" / "README.md").read_text(encoding="utf-8"))

    def test_the_web_lane_runs_the_pass_as_a_separate_agent_and_logs_the_real_turns(self):
        """Retest-ft2 fix 4: the research pass sees only the transcript so far, never the persona files, and each query is
        logged with the turn it really ran after; the leak check on that log is named in the packet."""
        [off] = self.packets()
        [on] = self.packets(web=True, tag="w")
        text = self.machine(on)
        for phrase in ("Run the research pass as if by a separate agent that sees only the transcript so far",
                       "never the persona files, `answers.md`, `expected.toml`", "Log the real turn of each query",
                       "`Q<n> · after turn <N> · <query>`", "not a turn it is modelled in later or earlier",
                       "a run of two or more content words that only the persona's answer bank holds",
                       "is a leak and makes the run invalid"):
            self.assertIn(phrase, text)
        self.assertNotIn("separate agent", self.machine(off))
        readme = (on / "packet" / "README.md").read_text(encoding="utf-8")
        for phrase in ("Run the research pass as if by a separate agent", "Q6 · after turn 3 · \"which clients\" agency owner",
                       "A modelled turn", "research_leaks", "research_log", "`KEEP: <pattern> (lines 1, 2, 3)`"):
            self.assertIn(phrase, readme)
        self.assertNotIn("research_leaks", (off / "packet" / "README.md").read_text(encoding="utf-8"))

    def test_the_plugin_form_ships_the_companion_skills(self):
        [packet] = self.packets(plugin=True, tag="p")
        self.assertEqual(packet.name, "p-day0-en-test-coach-S1-plugin-r1")
        files = self.tree(packet)
        self.assertIn("plugin/skills/content-machine-en/SKILL.md", files)
        self.assertIn("plugin/skills/cm-research-en/SKILL.md", files)
        self.assertIn("plugin/skills/cm-strategy-en/SKILL.md", files)
        self.assertIn("plugin/agents/cm-listener.md", files)
        self.assertFalse([f for f in files if "-vn" in f or f.endswith("README.md") and "plugin" in f])   # one edition only
        self.assertNotIn("plugin/skills/cm-research-en/RESEARCH-EN.md", files)                  # the kit's Level-ups hold it
        self.assertIn("Level-ups/RESEARCH-EN.md", files)
        self.assertEqual((packet / "packet" / "kit" / "plugin" / "skills" / "cm-research-en" / "SKILL.md").read_text(
            encoding="utf-8"), "body of skills/cm-research-en/SKILL.md")
        text = self.machine(packet)
        self.assertIn("**Plugin form:** the coach installed the plugin.", text)
        self.assertIn("never ask the coach to upload a Level-ups file", text)
        self.assertIn("# Machine side (S1+plugin)", text)
        self.assertEqual(json.loads((packet / "meta.json").read_text(encoding="utf-8"))["plugin"], True)
        both = self.packets(plugin=True, web=True, tag="b")[0]
        self.assertEqual(both.name, "b-day0-en-test-coach-S1-web-plugin-r1")
        self.assertEqual(run.lane_label(json.loads((both / "meta.json").read_text(encoding="utf-8"))), "S1+web+plugin")

    def test_the_plugin_needs_a_method_lane_and_a_built_zip(self):
        with self.assertRaisesRegex(run.RunError, "--plugin needs a lane with the method file"):
            self.packets(lane="S0", plugin=True)
        self.assertFalse((self.out / "day0-en-test-coach-S0-plugin-r1").exists())            # nothing half-written
        kit = (dict(self.kit[0], plugin_zip=self.root / "missing.zip"), "abc123")
        with self.assertRaisesRegex(run.RunError, "missing.zip not found"):
            self.packets(plugin=True, kit=kit)
        self.assertFalse(self.out.exists() and any(self.out.iterdir()))
        empty = self.root / "empty.zip"
        with zipfile.ZipFile(empty, "w") as zf:
            zf.writestr("content-machine/skills/cm-research-vn/SKILL.md", "x")
        with self.assertRaisesRegex(run.RunError, "holds no en skills"):
            self.packets(plugin=True, kit=(dict(self.kit[0], plugin_zip=empty), "abc123"))

    def test_the_cli_flags(self):
        with mock.patch.object(run, "make_packets", return_value=[]) as made:
            self.assertEqual(run.main(["--root", str(self.root), "packet", "--suite", "day0", "--edition", "en",
                                       "--lane", "S1", "--web", "--plugin"]), 0)
        self.assertEqual((made.call_args.kwargs["web"], made.call_args.kwargs["plugin"]), (True, True))
        with mock.patch.object(run, "make_packets", return_value=[]) as made:
            run.main(["--root", str(self.root), "packet", "--suite", "day0", "--edition", "en", "--lane", "S1"])
        self.assertEqual((made.call_args.kwargs["web"], made.call_args.kwargs["plugin"]), (False, False))

    def test_the_summary_names_the_lane_options(self):
        row = run.summary_rows([{"run": "r1", "persona": "en/x", "lane": "S1", "web": True, "pass": True, "failed": [],
                                 "protocol": [], "summary": {"coach_turns": 5}, "checks": []}])
        self.assertIn("| S1+web |", row)
        self.assertIn("| S1 |", run.summary_rows([{"run": "r2", "persona": "en/x", "lane": "S1", "pass": True,
                                                   "failed": [], "protocol": [], "summary": {}, "checks": []}]))

    def test_a_run_graded_with_the_options_says_so(self):
        d = self.run_dir([("coach", "Tuesday."), ("machine", MAP_REPLY)], web=True, plugin=True)
        g = run.grade_run(d, self.root)
        self.assertEqual((g["web"], g["plugin"]), (True, True))

    def test_the_leak_check_reads_the_kits_subfolders(self):
        """A kit/Level-ups/ folder made check_leaks read a directory as a file; its wording is the kit's, never a leak."""
        self.write("evals/personas/en/test-coach/voice-samples.md",
                   "## Phrases\n1. Tells the story first, then the step, every single time\n")
        pdir = self.root / "evals" / "personas" / "en" / "test-coach"
        kit = self.root / "packet-kit"
        (kit / "Level-ups").mkdir(parents=True)
        (kit / "plugin" / "skills" / "cm-research-en").mkdir(parents=True)
        (kit / "1-INSTRUCTIONS.txt").write_text("x", encoding="utf-8")
        (kit / "Level-ups" / "STRATEGY-EN.md").write_text("Tells the story first, then the step, every single time.",
                                                          encoding="utf-8")
        (kit / "plugin" / "skills" / "cm-research-en" / "SKILL.md").write_text("skill", encoding="utf-8")
        rows = [{"turn": 1, "role": "coach", "text": "hi", "t_min": None},
                {"turn": 1, "role": "machine", "text": "rhythm: tells the story first, then the step, every single time",
                 "t_min": None}]
        self.assertEqual(run.check_leaks(rows, pdir, kit, "en")["status"], "pass")
        self.assertFalse(run.check_leaks(rows, pdir, None, "en")["pass"])          # without the kit's wording it leaks


class ResearchLeaks(TempRepo):
    """Retest-ft2 §8 fix 4 (qa/runs/retest-ft2/review.md §2): the research pass of a web run is audited. EN's topic 1 changed
    on "which clients", a phrase of the persona's undictated answer bank that sat in queries 6, 10 and 11 and that a
    5-word leak window cannot see."""

    ANSWERS = ("## Dump chunk 1\nI run an agency. Best year in the history of the company and I'm asking the bank for payroll.\n\n"
               "## Answer bank\n- **What clients ask most:** \"Which clients actually make us money?\" Then \"Can we afford to hire?\"\n"
               "- Cash is tight in the bank every March.\n")

    def setUp(self):
        super().setUp()
        self.write("evals/personas/en/test-coach/answers.md", self.ANSWERS)
        self.pdir = self.root / "evals" / "personas" / "en" / "test-coach"

    def rows(self, *turns):
        return [dict({"turn": i // 2 + 1, "role": role, "text": text, "t_min": None})
                for i, (role, text) in enumerate(turns)]

    def log_dir(self, queries: str, name="a") -> Path:
        d = self.root / "evals" / "runs" / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "notes.md").write_text("# notes\n\n## Research log\n\n### Queries\n" + queries + "\n### Pages opened\n"
                                    "1. https://x.com/a · X · Jan 2026\n\n## Grade\nfine\n", encoding="utf-8")
        return d

    def check(self, queries, rows, lang="en", web=True, kit=None):
        return run.check_research_leaks(self.log_dir(queries), rows, self.pdir, kit, lang, web)

    DIALOGUE = ("coach", "Start"), ("machine", "Hi."), ("coach", "I run an agency and it was our best year."), \
        ("machine", "Go on."), ("coach", "We're busy and broke, the bank account is empty."), ("machine", "Map.")

    def test_a_phrase_only_the_answer_bank_holds_makes_the_run_invalid(self):
        res = self.check('Q6 · after turn 3 · "we\'re busy" agency owner "which clients" making money\n',
                         self.rows(*self.DIALOGUE))
        self.assertFalse(res["pass"])
        self.assertEqual(res["status"], "fail")
        self.assertIn('query 6', res["evidence"][0])
        self.assertIn('"which clients" is in the persona\'s answer bank and was never said (2+ words in a row)', res["evidence"][0])
        self.assertIn("after turn 3", res["evidence"][0])
        self.assertEqual(res["queries"], 1)

    def test_the_words_the_coach_said_by_that_turn_are_fine_and_later_ones_warn(self):
        said = self.rows(*self.DIALOGUE[:2], ("coach", "Everyone asks which clients make us money."), ("machine", "Go on."),
                         ("coach", "Cash."), ("machine", "Map."))
        self.assertEqual(self.check('Q6 · after turn 2 · "which clients" agency owner\n', said)["status"], "pass")
        res = self.check('Q6 · after turn 1 · "which clients" agency owner\n', said)                       # said at turn 2: a modelled turn
        self.assertEqual((res["pass"], res["status"]), (True, "warn"))
        late = self.rows(*self.DIALOGUE[:2], ("coach", "Hello."), ("machine", "Go on."),
                         ("coach", "Everyone asks which clients make us money."), ("machine", "Map."))
        res = self.check('Q6 · after turn 2 · "which clients" agency owner\n', late)          # said, but at turn 3
        self.assertTrue(res["pass"])
        self.assertEqual(res["status"], "warn")
        self.assertIn("first said at turn 3, after the turn the log gives", res["warnings"][0])
        # the machine's own earlier reply and the kit's wording are known, too
        said_by_machine = self.rows(("coach", "Start"), ("machine", "Which clients are they?"), ("coach", "Agency owners."),
                                    ("machine", "Go on."))
        self.assertTrue(self.check('Q1 · after turn 2 · "which clients" agency\n', said_by_machine)["pass"])
        kit = self.root / "kit"
        kit.mkdir()
        (kit / "1-INSTRUCTIONS.txt").write_text("Ask which clients make money.", encoding="utf-8")
        self.assertTrue(self.check('Q1 · after turn 1 · "which clients" agency\n', self.rows(*self.DIALOGUE), kit=kit)["pass"])

    def test_one_word_function_words_quotes_and_plurals(self):
        rows = self.rows(*self.DIALOGUE)
        for query, ok in (('Q1 · after turn 3 · clients forum\n', True),                           # one word of a phrase
                          ('Q1 · after turn 3 · money in the bank\n', True),                       # "in the" runs hold a function word
                          ('Q1 · after turn 3 · "cash" "bank" agency\n', True),                    # separate quotes are separate runs
                          ('Q1 · after turn 3 · which, clients\n', True),                          # a comma ends a run
                          ('Q1 · after turn 3 · which client make money\n', False),                # the singular is the same phrase
                          ('Q1 · after turn 3 · Cash is tight in the bank every March\n', False),
                          ('Q1 · after turn 3 · "afford to hire" owners\n', True)):                # "afford to": a function word breaks it
            with self.subTest(query=query):
                self.assertEqual(self.check(query, rows)["pass"], ok, query)

    def test_vn_runs_need_four_tieng(self):
        self.write("evals/personas/vn/test-hanh/answers.md",
                   "## Dump chunk 1\nMình mở spa.\n\n## Answer bank\n- Các em hay nói: \"em ngại chào liệu trình lắm chị ơi\".\n")
        pdir = self.root / "evals" / "personas" / "vn" / "test-hanh"
        rows = self.rows(("coach", "Chị mở spa nhỏ."), ("machine", "Dạ."), ("coach", "Khách làm một buổi rồi thôi."), ("machine", "Dạ."))
        d = self.log_dir('- T2: Q1 "chủ spa nhỏ ngại chào liệu trình cho khách" · Q2 "chủ spa ngại chào liệu" · Q3 "spa khách làm một buổi"\n')
        res = run.check_research_leaks(d, rows, pdir, None, "vn")
        self.assertFalse(res["pass"])
        self.assertEqual(len(res["evidence"]), 1, res["evidence"])
        self.assertIn('query 1', res["evidence"][0])
        self.assertIn('"ngại chào liệu trình" is in the persona\'s answer bank', res["evidence"][0])
        self.assertIn("4+ tiếng in a row", res["evidence"][0])
        self.assertEqual(res["n"], 4)

    def test_every_query_names_the_turn_it_ran_after(self):
        rows = self.rows(*self.DIALOGUE)
        res = self.check("1. agency owner forum\n2. cash payroll agency\n", rows)
        self.assertFalse(res["pass"])
        self.assertIn('queries 1, 2 name no turn: log each as "Q<n> · after turn <N> · <query>"', res["evidence"][0])
        res = self.check("Q1 · after turn 9 · agency owner forum\n", rows)
        self.assertIn("logged after turn 9, a turn this run does not have (3 coach turns)", res["evidence"][0])
        res = self.check("Reply 2 (after chunk 1):\n1. agency owner forum\nT3: Q2 \"cash payroll agency\"\n", rows)   # the older headers
        self.assertTrue(res["pass"], res)

    def test_a_web_run_needs_its_log_and_a_plain_run_is_not_asked(self):
        d = self.root / "evals" / "runs" / "none"
        d.mkdir(parents=True)
        res = run.check_research_leaks(d, self.rows(*self.DIALOGUE), self.pdir, None, "en", web=True)
        self.assertFalse(res["pass"])
        self.assertIn("a web-lane run needs its Research log", res["evidence"][0])
        self.assertIsNone(run.check_research_leaks(d, self.rows(*self.DIALOGUE), self.pdir, None, "en", web=False))
        (d / "notes.md").write_text("# notes\n\n## Research log\nNo queries ran: the coach quit first.\n", encoding="utf-8")
        res = run.check_research_leaks(d, self.rows(*self.DIALOGUE), self.pdir, None, "en", web=True)
        self.assertTrue(res["pass"])
        self.assertEqual(res["queries"], 0)

    def test_protocol_checks_and_grade_run_carry_it(self):
        d = self.run_dir([("coach", "Start"), ("machine", MAP_REPLY)], web=True)
        meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
        ids = [c["id"] for c in run.protocol_checks(d, self.root, meta)]
        self.assertEqual(ids, ["turns", "pace", "leaks", "edits", "research_leaks"])             # a web run with no log fails
        self.assertFalse(run.protocol_checks(d, self.root, meta)[-1]["pass"])
        plain = self.run_dir([("coach", "Start"), ("machine", MAP_REPLY)])
        plain_meta = json.loads((plain / "meta.json").read_text(encoding="utf-8"))
        self.assertEqual([c["id"] for c in run.protocol_checks(plain, self.root, plain_meta)], ["turns", "pace", "leaks", "edits"])
        (plain / "notes.md").write_text("## Research log\n\n### Queries\nQ1 · after turn 1 · agency owner\n", encoding="utf-8")
        self.assertEqual(run.protocol_checks(plain, self.root, plain_meta)[-1]["id"], "research_leaks")     # a log, web or not
        graded = run.grade_run(d, self.root)
        self.assertFalse(graded["valid"])
        self.assertFalse(graded["pass"])
        self.assertIn("no: research_leaks", run.summary_rows([graded]))
        # a run whose queries are clean is valid
        clean = self.run_dir([("coach", "Start"), ("machine", MAP_REPLY)], web=True)
        (clean / "notes.md").write_text("## Research log\n\n### Queries\nQ1 · after turn 1 · agency owner forum\n", encoding="utf-8")
        self.assertTrue(run.grade_run(clean, self.root)["valid"])


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

    def test_summary_prints_active_film_minutes_and_the_run_name(self):
        """Review G16 / VG-16: film-ready in active minutes, the clock in brackets; a run graded from inside its
        folder still has its name."""
        self.assertEqual(run.film_cell({"film_ready_minutes": 56.1, "film_ready_active_minutes": 16.1}), "16.1 (56.1)")
        self.assertEqual(run.film_cell({"film_ready_minutes": 19.1, "film_ready_active_minutes": 19.1}), "19.1")
        self.assertEqual(run.film_cell({}), "–")
        table = run.summary_rows([{"run": "r1", "persona": "en/x", "lane": "S1", "pass": False, "failed": ["I8"],
                                   "edited": 2, "protocol": [], "summary": {"coach_turns": 5},
                                   "checks": [{"id": "day0_timing", "details": {
                                       "map_coach_turns": 4, "film_ready_minutes": 61.9,
                                       "film_ready_active_minutes": 16.9}}]}])
        self.assertIn("| yes (edited: 2) | no | I8 | 5 | 4 | 16.9 (61.9) |", table)
        d = self.run_dir([("coach", "Tuesday."), ("machine", MAP_REPLY)])
        here = Path.cwd()
        try:
            import os
            os.chdir(d)
            self.assertEqual(run.graders.grade(Path("."), self.root)["run"], d.name)
        finally:
            os.chdir(here)


class Protocol(TempRepo):
    def rows(self, *turns):
        return [dict({"turn": i // 2 + 1, "role": role, "text": text, "t_min": None}, **extra)
                for i, (role, text, *rest) in enumerate(turns) for extra in [rest[0] if rest else {}]]

    def test_turns_alternate_and_quit_ends_the_run(self):
        ok = run.check_turns(self.rows(("coach", "a"), ("machine", "b"), ("coach", "bye", {"quit": True})))
        self.assertTrue(ok["pass"], ok)
        bad = run.check_turns(self.rows(("coach", "a"), ("coach", "b")))
        self.assertIn("two coach turns in a row", " ".join(bad["evidence"]))
        self.assertIn("no reply", " ".join(bad["evidence"]))

    def test_pace_needs_time_to_dictate_a_chunk(self):
        chunk = " ".join(f"word{i}" for i in range(320))
        self.write("evals/personas/en/test-coach/answers.md", f"## Dump chunk 1\n{chunk}\n\n## Answer bank\nx\n")
        pdir = self.root / "evals" / "personas" / "en" / "test-coach"
        fast = [{"turn": 1, "role": "machine", "text": "go", "t_min": 1.0},
                {"turn": 2, "role": "coach", "text": chunk, "t_min": 1.5}]
        self.assertFalse(run.check_pace(fast, pdir)["pass"])
        slow = [dict(fast[0]), dict(fast[1], t_min=4.0)]
        self.assertTrue(run.check_pace(slow, pdir)["pass"])
        away = [dict(fast[0]), dict(fast[1], t_min=40.0, away_min=38.5)]
        self.assertFalse(run.check_pace(away, pdir)["pass"])

    def test_pace_pasted_posts_are_not_dictated(self):
        """Retest VG4/G5 §8 P14: Tuấn's W2 repeats a dump line, so one shared 12-gram made the W1+W2 paste read as 135
        dictated words; pasted posts leave the dictation test and take ≥0.5 min each instead."""
        line = "căn nào hợp là do con số chứ hổng phải do cái rèm nhà mẫu nha bạn"
        chunk = " ".join(f"chữ{i}" for i in range(200)) + " " + line
        self.write("evals/personas/vn/test-vn/answers.md", f"## Dump chunk 1\n{chunk}\n\n## Answer bank\nx\n")
        w1 = "Tính trước rồi hẵng cọc nha. Sáng thứ Bảy có chị gọi mình từ trong toilet nhà mẫu, nói nhỏ xíu."
        w2 = f"Nói thiệt nè, tui bán bảo hiểm, tui có nhận hoa hồng. {line.capitalize()}. Ai sắp cọc thì inbox tui."
        self.write("evals/personas/vn/test-vn/written-posts.md", f"# Bài\n\n## W1 · TikTok\n\n{w1}\n\n## W2 · FB\n\n{w2}\n")
        pdir = self.root / "evals" / "personas" / "vn" / "test-vn"

        def pace(text: str, minutes: float) -> dict:
            rows = [{"turn": 4, "role": "machine", "text": "Em nhận rồi.", "t_min": 9.5},
                    {"turn": 5, "role": "coach", "text": text, "t_min": 9.5 + minutes}]
            return run.check_pace(rows, pdir)

        paste = f"{w1}\n\n{w2}"
        tuan = pace(paste, 0.7)                                  # two posts in 0.7 min: still short, for the right reason
        self.assertEqual(tuan["evidence"], ["turn 5: 2 pasted posts in 0.7 min (needs ≥1.0 at 0.5 min a post)"])
        self.assertTrue(pace(paste, 1.0)["pass"])
        self.assertTrue(pace("2 bài mình viết:\n\n" + paste, 1.1)["pass"])       # a short intro line is no dictation
        # a dictated chunk with a post pasted after it: the chunk's words at 160 wpm plus 0.5 min for the post
        both = pace(f"{chunk}\n\n{w1}", 1.5)
        self.assertEqual(both["evidence"], ["turn 5: 217 dictated words and 1 pasted post in 1.5 min (needs ≥1.9 at "
                                            "160 wpm, 0.5 min a post)"])
        self.assertTrue(pace(f"{chunk}\n\n{w1}", 1.9)["pass"])
        self.assertFalse(pace(chunk, 1.0)["pass"])               # dictation alone keeps its old reading
        self.assertEqual(pace(chunk, 1.0)["evidence"], ["turn 5: 217 dictated words in 1.0 min (needs ≥1.4 at 160 wpm)"])

    def test_leaks_fail_in_voice_fields_and_warn_elsewhere(self):
        self.write("evals/personas/en/test-coach/voice-samples.md",
                   "## Phrases\n1. Tells the story first, then the step, every single time\n")
        pdir = self.root / "evals" / "personas" / "en" / "test-coach"
        rows = self.rows(("coach", "I coach people out of corporate jobs."),
                         ("machine", "rhythm: tells the story first, then the step, every time"))
        res = run.check_leaks(rows, pdir, None, "en")
        self.assertFalse(res["pass"])
        prose = self.rows(("coach", "hi"), ("machine", "You tell the story first, then the step, every single time."))
        res2 = run.check_leaks(prose, pdir, None, "en")
        self.assertTrue(res2["pass"])
        self.assertEqual(res2["status"], "warn")
        said = self.rows(("coach", "I always tell the story first, then the step, every single time."),
                         ("machine", "rhythm: the story first, then the step, every single time"))
        self.assertEqual(run.check_leaks(said, pdir, None, "en")["status"], "pass")

    def test_leaks_fail_in_the_visible_voice_lines(self):
        """Verifier hole: a persona line in the card top's HOW YOU SAY IT or the Map's YOUR VOICE only warned. The
        line is read one quote apart from its label, so the kit's 'often says "…"' never joins the coach's words."""
        self.write("evals/personas/en/test-coach/voice-samples.md",
                   "## Phrases\n1. Tells the story first, then the step, every single time\n"
                   "2. She often says cheap quotes are quotes still missing something\n")
        pdir = self.root / "evals" / "personas" / "en" / "test-coach"
        labels = ("how you say it", "your voice")
        for line in ("HOW YOU SAY IT: tells the story first, then the step, every time · warm",
                     "YOUR VOICE: tells the story first, then the step, every time"):
            with self.subTest(line=line):
                rows = self.rows(("coach", "I coach people out of corporate jobs."), ("machine", line))
                self.assertFalse(run.check_leaks(rows, pdir, None, "en", labels)["pass"])
                self.assertTrue(run.check_leaks(rows, pdir, None, "en")["pass"])       # no labels: a warning
        said = self.rows(("coach", "I always say: cheap quotes are quotes still missing something."),
                         ("machine", 'YOUR VOICE: warm · often says "cheap quotes are quotes still missing something"'))
        self.assertTrue(run.check_leaks(said, pdir, None, "en", labels)["pass"])
        self.assertEqual(run.voice_labels(REPO, "en"), ("how you say it", "your voice"))

    def test_leaks_read_toml_values_and_list_items_apart(self):
        """Review G18: a TOML key never joins its value, a machine field label never joins its value, and list items
        are read apart; a persona line the coach never said still fails a voice field."""
        self.write("evals/personas/en/test-coach/expected.toml",
                   '[voice]\nopeners_closers = ["Here\'s the thing nobody tells you.", "Every time."]\n'
                   'never_say = ["revenue is vanity, profit is sanity", "crush it"]\n')
        pdir = self.root / "evals" / "personas" / "en" / "test-coach"
        corpus = run.leak_corpus(pdir, 6)
        self.assertNotIn("openers closers here's the thing nobody", corpus)
        pasted = self.rows(("coach", "Here's the thing nobody tells you. Every time."),
                           ("machine", 'openers_closers: "Here\'s the thing nobody tells you." | "Every time."'))
        self.assertTrue(run.check_leaks(pasted, pdir, None, "en")["pass"])
        joined = self.rows(("coach", "I say make it make sense, and I check the bank every morning."),
                           ("machine", "phrases: make it make sense | I check the bank"))
        self.assertTrue(run.check_leaks(joined, pdir, None, "en")["pass"])
        copied = self.rows(("coach", "I run an agency."),
                           ("machine", "never_say: revenue is vanity, profit is sanity | crush it"))
        res = run.check_leaks(copied, pdir, None, "en")
        self.assertFalse(res["pass"])
        self.assertIn("revenue is vanity profit is sanity", res["evidence"][0])
        # a whole persona phrase shorter than a leak n-gram, copied as a list item, still leaks
        self.write("evals/personas/en/test-coach/voice-samples.md", "## Phrases\n1. Okay. Here's the math.\n")
        short = self.rows(("coach", "I run an agency."),
                          ("machine", 'phrases=["Client by client"] openers_closers=["Okay. Here\'s the math."]'))
        self.assertIn("okay here's the math", " ".join(run.check_leaks(short, pdir, None, "en")["evidence"]))
        said = self.rows(("coach", "Okay. Here's the math, honestly."),
                         ("machine", 'openers_closers=["Okay. Here\'s the math."]'))
        self.assertTrue(run.check_leaks(said, pdir, None, "en")["pass"])


    def test_leaks_short_lifts_of_undictated_answers_warn(self):
        """Retest VG5/G6 §8 P17: Tuấn's machine lifted 5-7 tiếng from answer-bank lines he never said ("ngồi tính trước
        rồi mới dẫn đi"), under the 8-tiếng leak n-gram. A run of 5 from an answers.md paragraph no coach turn covered
        is a warning, never a failure, even in a voice field; a dictated line or the coach's own words add none."""
        line = "Tại tui ngồi tính trước rồi mới dẫn đi coi nhà."
        self.write("evals/personas/vn/test-vn/answers.md",
                   "## Dump chunk 1\nTui ngồi tính với từng nhà, mai mình ngồi tính rồi hẵng cọc.\n\n## Answer bank\n"
                   f"- **Vì sao khách chọn mình:** \"{line}\"\n- **Số giờ/tuần:** \"2 tiếng là hết cỡ.\"\n")
        pdir = self.root / "evals" / "personas" / "vn" / "test-vn"
        chunk = "Tui ngồi tính với từng nhà, mai mình ngồi tính rồi hẵng cọc."
        lift = "Nhà nào muốn coi thì mình ngồi tính trước rồi mới dẫn đi."
        res = run.check_leaks(self.rows(("coach", chunk), ("machine", lift)), pdir, None, "vn")
        self.assertEqual((res["pass"], res["status"], res["short_n"]), (True, "warn", 5))
        self.assertEqual(res["warnings"], ['turn 1: "ngồi tính trước rồi mới dẫn đi" (undictated answers.md, 5+ tiếng)'])
        voice = run.check_leaks(self.rows(("coach", chunk), ("machine", f"phrases: {lift}")), pdir, None, "vn")
        self.assertTrue(voice["pass"], voice)                                   # a warning, never a failure
        self.assertEqual(len(voice["warnings"]), 1)
        # he said the line: its paragraph is covered (the POST_RUN test) and the lift is his words
        said = self.rows(("coach", chunk), ("machine", "Em nhận rồi."), ("coach", line), ("machine", lift))
        self.assertEqual(run.check_leaks(said, pdir, None, "vn")["status"], "pass")
        corpus = run.undictated_corpus(said, pdir, 5)
        self.assertNotIn("ngồi tính trước rồi mới", corpus)
        self.assertIn("ngồi tính trước rồi mới", run.undictated_corpus(said[:2], pdir, 5))
        self.assertNotIn("ngồi tính với từng nhà", corpus)                   # chunk 1 was dictated
        # a run of 8+ is listed once, by the n-gram tier, not again by the short tier
        long = run.check_leaks(self.rows(("coach", chunk), ("machine", line)), pdir, None, "vn")
        self.assertEqual(long["warnings"], ['turn 1: "tại tui ngồi tính trước rồi mới dẫn đi coi nhà"'])
        # EN reads 5 words
        self.write("evals/personas/en/test-coach/answers.md",
                   "## Dump chunk 1\nI was at HQ 24 years.\n\n## Answer bank\n- **Why they pick me:** \"I ask for "
                   "the coffee before the resume, every time.\"\n")
        en = run.check_leaks(self.rows(("coach", "I was at HQ 24 years."),
                                       ("machine", "Coffee first, so the coffee before the resume.")),
                             self.root / "evals" / "personas" / "en" / "test-coach", None, "en")
        self.assertEqual(en["warnings"], ['turn 1: "the coffee before the resume" (undictated answers.md, 5+ words)'])


class Edits(TempRepo):
    """Review P8: the first grade freezes the transcript; later changes must be logged leak removals."""

    TURNS = [("coach", "Tuesday."), ("machine", MAP_REPLY)]

    def edit(self, d: Path, old: str, new: str, log: list | None = None, role: str = "machine") -> None:
        rows = [json.loads(x) for x in (d / "transcript.jsonl").read_text(encoding="utf-8").splitlines()]
        for row in rows:
            if row["role"] == role:
                row["text"] = row["text"].replace(old, new)
        (d / "transcript.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
                                            encoding="utf-8")
        if log is not None:
            meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
            meta["edits"] = log
            (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")

    def edits(self, g: dict) -> dict:
        return next(p for p in g["protocol"] if p["id"] == "edits")

    def test_first_grade_freezes_and_unlogged_edits_invalidate(self):
        d = self.run_dir(self.TURNS)
        first = run.grade_run(d, self.root)
        self.assertTrue((d / "transcript.raw.jsonl").exists())
        self.assertEqual((first["edited"], self.edits(first)["pass"]), (0, True))
        self.edit(d, "plain · dry · warm", "plain · warm")
        second = run.grade_run(d, self.root)
        self.assertEqual(second["edited"], 1)
        self.assertFalse(second["valid"])
        self.assertIn('no entry in meta.json "edits"', " ".join(self.edits(second)["evidence"]))

    def test_logged_leak_removal_is_valid_and_counted(self):
        d = self.run_dir(self.TURNS)
        run.grade_run(d, self.root)
        self.edit(d, "plain · dry · warm", "plain · warm", [{"turn": 2, "field": "YOUR VOICE",
                                                             "before": "plain · dry · warm", "after": "plain · warm",
                                                             "reason": "leak: dry"}])
        g = run.grade_run(d, self.root)
        self.assertTrue(self.edits(g)["pass"], self.edits(g))
        self.assertEqual(g["edited"], 1)
        self.assertTrue(g["valid"])

    def test_a_logged_leak_cannot_cover_other_rewrites_in_the_turn(self):
        """Verifier hole: a small logged leak removal used to cover any other change in the same machine turn."""
        d = self.run_dir(self.TURNS)
        run.grade_run(d, self.root)
        self.edit(d, "plain · dry · warm", "plain · warm", [{"turn": 2, "field": "YOUR VOICE",
                                                             "before": "plain · dry · warm", "after": "plain · warm",
                                                             "reason": "leak: dry"}])
        self.edit(d, "YOUR WORD:", "YOUR WORD (fixed):")
        g = run.grade_run(d, self.root)
        self.assertFalse(g["valid"])
        self.assertIn("changed beyond its logged edits", " ".join(self.edits(g)["evidence"]))

    def test_other_changes_invalidate(self):
        d = self.run_dir(self.TURNS)
        run.grade_run(d, self.root)
        self.edit(d, "plain · dry · warm", "plain · warm", [{"turn": 2, "field": "YOUR VOICE", "before": "plain · dry",
                                                             "after": "plain · warm", "reason": "reads better"}])
        self.assertIn("not a leak removal", " ".join(self.edits(run.grade_run(d, self.root))["evidence"]))
        d2 = self.run_dir(self.TURNS)
        run.grade_run(d2, self.root)
        self.edit(d2, "Tuesday.", "Wednesday.", role="coach")
        self.assertIn("a coach row changed", " ".join(self.edits(run.grade_run(d2, self.root))["evidence"]))

    def test_new_turns_after_the_first_grade_are_not_edits(self):
        d = self.run_dir(self.TURNS)
        run.grade_run(d, self.root)
        with open(d / "transcript.jsonl", "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"turn": 2, "role": "coach", "text": "ok", "t_min": 3.0}) + "\n")
            fh.write(json.dumps({"turn": 2, "role": "machine", "text": TAG + "Week 1\nNEXT → ok", "t_min": 4.0}) + "\n")
        g = run.grade_run(d, self.root)
        self.assertEqual((g["edited"], self.edits(g)["appended"], self.edits(g)["pass"]), (0, 2, True))


if __name__ == "__main__":
    unittest.main()
