"""Tests for schemas/*.toml, tools/cmschema.py and tools/hub_build_prompt.py.

Each test copies the four schema files into a temporary repo with minimal
editions and strings, so nothing here depends on prose, strings or other
content a later phase writes.
"""
from __future__ import annotations

import contextlib
import copy
import csv
import io
import re
import shutil
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import cmlib  # noqa: E402
import cmschema  # noqa: E402
import hub_build_prompt  # noqa: E402
from cmlib import CMError  # noqa: E402

STATUS_FLOW = ["Idea", "Scripted", "Filmed", "Edited", "Posted", "Reviewed"]
WEEKLY_SUFFIXES = {"P", "N1", "N2", "C1", "C2", "C3", "C4", "C5", "K", "T", "E", "D", "A1"}
# Wording lint rejects in rendered dist text (E142, E143).
BANNED_IN_DIST = ("fill in", "fill out", "fill this", "fill-in", "điền vào", "Content Waterfall",
                  "Content GPS", "4-3-2-1", "Authenticity Machine", "Founder OS")

EN_STRINGS = {
    "hub.content.slot_key": "The piece's unique key. The machine finds the row by it.",
    "hub.view.this_week": "This Week",
    "hub.sheets.start.title": "Start here: {{name}}",
}
VN_STRINGS = {
    "hub.content.slot_key": "Mã riêng của bài. Máy tìm đúng dòng nhờ mã này.",
    "hub.view.this_week": "Tuần này",
    "hub.sheets.start.title": "Bắt đầu: {{name}}",
}


def toml_value(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def make_repo(tmp: Path, name: str = "Content Machine", strings: bool = True) -> Path:
    """A temporary repo: the real schemas plus minimal editions and strings."""
    (tmp / "schemas").mkdir(parents=True)
    for schema in cmschema.SCHEMAS:
        shutil.copy(REPO / "schemas" / f"{schema}.toml", tmp / "schemas" / f"{schema}.toml")
    for ed, suffix in (("en", "EN"), ("vn", "VN")):
        skill = "content-machine" + ("-vn" if ed == "vn" else "")
        path = tmp / "editions" / f"{ed}.toml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(f"""\
            [edition]
            id = "{ed}"
            lang = "{ed}"
            name = {toml_value(name)}
            skill_name = "{skill}"
            file_suffix = "{suffix}"
            zip_name = "Content-Machine-{suffix}"

            [params]
            currency = "{'$' if ed == 'en' else 'đ'}"
            """), encoding="utf-8")
    if strings:
        (tmp / "strings").mkdir()
        en = ["[strings]"] + [f'"{k}" = {toml_value(v)}' for k, v in EN_STRINGS.items()]
        vn = ["[strings]"] + [f'"{k}" = {{ text = {toml_value(v)}, src = "{cmlib.sha10(EN_STRINGS[k])}" }}'
                              for k, v in VN_STRINGS.items()]
        (tmp / "strings" / "en.toml").write_text("\n".join(en) + "\n", encoding="utf-8")
        (tmp / "strings" / "vn.toml").write_text("\n".join(vn) + "\n", encoding="utf-8")
    return tmp


class TempRepo(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = make_repo(Path(self._tmp.name))
        self.data = {name: cmschema.load(name, self.root) for name in cmschema.SCHEMAS}
        self.hub = self.data["hub"]
        self.keys = self.data["keys"]
        self.banks = self.data["banks"]
        self.card = self.data["brand-card"]

    def tearDown(self):
        self._tmp.cleanup()

    def findings(self, data: dict) -> list[str]:
        return [msg for _, _, msg in cmschema.check(self.root, data)]


# ================================================================ the schema files

class SchemaFilesTest(TempRepo):
    def test_every_schema_parses_with_version_1(self):
        for name, data in self.data.items():
            with self.subTest(schema=name):
                self.assertEqual(data.get("schema_version"), 1)

    def test_validator_finds_nothing(self):
        self.assertEqual(cmschema.check(self.root), [])

    def test_every_property_has_name_and_type(self):
        for db in cmschema.databases(self.hub):
            for p in cmschema.properties(self.hub, db):
                with self.subTest(db=db, prop=p.get("name")):
                    self.assertIsInstance(p.get("name"), str)
                    self.assertTrue(p["name"].strip())
                    self.assertIn(p.get("type"), cmschema.PROPERTY_TYPES)
                    self.assertIsInstance(p.get("sheet_column"), bool)
                    self.assertTrue(cmlib.KEY_RE.match(p.get("description_key", "")))

    def test_status_runs_idea_to_reviewed_and_ai_sets_three(self):
        status = cmschema.prop(self.hub, "content", "Status")
        self.assertEqual(status["type"], "status")
        self.assertEqual(status["options"], STATUS_FLOW)
        self.assertEqual(status["ai_may_set"], ["Idea", "Scripted", "Reviewed"])
        self.assertEqual(set(status["on_coach_word"]), {"Filmed", "Edited", "Posted"})
        self.assertEqual(self.hub["rules"]["ai_status"], ["Idea", "Scripted", "Reviewed"])

    def test_ai_may_set_is_a_subset_of_options(self):
        found = 0
        for db in cmschema.databases(self.hub):
            for p in cmschema.properties(self.hub, db):
                if "ai_may_set" in p:
                    found += 1
                    with self.subTest(db=db, prop=p["name"]):
                        self.assertLessEqual(set(p["ai_may_set"]), set(p["options"]))
        self.assertGreaterEqual(found, 1)

    def test_content_has_the_planned_properties(self):
        names = {p["name"] for p in cmschema.properties(self.hub, "content")}
        wanted = {"Slot Key", "Run Key", "Title", "Status", "Post Date", "Archive", "Pillar", "Why", "Job", "Rung",
                  "Format", "Platform", "Keyword", "Hook", "CTA", "Series", "Episode",
                  "Views", "Sends", "Saves", "Leads", "Result", "Edge", "Uses", "Needs"}
        self.assertLessEqual(wanted, names)
        self.assertEqual(cmschema.prop(self.hub, "content", "Job")["options"], ["Educate", "Entertain", "Convert"])
        series = cmschema.prop(self.hub, "content", "Series")
        self.assertEqual((series["type"], series["relation_to"]), ("relation", "series"))
        self.assertTrue(cmschema.prop(self.hub, "runs", "Run Key"))

    def test_quality_group(self):
        quality = [p for p in cmschema.notion_properties(self.hub, "content") if p["group"] == "Quality"]
        self.assertEqual([p["name"] for p in quality], ["Result", "Edge", "Uses", "Needs"])
        self.assertEqual(cmschema.prop(self.hub, "content", "Result")["options"],
                         ["Ready", "Draft", "Override", "Pending"])
        self.assertEqual(cmschema.prop(self.hub, "content", "Edge")["range"], [0, 10])
        self.assertTrue(cmschema.prop(self.hub, "content", "Edge")["internal"])

    def test_rules(self):
        rules = self.hub["rules"]
        self.assertIn("never delete", rules["never_delete"])
        self.assertEqual(rules["upsert_keys"]["content"], "Slot Key")
        self.assertIn("same upsert", rules["quality_in_same_upsert"])
        self.assertEqual(rules["max_hub_calls_per_run"], 30)
        self.assertTrue(self.hub["paste"]["key_first"])

    def test_each_tab_starts_with_its_key(self):
        for db, key in self.hub["rules"]["upsert_keys"].items():
            with self.subTest(db=db):
                self.assertEqual(cmschema.sheet_columns(self.hub, db)[0]["name"], key)

    def test_coach_views_hide_internal_properties(self):
        coach = [v for v in self.hub["views"] if v["audience"] == "coach"]
        self.assertEqual({v["name"] for v in coach}, {"This Week", "Film Queue", "Add Stats", "Runs"})
        for v in coach:
            for name in v["properties"]:
                with self.subTest(view=v["name"], prop=name):
                    self.assertFalse(cmschema.prop(self.hub, v["database"], name).get("internal"))

    def test_planned_views_exist(self):
        names = {v["name"] for v in self.hub["views"]}
        self.assertLessEqual({"Film Queue", "This Week", "Ideas", "Bank by Type", "Runs"}, names)

    def test_bank_types(self):
        types = self.banks["types"]
        self.assertEqual(set(types), set("VOSBPRKICAWX"))
        for prefix, t in types.items():
            with self.subTest(type=prefix):
                self.assertEqual(t["prefix"], prefix)
                self.assertTrue(any(f["required"] for f in t["fields"]))
        p_fields = {f["name"]: f for f in types["P"]["fields"]}
        for name in ("consent", "consent_date", "allowed_uses", "substantiated", "re_check_by"):
            self.assertTrue(p_fields[name]["required"], name)
        self.assertEqual(p_fields["re_check_by"]["hub"], "Re-check By")
        self.assertEqual(types["P"]["rules"]["re_check_days"], 90)
        self.assertEqual(self.banks["privacy"]["rule"], "role only, never names")
        caps = self.banks["card_caps"]
        self.assertEqual((caps["V"], caps["S"], caps["P"]), (8, 5, 5))

    def test_bank_ids(self):
        ids = self.banks["ids"]
        for ok in ids["examples"]:
            self.assertRegex(ok, ids["pattern"])
        for bad in ids["near_misses"]:
            self.assertIsNone(re.fullmatch(ids["pattern"], bad), bad)
        self.assertIn("highest", ids["next"])
        self.assertTrue(ids["unique"])

    def test_brand_card_visible_part_fits_one_screen(self):
        for ed in cmlib.EDITIONS:
            with self.subTest(edition=ed):
                self.assertLessEqual(cmschema.visible_max(self.card, ed), self.card["budgets"]["visible_chars"][ed])
        self.assertEqual(self.card["budgets"]["whole_chars"], {"en": 5700, "vn": 6600})   # wf13 §4, wf14 §3
        # wf15-simple-surface-spec §0 S3, §4 replaced the 900-character screen with a 3-line top ≤500.
        self.assertEqual(self.card["budgets"]["visible_chars"], {"en": 500, "vn": 500})

    def test_brand_card_visible_top_is_three_lines(self):
        """wf15 S3 + wf14 §1: the title, WHAT YOU SAY (message · 3 topics · keyword), HOW YOU SAY IT (voice).

        Until wf15 the visible part was 6 lines (title, message, big ideas, keyword, offer, week); offer and
        week now live in the machine block, so nothing the machine needs is lost.
        """
        visible = self.card["visible"]
        self.assertEqual(visible["lines"], ["title", "what", "how"])
        by_line = {}
        for f in visible["field"]:
            by_line.setdefault(f["line"], []).append(f["name"])
        self.assertEqual(by_line, {"title": ["title"], "what": ["message", "big_ideas", "keyword"],
                                   "how": ["voice_line"]})
        self.assertEqual(visible["line_label_keys"], {"what": "card.visible.what", "how": "card.visible.how"})
        machine = {f["name"]: f for f in self.card["machine"]["field"]}
        self.assertEqual((machine["offer"]["group"], machine["week"]["group"]), ("map", "plan"))
        for ed in cmlib.EDITIONS:
            self.assertLessEqual(cmschema.visible_max(self.card, ed), 500, ed)

    def test_brand_card_voice_card_fields(self):
        """wf14-voice-language-spec §3: the Voice Card lives in the machine block, group "voice"."""
        machine = {f["name"]: f for f in self.card["machine"]["field"]}
        voice = [f["name"] for f in self.card["machine"]["field"] if f["group"] == "voice"]
        self.assertEqual(voice, ["tone", "rhythm", "phrases", "openers_closers", "audience_address", "pronouns",
                                 "dialect", "code_mix", "humour", "written_vs_spoken", "never_say", "do_say"])
        caps = {"tone": 40, "rhythm": 60, "openers_closers": 50, "audience_address": 40, "dialect": 40,
                "code_mix": 60, "written_vs_spoken": 80}
        for name, cap in caps.items():
            self.assertEqual(machine[name]["max_chars"], {"en": cap, "vn": cap}, name)
        self.assertEqual(machine["openers_closers"]["max_items"], 3)
        self.assertEqual(machine["humour"]["options"], ["none", "dry", "playful", "self-roast"])
        for name in ("tone", "rhythm", "audience_address", "code_mix", "humour"):
            self.assertIs(machine[name]["required"], True, name)
        for name in ("openers_closers", "written_vs_spoken", "never_say", "do_say"):
            self.assertIs(machine[name]["required"], False, name)
        # the audience address is the coach's, kept apart from the machine-coach pair (VN pronouns)
        self.assertEqual((machine["pronouns"]["required"], machine["dialect"]["required"]), (["vn"], ["vn"]))
        self.assertIn("particles", machine["dialect"]["note"])
        self.assertEqual((machine["written_vs_spoken"]["source"], machine["openers_closers"]["source"]),
                         ("posts", "posts"))
        self.assertIn("posts", self.card["sources"])

    def test_brand_card_trims_voice_last(self):
        """wf14 §3: "voice is core": voice fields are trimmed last, phrases first among them."""
        machine = {f["name"]: f for f in self.card["machine"]["field"]}
        order = self.card["budgets"]["trim_order"]
        groups = [machine[n]["group"] for n in order]
        first_voice = groups.index("voice")
        self.assertEqual(order[first_voice], "phrases")
        self.assertTrue(all(g == "voice" for g in groups[first_voice:]), order)
        self.assertNotIn("voice", groups[:first_voice])
        self.assertEqual(order[-1], "never_say")

    def test_brand_card_machine_block_holds_the_ux_fields(self):
        machine = {f["name"]: f for f in self.card["machine"]["field"]}
        for name in ("phrases", "pronouns", "dialect", "trait", "enemy", "principles", "passages", "client_words",
                     "stories", "proof", "plan_start", "talk_day", "tier", "platform", "list_size", "cta_style",
                     "not_now", "progress", "version", "date", "never_say", "do_say",
                     "offer", "week"):     # visible until wf15 (3-line top); the machine block keeps them
            self.assertIn(name, machine)
        self.assertEqual(machine["phrases"]["max_items"], 5)
        self.assertEqual((machine["passages"]["max_items"], machine["passages"]["max_words"]), (5, 60))
        self.assertEqual(machine["not_now"]["max_items"], 7)
        caps = self.banks["card_caps"]
        for name in ("client_words", "stories", "proof"):
            self.assertEqual(machine[name]["max_items"], caps[machine[name]["bank_type"]])
        self.assertEqual(machine["cta_style"]["options"], ["keyword", "quiet"])

    def test_brand_card_labels_are_strings_keys(self):
        for part in ("visible", "machine"):
            for f in self.card[part]["field"]:
                with self.subTest(field=f["name"]):
                    self.assertTrue(cmlib.KEY_RE.match(f["label_key"]))
                    self.assertTrue(f["label_key"].startswith("card."))

    def test_liked_post_bank_type(self):
        """wf13-inspiration-spec §4: the W row is a post or channel the coach likes or follows."""
        w = self.banks["types"]["W"]
        self.assertEqual(w["hub_option"], "Liked post")
        self.assertEqual(w["states"], ["Active", "Retired"])
        self.assertEqual(w["kinds"], ["Post", "Channel"])
        fields = {f["name"]: f for f in w["fields"]}
        self.assertEqual({n for n, f in fields.items() if f["required"]}, {"shape", "kind", "seen", "source"})
        self.assertEqual({n for n, f in fields.items() if not f["required"]},
                         {"about", "why", "hook_type", "relation", "fits", "ratio", "link", "used_in"})
        self.assertEqual((fields["shape"]["hub"], fields["shape"]["max_chars"]), ("Text", 140))
        self.assertEqual(fields["kind"]["hub"], "Kind")
        self.assertEqual(fields["seen"]["options"], ["screenshot", "caption", "transcript", "told", "grid", "page"])
        self.assertEqual(fields["about"]["max_words"], {"en": 12, "vn": 18})
        self.assertNotIn("L1", fields["link"]["levels"])
        never = " ".join(w["rules"]["never_store"])
        for word in ("commenter", "phone", "results"):
            self.assertIn(word, never)
        self.assertIn("W rows only", self.banks["privacy"]["public_source_names"])
        hub_types = cmschema.prop(self.hub, "bank", "Type")["options"]
        self.assertIn("Liked post", hub_types)
        self.assertNotIn("Swipe", hub_types)
        self.assertLessEqual({"Post", "Channel"}, set(cmschema.prop(self.hub, "bank", "Kind")["options"]))

    def test_posts_i_like_view(self):
        view = next(v for v in self.hub["views"] if v["name"] == "Posts I like")
        self.assertEqual((view["database"], view["label_key"]), ("bank", "hub.view.liked"))
        self.assertIn({"property": "Type", "op": "is", "value": "Liked post"}, view["filter"])
        self.assertIn({"property": "State", "op": "is", "value": "Active"}, view["filter"])
        self.assertEqual(view["sort"][0]["property"], "Added")
        for name in view["properties"]:
            self.assertFalse(cmschema.prop(self.hub, "bank", name).get("internal"), name)
        self.assertNotIn("Score", view["properties"])        # no ratio in front of the coach

    def test_brand_card_liked_line(self):
        """wf13-inspiration-spec §4: ≤8 entries, ≤80 EN / 90 VN chars, first in trim_order, never visible."""
        machine = {f["name"]: f for f in self.card["machine"]["field"]}
        liked = machine["liked"]
        self.assertEqual((liked["type"], liked["max_items"]), ("list", 8))
        self.assertEqual(liked["max_chars"], {"en": 80, "vn": 90})
        self.assertFalse(liked["required"])
        self.assertEqual(self.card["budgets"]["trim_order"][0], "liked")
        self.assertNotIn("liked", {f["name"] for f in self.card["visible"]["field"]})
        for ed in cmlib.EDITIONS:
            added = self.card["budgets"]["whole_chars"][ed] - {"en": 5000, "vn": 5800}[ed]
            self.assertGreaterEqual(added, liked["max_items"] * liked["max_chars"][ed], ed)

    def test_brand_card_budgets_match_targets(self):
        targets_path = REPO / "platform" / "targets.toml"
        if not targets_path.exists():
            self.skipTest("platform/targets.toml not present")
        budgets = cmlib.load_toml(targets_path).get("budgets", {})
        for ref, key in (("brand_card", "whole_chars"), ("brand_card_visible", "visible_chars")):
            if ref not in budgets:
                continue
            for ed in cmlib.EDITIONS:
                self.assertEqual(budgets[ref][ed], self.card["budgets"][key][ed], f"{ref}.{ed}")


# ================================================================ keys

class KeysTest(TempRepo):
    def test_examples_match_and_near_misses_do_not(self):
        grammars = cmschema.key_grammars(self.keys)
        self.assertGreaterEqual(len(grammars), 10)
        for kind, spec in grammars:
            for ok in spec["examples"]:
                with self.subTest(kind=kind, key=ok):
                    self.assertIsNotNone(cmschema.match_key(ok, spec))
            for bad in spec.get("near_misses", []):
                with self.subTest(kind=kind, near_miss=bad):
                    self.assertIsNone(re.fullmatch(spec["pattern"], bad))
            for bad in spec.get("invalid", []):
                with self.subTest(kind=kind, invalid=bad):
                    self.assertIsNotNone(re.fullmatch(spec["pattern"], bad))
                    self.assertIsNone(cmschema.match_key(bad, spec))

    def test_kinds(self):
        cases = {
            "2026-W41-N1": ["slot.weekly"],
            "2026-W53-P": ["slot.weekly"],
            "LCH-NOV26-D03-REEL": ["slot.launch"],
            "DROP-2026-10-07": ["slot.drop", "run.DROP"],
            "BATCH-2026-W41": ["run.BATCH"],
            "REVIEW-2026-W41": ["run.REVIEW"],
            "SETUP-2026-10-05": ["run.SETUP"],
            "CUT-2026-W41-P": ["run.CUT"],
            "PLAN-2026-11": ["run.PLAN"],
            "LAUNCH-NOV26": ["run.LAUNCH"],
        }
        for key, kinds in cases.items():
            with self.subTest(key=key):
                self.assertEqual(cmschema.key_kinds(key, self.keys), kinds)
        for bad in ("2027-W53-P", "DROP-2026-02-30", "2026-W41-P\n", "2026-W41-C6", "BATCH-2026-W41-P", ""):
            with self.subTest(bad=bad):
                self.assertEqual(cmschema.key_kinds(bad, self.keys), [])
        self.assertTrue(cmschema.is_slot_key("2026-W41-A1", self.keys))
        self.assertFalse(cmschema.is_run_key("2026-W41-A1", self.keys))
        self.assertTrue(cmschema.is_run_key("DROP-2026-10-07", self.keys))

    def test_weekly_suffixes(self):
        codes = {s["code"] for s in self.keys["slot"]["weekly"]["suffix"]}
        self.assertEqual(codes, WEEKLY_SUFFIXES)
        spec = self.keys["slot"]["weekly"]
        for code in WEEKLY_SUFFIXES:
            self.assertIsNotNone(cmschema.match_key(f"2026-W41-{code}", spec), code)

    def test_slot_formats_are_content_formats(self):
        formats = set(cmschema.prop(self.hub, "content", "Format")["options"])
        for entry in self.keys["slot"]["weekly"]["suffix"] + self.keys["slot"]["launch"]["fmt"]:
            self.assertIn(entry["format"], formats, entry["code"])

    def test_run_states_and_types_match_the_hub(self):
        states = [s["name"] for s in self.keys["run"]["state"]]
        self.assertEqual(states, ["Running", "OK", "Partial", "Failed"])
        self.assertEqual(states, cmschema.prop(self.hub, "runs", "Run State")["options"])
        types = sorted(e["type"] for e in self.keys["run"]["key"])
        self.assertEqual(types, sorted(cmschema.prop(self.hub, "runs", "Type")["options"]))
        self.assertEqual(self.keys["run"]["stale_running_hours"], 2)


# ================================================================ the validator catches faults

class ValidatorFaultsTest(TempRepo):
    def mutated(self, fn) -> list[str]:
        data = copy.deepcopy(self.data)
        fn(data)
        return self.findings(data)

    def assertFlags(self, fn, fragment: str):
        found = self.mutated(fn)
        self.assertTrue(any(fragment in m for m in found), f"no finding containing {fragment!r} in {found}")

    def test_ai_may_set_outside_options(self):
        def fn(d):
            cmschema.prop(d["hub"], "content", "Status")["ai_may_set"] = ["Idea", "Published"]
        self.assertFlags(fn, "subset of options")

    def test_ai_may_set_posted(self):
        def fn(d):
            cmschema.prop(d["hub"], "content", "Status")["ai_may_set"] = ["Idea", "Scripted", "Reviewed", "Posted"]
        self.assertFlags(fn, "ai_status must equal")

    def test_property_without_type(self):
        self.assertFlags(lambda d: cmschema.prop(d["hub"], "content", "Hook").pop("type"), "type must be one of")

    def test_option_with_comma(self):
        self.assertFlags(lambda d: cmschema.prop(d["hub"], "content", "Job")["options"].append("Sell, now"),
                         "comma")

    def test_coach_view_showing_a_score(self):
        def fn(d):
            next(v for v in d["hub"]["views"] if v["name"] == "This Week")["properties"].append("Edge")
        self.assertFlags(fn, "internal property 'Edge'")

    def test_view_filter_on_unknown_option(self):
        def fn(d):
            next(v for v in d["hub"]["views"] if v["name"] == "Film Queue")["filter"][0]["value"] = "Shot"
        self.assertFlags(fn, "not an option")

    def test_relation_to_nowhere(self):
        self.assertFlags(lambda d: cmschema.prop(d["hub"], "runs", "Items").update(relation_to="logs"),
                         "not a database id")

    def test_key_example_that_does_not_match(self):
        self.assertFlags(lambda d: d["keys"]["slot"]["weekly"]["examples"].append("2026-W41-Z"), "does not match")

    def test_near_miss_that_matches(self):
        self.assertFlags(lambda d: d["keys"]["slot"]["weekly"]["near_misses"].append("2026-W41-P"), "matches")

    def test_bank_field_mapped_to_unknown_property(self):
        self.assertFlags(lambda d: d["banks"]["types"]["V"]["fields"].append(
            {"name": "mood", "hub": "Mood", "required": False}), "unknown Bank property 'Mood'")

    def test_bank_kind_missing_from_hub(self):
        self.assertFlags(lambda d: d["banks"]["types"]["V"]["kinds"].append("Hope"), "Kind options")

    def test_visible_card_over_one_screen(self):
        def fn(d):
            d["brand-card"]["visible"]["field"][1]["max_chars"]["vn"] = 400
        self.assertFlags(fn, "over the 500 budget")      # wf15 §4: the visible top is ≤500, was 900

    def test_visible_field_on_unknown_line(self):
        def fn(d):
            d["brand-card"]["visible"]["field"][-1]["line"] = "who"
        self.assertFlags(fn, "line 'who' is not one of")

    def test_visible_line_with_no_field(self):
        self.assertFlags(lambda d: d["brand-card"]["visible"]["lines"].append("offer"), "line 'offer' has no field")

    def test_machine_field_with_a_line(self):
        def fn(d):
            next(f for f in d["brand-card"]["machine"]["field"] if f["name"] == "tone")["line"] = "how"
        self.assertFlags(fn, "line is for visible fields only")

    def test_card_cap_disagrees_with_banks(self):
        def fn(d):
            next(f for f in d["brand-card"]["machine"]["field"] if f["name"] == "client_words")["max_items"] = 9
        self.assertFlags(fn, "card_caps.V")

    def test_framework_word_in_card_field(self):
        def fn(d):
            d["brand-card"]["machine"]["field"][0]["name"] = "pillar_one"
        self.assertFlags(fn, "framework words")

    def test_bank_field_with_bad_options(self):
        def fn(d):
            next(f for f in d["banks"]["types"]["W"]["fields"] if f["name"] == "seen")["options"] = []
        self.assertFlags(fn, "options must be a non-empty list")

    def test_bank_field_with_bad_word_cap(self):
        def fn(d):
            next(f for f in d["banks"]["types"]["W"]["fields"] if f["name"] == "about")["max_words"] = {"en": 12}
        self.assertFlags(fn, "max_words needs positive en and vn")

    def test_liked_post_option_missing_from_hub(self):
        def fn(d):
            opts = cmschema.prop(d["hub"], "bank", "Type")["options"]
            opts[opts.index("Liked post")] = "Swipe"
        self.assertFlags(fn, "Bank Type options")

    def test_whole_card_smaller_than_visible(self):
        # 400 sits under the visible top's 500 (wf15 §4; the old 900 budget made 800 the probe)
        self.assertFlags(lambda d: d["brand-card"]["budgets"]["whole_chars"].update(vn=400), "smaller than visible")

    def test_run_state_drift(self):
        self.assertFlags(lambda d: cmschema.prop(d["hub"], "runs", "Run State")["options"].append("Skipped"),
                         "run states")


class HelpersTest(unittest.TestCase):
    def test_column_letters(self):
        for i, letters in ((0, "A"), (25, "Z"), (26, "AA"), (51, "AZ"), (701, "ZZ"), (702, "AAA")):
            self.assertEqual(cmschema.column_letter(i), letters)

    def test_scoreboard_formula_uses_content_columns(self):
        hub = cmschema.load("hub", REPO)
        cols = [p["name"] for p in cmschema.sheet_columns(hub, "content")]
        views = cmschema.column_letter(cols.index("Views"))
        self.assertEqual(cmschema.scoreboard_formula(hub, "=Content!{Views}{row}+{prev}", 5), f"=Content!{views}5+4")
        with self.assertRaises(CMError):
            cmschema.scoreboard_formula(hub, "=Content!{Hook Stem}{row}", 2)   # not a sheet column


# ================================================================ hub_build_prompt

class HubBuildPromptTest(TempRepo):
    def build(self, editions=("en", "vn")):
        return {r.edition: r for r in hub_build_prompt.build(self.root, list(editions))}

    def read(self, rel: str) -> str:
        return (self.root / "dist" / "maintainer" / rel).read_text(encoding="utf-8")

    def test_prompt_mentions_every_property_and_option(self):
        self.build()
        for ed in cmlib.EDITIONS:
            prompt = self.read(f"notion-build-prompt-{ed}.md")
            for db in cmschema.databases(self.hub):
                for p in cmschema.properties(self.hub, db):
                    with self.subTest(edition=ed, db=db, prop=p["name"]):
                        self.assertIn(f"`{p['name']}`", prompt)
                        for option in p.get("options", []):
                            self.assertIn(f"`{option}`", prompt)
            for v in self.hub["views"]:
                self.assertIn(f"`{v['properties'][0]}`", prompt)

    def test_csv_headers_equal_sheet_columns(self):
        self.build()
        for ed in cmlib.EDITIONS:
            folder = self.root / "dist" / "maintainer" / f"sheets-{ed}"
            for tab, db in cmschema.db_by_tab(self.hub).items():
                with self.subTest(edition=ed, tab=tab):
                    rows = list(csv.reader(io.StringIO((folder / f"{tab}.csv").read_text(encoding="utf-8"))))
                    self.assertEqual(rows, [[p["name"] for p in cmschema.sheet_columns(self.hub, db)]])
            board = list(csv.reader(io.StringIO((folder / "Scoreboard.csv").read_text(encoding="utf-8"))))
            self.assertEqual(board, [[c["name"] for c in self.hub["sheets"]["scoreboard"]]])
            start = list(csv.reader(io.StringIO((folder / "Start.csv").read_text(encoding="utf-8"))))
            self.assertEqual(start[0], ["Step", "Text"])
            self.assertEqual(len(start), 2 + len(self.hub["sheets"]["start"]["step_keys"]))
            self.assertEqual(sorted(p.name for p in folder.iterdir()),
                             sorted([f"{t}.csv" for t in self.hub["sheets"]["tabs"]] + ["BUILD-NOTES.md"]))

    def test_strings_are_used_and_missing_keys_fall_back(self):
        results = self.build()
        en = self.read("notion-build-prompt-en.md")
        vn = self.read("notion-build-prompt-vn.md")
        self.assertIn(EN_STRINGS["hub.content.slot_key"], en)
        self.assertIn('"hub.content.title"', en)                 # no string yet: the key itself
        self.assertIn(VN_STRINGS["hub.content.slot_key"], vn)
        self.assertIn('"Tuần này"', vn)
        self.assertIn('"Ideas"', vn)                             # a label with no string: the English name
        self.assertNotIn("hub.content.slot_key", results["en"].missing)
        self.assertIn("hub.content.title", results["en"].missing)
        start_vn = self.read("sheets-vn/Start.csv")
        self.assertIn("Bắt đầu: Content Machine", start_vn)      # {{name}} rendered from the edition
        self.assertIn("hub.sheets.start.what", start_vn)

    def test_names_stay_english_in_vn(self):
        self.build(["vn"])
        vn = self.read("notion-build-prompt-vn.md")
        self.assertIn("Vietnamese edition", vn)
        for name in ("`Slot Key`", "`Status`", "`Idea`", "`Run State`", "`Brand Brain`"):
            self.assertIn(name, vn)
        self.assertEqual(self.read("sheets-vn/Content.csv").splitlines()[0].split(",")[0], "Slot Key")

    def test_brand_name_comes_from_the_edition(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_repo(Path(tmp), name="Story Engine")
            hub_build_prompt.build(root, ["en"])
            prompt = (root / "dist" / "maintainer" / "notion-build-prompt-en.md").read_text(encoding="utf-8")
        self.assertIn("`Story Engine`", prompt)
        self.assertNotIn("Content Machine", prompt)

    def test_rules_and_views_are_in_the_prompt(self):
        self.build(["en"])
        en = self.read("notion-build-prompt-en.md")
        self.assertIn("Never delete", en)
        self.assertIn("at most 30 board calls", en)
        self.assertIn("same upsert", en)
        self.assertIn("the machine may set only `Idea`, `Scripted`, `Reviewed`", en)
        for view in ("This Week", "Film Queue", "Ideas", "Bank by Type", "Runs"):
            self.assertIn(f'"{view}"', en)
        self.assertIn("`Content` `Series` ↔ `Series` `Content`", en)

    def test_no_wording_lint_rejects(self):
        self.build()
        texts = [p.read_text(encoding="utf-8") for p in (self.root / "dist" / "maintainer").rglob("*") if p.is_file()]
        for text in texts:
            for phrase in BANNED_IN_DIST:
                self.assertNotIn(phrase.lower(), text.lower())

    def test_deterministic_and_stale_files_removed(self):
        self.build()
        out = self.root / "dist" / "maintainer"
        first = {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()}
        (out / "sheets-en" / "Old.csv").write_text("stale\n", encoding="utf-8")
        self.build()
        second = {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()}
        self.assertEqual(first, second)
        for rel, data in first.items():
            text = data.decode("utf-8")
            self.assertEqual(text, cmlib.nfc(text), rel)
            self.assertTrue(text.endswith("\n") and not text.endswith("\n\n"), rel)
            self.assertTrue(str(rel).isascii(), rel)

    def test_cli_all(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = hub_build_prompt.main(["--edition", "all", "--root", str(self.root)])
        self.assertEqual(code, 0)
        for ed in cmlib.EDITIONS:
            self.assertTrue((self.root / "dist" / "maintainer" / f"notion-build-prompt-{ed}.md").is_file())
            self.assertTrue((self.root / "dist" / "maintainer" / f"sheets-{ed}" / "Content.csv").is_file())
        self.assertIn("not in strings/en.toml yet", buf.getvalue())

    def test_missing_hub_schema_is_skipped(self):
        (self.root / "schemas" / "hub.toml").unlink()
        self.assertEqual(hub_build_prompt.build(self.root, ["en"]), [])
        self.assertFalse((self.root / "dist").exists())

    def test_invalid_schema_stops_the_build(self):
        path = self.root / "schemas" / "hub.toml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            'ai_may_set = ["Idea", "Scripted", "Reviewed"]', 'ai_may_set = ["Idea", "Scripted", "Posted"]'),
            encoding="utf-8")
        with self.assertRaises(CMError) as ctx:
            hub_build_prompt.build(self.root, ["en"])
        self.assertEqual(ctx.exception.code, "E161")
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            self.assertEqual(hub_build_prompt.main(["--edition", "en", "--root", str(self.root)]), 1)
        self.assertIn("E161", buf.getvalue())

    def test_works_without_strings_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_repo(Path(tmp), strings=False)
            results = hub_build_prompt.build(root, ["en", "vn"])
            self.assertTrue(all(r.missing for r in results))
            prompt = (root / "dist" / "maintainer" / "notion-build-prompt-en.md").read_text(encoding="utf-8")
        self.assertIn('"hub.content.slot_key"', prompt)


if __name__ == "__main__":
    unittest.main()
