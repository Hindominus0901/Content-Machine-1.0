"""Must-fail fixtures for tools/lint.py (gate G1): every defect must be caught.

Each test builds a small valid repo in a temp folder (and, where a check reads
built output, a small valid dist/), injects one defect and asserts the lint code.
Two tests prove the untouched repo is clean in dev and release mode, so each
code below is caused by its defect alone.

Choices docs/BUILD.md leaves open (see also the lint.py docstring):
  * 191-character description: tested both as strings key "skill.description"
    (source) and as SKILL.md front matter in a built skill zip. Both are E102.
  * NFD Vietnamese string: E111. src hashes and budgets are defined on NFC text,
    so a value that is not NFC counts as stale.
  * Non-deterministic zip: an entry stamped with a build-time timestamp, and a
    zip whose bytes differ from what package.make_zip rebuilds (another
    compression level). Both are E152.
"""
from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
import tempfile
import unicodedata
import unittest
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import lint  # noqa: E402
import package  # noqa: E402
from cmlib import sha10  # noqa: E402
from cmschema import SCHEMAS  # noqa: E402

TODAY = dt.date(2026, 10, 5)
DOS_EPOCH = (1980, 1, 1, 0, 0, 0)
SKILL_ZIP = "dist/en/Level-ups/autopilot/content-machine.zip"

EN_STRINGS = {
    "contract.output": "Always reply in English. One screen per reply, then one NEXT line.",
    "verdict.ready": "Ready to {verb} · I'd post it: {evidence}",
    "skill.description": "Writes a coach's week of content from their own words and checks it before handing it over.",
    "anchor.talk": "Weekly Talk",
}
VN_STRINGS = {
    "contract.output": "Luôn trả lời bằng tiếng Việt. Mỗi lần một màn hình, rồi một dòng TIẾP.",
    "verdict.ready": "Sẵn sàng {verb} · Mình sẽ đăng: {evidence}",
    "skill.description": "Viết nội dung cả tuần cho coach từ chính lời của họ và kiểm tra trước khi giao.",
    "anchor.talk": "Buổi nói chuyện tuần",
}

# prose[lang][file] = [[section id, attributes, body], ...]
EN_PROSE = {
    "core/en/start-block.md": [
        ["start.core", "", "{{t:contract.output}}\n### Start\nYou are {{name}}. The Weekly Talk lives in §CM-TALK.\n"
                           "SHIP CHECK · silent · once per batch\n{{t:contract.output}}"],
    ],
    "modules/en/talk.md": [
        ["talk.core", "", "### Weekly Talk\nAsk five questions. Log each piece with `hub:Status`."],
        ["talk.script", "kind=script", "### Script\nWrite the script, then print {{t:verdict.ready}}."],
    ],
}
VN_PROSE = {
    "core/vn/start-block.md": [
        ["start.core", "", "{{t:contract.output}}\n### Bắt đầu\nBạn là {{name}}. Buổi nói chuyện tuần ở §CM-TALK.\n"
                           "SHIP CHECK · im lặng · mỗi lô một lần\n{{t:contract.output}}"],
    ],
    "modules/vn/talk.md": [
        ["talk.core", "", "### Buổi nói chuyện tuần\nHỏi năm câu. Ghi mỗi bài bằng `hub:Status`."],
        ["talk.script", "kind=script", "### Kịch bản\nViết kịch bản, rồi in {{t:verdict.ready}}."],
    ],
}

BASE_FILES = {
    "editions/en.toml": """\
[edition]
id = "en"
lang = "en"
name = "Content Machine"
skill_name = "content-machine"
file_suffix = "EN"
zip_name = "Content-Machine-EN"

[params]
currency = "$"
""",
    "editions/vn.toml": """\
[edition]
id = "vn"
lang = "vn"
name = "Content Machine"
skill_name = "content-machine-vn"
file_suffix = "VN"
zip_name = "Content-Machine-VN"

[params]
currency = "đ"

[pending]
platform_priority = { default = "Facebook + Zalo", reason = "fixture" }
""",
    "editions/vn.acceptance.toml": """\
[accepted.platform_priority]
default = "Facebook + Zalo"
signed_by = "founder"
date = "2026-09-30"
""",
    "platform/targets.toml": """\
[meta]
schema = 1
max_age_days = 90

[limits.chatgpt_free_project_files]
value = 5
unit = "files"
evidence = "DATA"
verified_on = "2026-10-01"
source = "fixture"

[budgets.skill_description]
artifact = "SKILL.md description"
unit = "chars_nfc"
en = 190
vn = 190
limit = ""

[budgets.reference_lines]
artifact = "each skill reference file"
unit = "lines"
en = 150
vn = 150
limit = ""

[budgets.references_per_job]
artifact = "router: files loaded per job"
unit = "files"
en = 4
vn = 4
limit = ""
""",
    "core/method.toml": """\
[method]
[[method.anchor]]
id = "TALK"
sections = ["talk.*"]

[skill]
[[skill.reference]]
file = "talk.md"
sections = ["talk.*"]
module = "talk"
formats = ["short"]
""",
    "core/router.toml": """\
[[route]]
id = "weekly-talk"
module = "talk"
trigger = "The coach says next on talk day."
trigger_vn = "Coach nhắn tiếp vào ngày nói chuyện."
rules = ["Ask one question at a time."]
rules_vn = ["Hỏi từng câu một."]
loads = ["talk.md"]
writes = ["Content"]
phrases.en = ["next"]
phrases.vn = ["tiếp"]
""",
    "core/format-checks.toml": """\
[format.short]
checks = ["Does the first line make the claim?"]
checks_vn = ["Câu đầu đã nói thẳng ý chính chưa?"]
""",
    "locales/en/deny-list.txt": "# fixture list\nShip Check\nre:\\bB[1-7]\\b\n",
    "locales/en/banned-tells.txt": "delve\nlet's dive in\n",
    "locales/vn/deny-list.txt": "Ship Check\ntrụ cột\n",
    "locales/vn/banned-tells.txt": "hãy cùng khám phá\nnâng tầm\n",
    "locales/en/examples.md": "Film it today: one idea, one story, one ask.\n",
    "locales/vn/examples.md": "Quay ngay hôm nay: một ý, một câu chuyện, một lời mời.\n",
    "locales/en/market.md": "Coaches here sell through LinkedIn and email.\n",
    "locales/vn/market.md": "Coach ở đây bán qua Facebook và Zalo.\n",
    "locales/en/platform-notes.md": "Checked 2026-10-05: ChatGPT Free allows 5 project files.\n",
    "locales/vn/platform-notes.md": "Kiểm tra ngày 5/10/2026: ChatGPT Free cho 5 file mỗi dự án.\n",
}


def sentence(n: int) -> str:
    """Realistic text of exactly n characters, ending in a full stop (nothing to strip)."""
    text = ("Writes a coach's week of content from their own words and checks it. " * 4)[: n - 1].rstrip()
    return text + "." * (n - len(text))


def toml_str(text: str) -> str:
    return json.dumps(text, ensure_ascii=False)  # JSON escapes are valid TOML basic-string escapes


def write_zip(path: Path, entries: dict[str, bytes], date_time=DOS_EPOCH, compresslevel: int = 9) -> None:
    """A zip written the way package.make_zip writes one, with knobs to break it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as zf:
        for name in sorted(entries):
            info = zipfile.ZipInfo(name, date_time=date_time)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            zf.writestr(info, entries[name], compresslevel=compresslevel)


def zip_entries(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path) as zf:
        return {name: zf.read(name) for name in zf.namelist()}


class Repo:
    """A minimal valid source tree (and, on request, a valid dist/) in a temp folder."""

    def __init__(self, root: Path):
        self.root = root
        self.strings = {"en": dict(EN_STRINGS), "vn": dict(VN_STRINGS)}
        self.src_override: dict[str, str] = {}
        self.prose = {"en": json.loads(json.dumps(EN_PROSE)), "vn": json.loads(json.dumps(VN_PROSE))}
        self.section_src_override: dict[str, str] = {}
        for rel, text in BASE_FILES.items():
            self.write(rel, text)
        for name in SCHEMAS:  # the real schema set (cmschema checks the four together; E160 reads hub.toml)
            self.write(f"schemas/{name}.toml", (REPO / "schemas" / f"{name}.toml").read_text(encoding="utf-8"))
        self.write_strings()
        self.write_prose()

    # -- sources

    def write(self, rel: str, text: str) -> Path:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")

    def write_strings(self) -> None:
        en = self.strings["en"]
        lines = ["[strings]"] + [f"{toml_str(k)} = {toml_str(v)}" for k, v in en.items()]
        self.write("strings/en.toml", "\n".join(lines) + "\n")
        lines = ["[strings]"]
        for key, text in self.strings["vn"].items():
            src = self.src_override.get(key, sha10(en.get(key, "")))
            lines.append(f'{toml_str(key)} = {{ text = {toml_str(text)}, src = "{src}" }}')
        self.write("strings/vn.toml", "\n".join(lines) + "\n")

    def set_string(self, lang: str, key: str, text: str) -> None:
        self.strings[lang][key] = text
        self.write_strings()

    def en_body(self, section_id: str) -> str:
        for secs in self.prose["en"].values():
            for sid, _, body in secs:
                if sid == section_id:
                    return body
        return ""

    def write_prose(self) -> None:
        for lang, files in self.prose.items():
            for rel, secs in files.items():
                out = ["<!-- maintainer notes: the preamble does not ship -->"]
                for sid, attrs, body in secs:
                    extra = f" {attrs}" if attrs else ""
                    if lang != "en":
                        extra += f" src={self.section_src_override.get(sid, sha10(self.en_body(sid)))}"
                    out.append(f"<!-- @section {sid}{extra} -->\n{body}\n")
                self.write(rel, "\n".join(out))

    def set_section(self, lang: str, rel: str, section_id: str, body: str) -> None:
        for sec in self.prose[lang][rel]:
            if sec[0] == section_id:
                sec[2] = body
        self.write_prose()

    def set_both(self, rel_en: str, section_id: str, en_body: str, vn_body: str) -> None:
        """Change a section in EN and its VN twin (src kept in step)."""
        self.set_section("en", rel_en, section_id, en_body)
        self.set_section("vn", rel_en.replace("/en/", "/vn/"), section_id, vn_body)

    # -- built output

    def build_dist(self, *, description: str | None = None, ref_lines: int | None = None,
                   skill_files: dict[str, str] | None = None, instructions: str | None = None,
                   skill_md: str | None = None) -> None:
        """A dist/ that passes every dist check; keyword arguments break one thing."""
        dist = self.root / "dist"
        for ed, suffix, name in (("en", "EN", "content-machine"), ("vn", "VN", "content-machine-vn")):
            contract = self.strings[ed]["contract.output"]
            out = dist / ed
            text = instructions if (instructions is not None and ed == "en") else (
                f"{contract}\n\nSHIP CHECK · silent · once per batch\nWeekly Talk: §CM-TALK.\n\n{contract}\n")
            self.write(f"dist/{ed}/1-INSTRUCTIONS.txt", text)
            self.write(f"dist/{ed}/CONTENT-MACHINE-{suffix}.md", f"# Content Machine\n\n{contract}\n\n"
                       f"## §CM-TALK · Weekly Talk\n\nAsk five questions.\n\n{contract}\n")
            desc = description if (description is not None and ed == "en") else self.strings[ed]["skill.description"]
            body = "Ask five questions.\n"
            if ref_lines is not None and ed == "en":
                body = "".join(f"Step {i}.\n" for i in range(ref_lines - 8))  # 8 wrapper lines
            files = {
                "SKILL.md": skill_md if (skill_md is not None and ed == "en") else (
                    f"---\nname: {name}\ndescription: {desc}\n---\n"
                    "# Content Machine\n\nSHIP CHECK · silent · once per batch\n"),
                "references/talk.md": (f"{contract}\n\nWHEN TO USE: The coach says next.\n\n{body}\n"
                                       f"CHECK BEFORE ANSWERING:\n- Does the first line make the claim?\n{contract}\n"),
            }
            if ed == "en":
                files.update(skill_files or {})
            stage = self.root / "stage" / ed / name
            for rel, content in files.items():
                path = stage / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            package.make_zip(stage, out / "Level-ups" / "autopilot" / f"{name}.zip", prefix=name)
            package.make_zip(out, dist / f"Content-Machine-{suffix}-v1.0.0.zip")
        self.write("dist/maintainer/manifest.json", json.dumps({"schema": 1, "skipped": []}))

    @property
    def skill_zip(self) -> Path:
        return self.root / "dist" / "en" / "Level-ups" / "autopilot" / "content-machine.zip"

    def lint(self, release: bool = False) -> lint.Report:
        return lint.run_lint(self.root, release=release, today=TODAY)


class LintCase(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Repo(Path(self._tmp.name))

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def dump(self, report: lint.Report) -> str:
        return "\n".join(map(str, report.findings)) or "(no findings)"

    def assertCatches(self, code: str, release: bool = False, where: str | None = None) -> lint.Report:
        report = self.repo.lint(release=release)
        hits = [f for f in report.errors if f.code == code]
        self.assertTrue(hits, f"{code} not reported; findings:\n{self.dump(report)}")
        if where is not None:
            self.assertTrue(any(f.path.startswith(where) for f in hits),
                            f"{code} not reported at {where}; findings:\n{self.dump(report)}")
        return report

    def assertClean(self, report: lint.Report, code: str | None = None) -> None:
        bad = [f for f in report.errors if code is None or f.code == code]
        self.assertFalse(bad, self.dump(report))


class ValidRepo(LintCase):
    def test_valid_repo_has_no_errors(self):
        report = self.repo.lint()
        self.assertClean(report)
        self.assertTrue(any("dist/ not found" in n for n in report.notes), report.notes)

    def test_valid_repo_with_dist_passes_release(self):
        self.repo.build_dist()
        self.assertClean(self.repo.lint(release=True))


class MustFailFixtures(LintCase):
    """The P1 fixture list (PLAN.md P1, arch-final-spec Phase 1, QA spec §10). All must fail."""

    def test_E102_191_char_description_in_strings(self):
        self.repo.set_string("en", "skill.description", sentence(191))
        report = self.assertCatches("E102", where="strings/en.toml")
        self.assertTrue(any("191 characters" in f.message for f in report.errors), self.dump(report))

    def test_E102_191_char_description_in_skill_md(self):
        self.repo.build_dist(description=sentence(191))
        self.assertCatches("E102", where=f"{SKILL_ZIP}!content-machine/SKILL.md")

    def test_E111_vn_string_in_nfd(self):
        self.repo.set_string("vn", "verdict.ready", unicodedata.normalize("NFD", VN_STRINGS["verdict.ready"]))
        report = self.assertCatches("E111", where="strings/vn.toml")
        self.assertTrue(any("not NFC" in f.message for f in report.errors), self.dump(report))

    def test_E130_missing_router_anchor(self):
        self.repo.set_both("core/en/start-block.md", "start.core",
                           "### Start\nYou are {{name}}.\n{{t:contract.output}}",
                           "### Bắt đầu\nBạn là {{name}}.\n{{t:contract.output}}")
        self.assertCatches("E130", where="core/en/start-block.md")

    def test_E111_stale_string_hash(self):
        self.repo.src_override["verdict.ready"] = sha10("Ready to {verb}: {evidence}")
        self.repo.write_strings()
        report = self.assertCatches("E111", where="strings/vn.toml")
        self.assertTrue(any("stale" in f.message for f in report.errors), self.dump(report))

    def test_E120_unaccepted_pending_key_on_release(self):
        self.repo.build_dist()
        self.repo.write("editions/vn.acceptance.toml", "# nothing signed yet\n")
        self.assertClean(self.repo.lint(), "E120")  # dev mode only notes it
        self.assertCatches("E120", release=True, where="editions/vn.acceptance.toml")

    def test_E121_verified_on_older_than_90_days_on_release(self):
        self.repo.build_dist()
        targets = self.repo.read("platform/targets.toml").replace('"2026-10-01"', '"2026-06-01"')
        self.repo.write("platform/targets.toml", targets)
        dev = self.repo.lint()
        self.assertClean(dev, "E121")
        self.assertIn("W204", dev.codes("warning"))
        self.assertCatches("E121", release=True, where="platform/targets.toml")

    def test_E151_dotfile_in_zip(self):
        self.repo.build_dist()
        entries = zip_entries(self.repo.skill_zip)
        entries["content-machine/.DS_Store"] = b"\0"
        write_zip(self.repo.skill_zip, entries)
        self.assertCatches("E151", where=SKILL_ZIP)

    def test_E150_non_ascii_file_name(self):
        self.repo.build_dist()
        self.repo.write("dist/en/Help/hướng-dẫn.html", "<p>Help</p>\n")
        self.assertCatches("E150", where="dist/en/Help/")

    def test_E103_151_line_reference(self):
        self.repo.build_dist(ref_lines=151)
        report = self.assertCatches("E103", where=f"{SKILL_ZIP}!content-machine/references/talk.md")
        self.assertTrue(any("151 lines" in f.message for f in report.errors), self.dump(report))

    def test_E103_route_loading_5_files(self):
        router = self.repo.read("core/router.toml").replace(
            'loads = ["talk.md"]', 'loads = ["talk.md", "plan.md", "ideas.md", "review.md", "hub.md"]')
        self.repo.write("core/router.toml", router)
        self.assertCatches("E103", where="core/router.toml")

    def test_E160_unknown_hub_property(self):
        self.repo.set_both("modules/en/talk.md", "talk.core",
                           "### Weekly Talk\nLog each piece with `hub:Stauts`.",
                           "### Buổi nói chuyện tuần\nGhi mỗi bài bằng `hub:Status`.")
        self.assertCatches("E160", where="modules/en/talk.md")

    def test_E146_script_section_without_verdict_line(self):
        self.repo.set_both("modules/en/talk.md", "talk.script",
                           "### Script\nWrite the script.", "### Kịch bản\nViết kịch bản.")
        self.assertCatches("E146", where="modules/en/talk.md")

    def test_E143_fill_in_in_strings(self):
        self.repo.set_string("en", "help.form", "Fill in the form below and send it back.")
        self.repo.set_string("vn", "help.form", "Nói cho mình ba dòng, mình viết giúp bạn.")
        self.assertCatches("E143", where="strings/en.toml")

    def test_E141_hay_cung_kham_pha_in_vn_examples(self):
        self.repo.write("locales/vn/examples.md", "Hãy cùng khám phá cách quay video đầu tiên.\n")
        self.assertCatches("E141", where="locales/vn/examples.md")

    def test_E142_content_waterfall_in_module(self):
        self.repo.set_both("modules/en/talk.md", "talk.core",
                           "### Weekly Talk\nTurn the talk into a Content Waterfall.",
                           "### Buổi nói chuyện tuần\nBiến buổi nói chuyện thành nhiều bài.")
        self.assertCatches("E142", where="modules/en/talk.md")

    def test_E145_date_in_market_md(self):
        self.repo.write("locales/en/market.md", "In March 2026 most coaches here sold through LinkedIn.\n")
        self.assertCatches("E145", where="locales/en/market.md")

    def test_E152_zip_entry_with_build_time_timestamp(self):
        self.repo.build_dist()
        write_zip(self.repo.skill_zip, zip_entries(self.repo.skill_zip), date_time=(2026, 10, 5, 9, 30, 0))
        report = self.assertCatches("E152", where=SKILL_ZIP)
        self.assertTrue(any("timestamp" in f.message for f in report.errors), self.dump(report))

    def test_E152_zip_that_rebuilds_to_a_different_sha256(self):
        self.repo.build_dist()
        write_zip(self.repo.skill_zip, zip_entries(self.repo.skill_zip), compresslevel=1)
        report = self.assertCatches("E152", where=SKILL_ZIP)
        self.assertTrue(any("different sha256" in f.message for f in report.errors), self.dump(report))

    def test_E153_qa_folder_in_zip(self):
        self.repo.build_dist(skill_files={"qa/verdict.md": "Result: PASS\n"})
        self.assertCatches("E153", where=SKILL_ZIP)

    def test_E144_email_in_module(self):
        self.repo.set_both("modules/en/talk.md", "talk.core",
                           "### Weekly Talk\nSend questions to dana.coach@gmail.com.",
                           "### Buổi nói chuyện tuần\nHỏi năm câu.")
        self.assertCatches("E144", where="modules/en/talk.md")

    def test_E113_vn_section_stale(self):
        self.repo.section_src_override["talk.core"] = sha10(self.repo.en_body("talk.core"))
        self.repo.set_section("en", "modules/en/talk.md", "talk.core",
                              "### Weekly Talk\nAsk six questions. Log each piece with `hub:Status`.")
        report = self.assertCatches("E113", where="modules/vn/talk.md")
        self.assertTrue(any("stale" in f.message for f in report.errors), self.dump(report))

    def test_E114_duplicate_section_id(self):
        self.repo.prose["en"]["modules/en/week.md"] = [["talk.core", "", "### Again\nA second talk.core."]]
        self.repo.write_prose()
        self.assertCatches("E114", where="modules/en/week.md")


class MoreCodes(LintCase):
    """Codes outside the P1 fixture list, plus waivers, the allowlist and the CLI."""

    def test_E110_vn_string_missing(self):
        del self.repo.strings["vn"]["verdict.ready"]
        self.repo.write_strings()
        self.assertCatches("E110", where="strings/vn.toml")

    def test_E112_placeholders_differ(self):
        self.repo.set_string("vn", "verdict.ready", "Sẵn sàng {verb} · Mình sẽ đăng: {proof}")
        self.assertCatches("E112", where="strings/vn.toml")

    def test_E122_verify_limit_with_a_date(self):
        targets = self.repo.read("platform/targets.toml").replace('evidence = "DATA"', 'evidence = "VERIFY"')
        self.repo.write("platform/targets.toml", targets)
        self.assertCatches("E122", where="platform/targets.toml")

    def test_E101_instruction_block_over_budget(self):
        self.repo.build_dist()
        self.repo.write("platform/targets.toml", self.repo.read("platform/targets.toml") + """
[budgets.instructions_block]
artifact = "1-INSTRUCTIONS.txt"
unit = "chars_nfc"
en = 40
vn = 6500
limit = ""
""")
        self.assertCatches("E101", where="dist/en/1-INSTRUCTIONS.txt")

    def test_W201_description_above_90_percent(self):
        self.repo.set_string("en", "skill.description", sentence(180))
        report = self.repo.lint()
        self.assertClean(report, "E102")
        self.assertIn("W201", report.codes("warning"))

    def test_E131_contract_missing_at_the_bottom(self):
        contract = EN_STRINGS["contract.output"]
        rules = "".join(f"Rule {i}: one question per reply.\n" for i in range(1, 13))
        self.repo.build_dist(instructions=f"{contract}\n\nSHIP CHECK · silent\n{rules}Weekly Talk: §CM-TALK.\n")
        report = self.assertCatches("E131", where="dist/en/1-INSTRUCTIONS.txt")
        self.assertTrue(any("bottom" in f.message for f in report.errors), self.dump(report))

    def test_E132_card_missing_from_skill_md(self):
        self.repo.build_dist(skill_md="---\nname: content-machine\ndescription: Writes content.\n---\n# Hi\n")
        self.assertCatches("E132", where=f"{SKILL_ZIP}!content-machine/SKILL.md")

    def test_E140_jargon_in_coach_strings(self):
        self.repo.set_string("en", "verdict.ready", "Ready to {verb} · passed the Ship Check: {evidence}")
        self.repo.set_string("vn", "verdict.ready", "Sẵn sàng {verb} · Mình sẽ đăng: {evidence}")
        self.assertCatches("E140", where="strings/en.toml")

    def test_E110_vn_reference_would_fall_back_to_en_router_text(self):
        router = self.repo.read("core/router.toml").replace('trigger_vn = "Coach nhắn tiếp vào ngày nói chuyện."\n', "")
        self.repo.write("core/router.toml", router)
        report = self.assertCatches("E110", where="core/router.toml")
        self.assertTrue(any("trigger_vn" in f.message for f in report.errors), self.dump(report))

    def test_E110_vn_reference_would_fall_back_to_en_format_checks(self):
        checks = self.repo.read("core/format-checks.toml").split("checks_vn")[0]
        self.repo.write("core/format-checks.toml", checks)
        report = self.assertCatches("E110", where="core/format-checks.toml")
        self.assertTrue(any("checks_vn" in f.message for f in report.errors), self.dump(report))

    def test_E170_anchor_without_a_title_string(self):
        del self.repo.strings["vn"]["anchor.talk"]
        del self.repo.strings["en"]["anchor.talk"]
        self.repo.write_strings()
        report = self.assertCatches("E170", where="core/method.toml")
        self.assertTrue(any("anchor.talk" in f.message for f in report.errors), self.dump(report))

    def test_E161_schema_missing_a_required_key(self):
        hub = self.repo.read("schemas/hub.toml").replace("max_hub_calls_per_run", "max_calls_per_run", 1)
        self.repo.write("schemas/hub.toml", hub)
        report = self.assertCatches("E161", where="schemas/hub.toml")
        self.assertTrue(any("max_hub_calls_per_run" in f.message for f in report.errors), self.dump(report))

    def test_E161_schema_file_missing(self):
        (self.repo.root / "schemas" / "keys.toml").unlink()
        self.assertCatches("E161", where="schemas/keys.toml")

    def test_E161_bad_toml(self):
        self.repo.write("core/format-checks.toml", "[format.short\nchecks = [\n")
        self.assertCatches("E161", where="core/format-checks.toml")

    def test_E170_unknown_string_key_in_prose(self):
        self.repo.set_both("modules/en/talk.md", "talk.script",
                           "### Script\nPrint {{t:verdict.redy}}.", "### Kịch bản\nIn {{t:verdict.ready}}.")
        self.assertCatches("E170", where="modules/en/talk.md")

    def test_waiver_covers_the_source_line_and_its_rendered_copy(self):
        rule = "### Weekly Talk\nNever ask the coach to fill in a form. <!-- lint-ok:E143 -->"
        self.repo.set_both("modules/en/talk.md", "talk.core", rule, "### Buổi nói chuyện tuần\nHỏi năm câu.")
        self.repo.build_dist()
        method = self.repo.root / "dist" / "en" / "CONTENT-MACHINE-EN.md"
        method.write_text(method.read_text(encoding="utf-8") + "Never ask the coach to fill in a form.\n",
                          encoding="utf-8")
        self.assertClean(self.repo.lint(), "E143")
        # without the waiver the source line is reported once; its rendered copy is not reported again
        self.repo.set_both("modules/en/talk.md", "talk.core", rule.replace(" <!-- lint-ok:E143 -->", ""),
                           "### Buổi nói chuyện tuần\nHỏi năm câu.")
        report = self.assertCatches("E143", where="modules/en/talk.md")
        self.assertFalse([f for f in report.errors if f.code == "E143" and f.path.startswith("dist/")],
                         self.dump(report))

    def test_allowlist_and_example_domains_pass_E144(self):
        self.repo.write("tools/lint_allow.toml", '[E144]\nallow = ["hello@contentmachine.vn"]\n')
        self.repo.set_both("modules/en/talk.md", "talk.core",
                           "### Weekly Talk\nWrite to hello@contentmachine.vn or you@example.com.",
                           "### Buổi nói chuyện tuần\nHỏi năm câu.")
        self.assertClean(self.repo.lint(), "E144")

    def test_vn_phone_number_and_handle_are_E144(self):
        for text in ("Gọi 0912 345 678 nhé.", "Nhắn +84 912 345 678.", "Theo dõi @chi.hanh.coach nha."):
            with self.subTest(text=text):
                self.repo.write("locales/vn/examples.md", text + "\n")
                self.assertCatches("E144", where="locales/vn/examples.md")

    def test_runtime_slot_after_as_of_is_not_a_date(self):
        self.repo.write("locales/en/market.md", "Prices as of {date} come from the coach.\n")
        self.assertClean(self.repo.lint(), "E145")

    def test_cli_exit_status_and_json(self):
        cmd = [sys.executable, str(TOOLS / "lint.py"), "--root", str(self.repo.root), "--today", TODAY.isoformat()]
        ok = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertIn("lint (dev): 0 errors", ok.stdout)
        self.repo.set_both("modules/en/talk.md", "talk.core", "### Weekly Talk\nUse the Content GPS.",
                           "### Buổi nói chuyện tuần\nHỏi năm câu.")
        bad = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(bad.returncode, 1, bad.stdout + bad.stderr)
        self.assertRegex(bad.stdout, r"(?m)^E142 modules/en/talk\.md:\d+: Matt Gray framework name 'Content GPS'$")
        js = subprocess.run(cmd + ["--json"], capture_output=True, text=True, encoding="utf-8")
        findings = json.loads(js.stdout)
        self.assertIn({"code", "path", "message", "level"}, [set(f) for f in findings])
        self.assertTrue(any(f["code"] == "E142" and f["level"] == "error" for f in findings))


class RealBuild(LintCase):
    """build.py + package.py output for the valid repo must pass lint (interface check)."""

    def test_built_and_packaged_valid_repo_has_no_errors(self):
        try:
            import build
        except ImportError as exc:  # pragma: no cover - build.py is a sibling P1 tool
            self.skipTest(f"tools/build.py not importable: {exc}")
        self.repo.write("VERSION", "1.0.0\n")
        self.repo.write("core/SKILL.md.tmpl", "---\nname: {{skill_name}}\ndescription: {{t:skill.description}}\n"
                                              "---\n# {{name}}\n\nSHIP CHECK · silent · once per batch\n")
        build.build(self.repo.root, ["en", "vn"])
        for ed in ("en", "vn"):
            package.package_edition(self.repo.root, ed, "1.0.0")
        report = self.repo.lint()
        self.assertClean(report)
        self.assertTrue(list((self.repo.root / "dist").rglob("*.zip")))


class ShippedWordLists(unittest.TestCase):
    """The real locales/*/deny-list.txt and banned-tells.txt parse (no bad regex)."""

    def test_lists_parse(self):
        root = TOOLS.parent
        linter = lint.Linter(root)
        for path in sorted((root / "locales").glob("*/*.txt")):
            if path.name not in lint.LIST_FILES:
                continue
            with self.subTest(path=path.name, lang=path.parent.name):
                terms = linter.parse_terms(path)
                self.assertTrue(terms)
        self.assertFalse([f for f in linter.findings if f.code == "E161"], linter.findings)


if __name__ == "__main__":
    unittest.main()
