"""Tests for render.py, build.py, package.py and ics.py on a tiny temporary repo."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import csv
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
import tomllib
import unittest
import unittest.mock
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import build  # noqa: E402
import cmlib  # noqa: E402
import ics  # noqa: E402
import package  # noqa: E402
import render  # noqa: E402
from cmlib import CMError  # noqa: E402

EN_STRINGS = {
    "contract.output": "Always reply in English. One screen per reply.",
    "method.title": "{{name}} · Method",
    "anchor.talk": "Weekly Talk",
    "starthere.title": "Start here: {{name}}",
    "starthere.body": "Set up {{name}} in 4 steps.",
    "ics.talk.summary": "Weekly Talk · {{name}}",
    "ics.talk.description": 'Open {{name}} and say "next".',
    "ics.friday.summary": "Friday numbers · {{name}}",
    "ics.friday.description": 'Open {{name}} and say "my numbers".',
}
VN_TEXT = {
    "contract.output": "Luôn trả lời bằng tiếng Việt.",
    "method.title": "{{name}} · Phương pháp",
    "anchor.talk": "Buổi nói chuyện tuần",
    "starthere.title": "Bắt đầu từ đây: {{name}}",
    "starthere.body": "Cài {{name}} trong 4 bước.",
    "ics.talk.summary": "Buổi nói chuyện tuần · {{name}}",
    "ics.talk.description": 'Mở {{name}} và gõ "tiếp".',
    "ics.friday.summary": "Số liệu thứ Sáu · {{name}}",
    "ics.friday.description": 'Mở {{name}} và gõ "số liệu tuần này".',
}

EN_TALK = {
    "talk.core": "### Weekly Talk\nAsk five questions in {{currency}} terms.{{#if vn}} VN only.{{/if}}",
    "talk.mini": "### Mini-talk\nThree questions when the week is busy.",
    "setup.start": "### Setup\nSay {{t:contract.output}}",
}
VN_TALK = {
    "talk.core": "### Buổi nói chuyện\nHỏi năm câu theo {{currency}}.{{#if vn}} Chỉ VN.{{/if}}",
    "talk.mini": "### Buổi ngắn\nBa câu khi tuần bận.",
    "setup.start": "### Cài đặt\nNói {{t:contract.output}}",
}

SHIPLINT = '''\
#!/usr/bin/env python3
"""Runtime lint stub."""
import sys

try:
    from cmcore.checks import count_words as words
except ImportError:  # running from the repo
    sys.path.insert(0, ".")
    from cmcore.checks import count_words as words
from cmcore import checks
import cmcore.checks as ck


def main():
    print(words("one two three"), checks.LIMIT, ck.shout("ok"))


if __name__ == "__main__":
    main()
'''

CHECKS = '''\
"""Shared check core stub."""
from __future__ import annotations

import re

LIMIT: int = 15


def count_words(text: str) -> int:
    return len(re.findall(r"\\S+", text))


def shout(text: str) -> str:
    return text.upper()


if __name__ == "__main__":
    print("checks self-test")
'''


def release_verdict(build_sha: str) -> str:
    """A valid PASS verdict file (tools/verdict_check.py rules)."""
    return (
        "Result: PASS\nScore: 20/20\nCritical items failed: none\nNot run: none\n\n"
        "| Field | Value |\n|---|---|\n| Subject at commit | release v1.2.3 @ e70891d |\n"
        f"| Build sha | {build_sha} |\n| Edition and lane | en, vn · all |\n"
        "| Producer | lead |\n| Reviewer | release reviewer |\n\n"
        '<!-- scorecard {"result": "PASS", "score": "20/20"} -->\n'
    )


def write(root: Path, rel: str, text: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text) if text.startswith("\n") else text, encoding="utf-8")
    return path


def toml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def sections_file(bodies: dict[str, str], src: dict[str, str] | None = None) -> str:
    out = ["Preamble: maintainer notes, never shipped.", ""]
    for sid, body in bodies.items():
        attr = f" src={src[sid]}" if src else ""
        out += [f"<!-- @section {sid}{attr} -->", body, ""]
    return "\n".join(out)


def make_repo(root: Path, *, skill: bool = True, shiplint: bool = True) -> Path:
    """A small but complete source tree for both editions."""
    write(root, "VERSION", "1.2.3\n")
    for ed, suffix, skill_name, currency in (("en", "EN", "content-machine", "$"),
                                             ("vn", "VN", "content-machine-vn", "đ")):
        write(root, f"editions/{ed}.toml", f'''
            [edition]
            id = "{ed}"
            lang = "{ed}"
            name = "Content Machine"
            skill_name = "{skill_name}"
            file_suffix = "{suffix}"
            zip_name = "Content-Machine-{suffix}"

            [params]
            currency = "{currency}"
            ''')
    write(root, "strings/en.toml", "[strings]\n" + "".join(
        f'"{k}" = {toml_str(v)}\n' for k, v in EN_STRINGS.items()))
    write(root, "strings/vn.toml", "[strings]\n" + "".join(
        f'"{k}" = {{ text = {toml_str(v)}, src = "{cmlib.sha10(EN_STRINGS[k])}" }}\n' for k, v in VN_TEXT.items()))
    write(root, "modules/en/talk.md", sections_file(EN_TALK))
    write(root, "modules/vn/talk.md", sections_file(VN_TALK, {k: cmlib.sha10(v) for k, v in EN_TALK.items()}))
    for lang in ("en", "vn"):
        write(root, f"core/{lang}/start-block.md", '''
            Preamble line that must not ship.
            <!-- @section start.block -->
            {{t:contract.output}}
            {{#if kit}}KIT ROUTER{{else}}PHONE ONLY{{/if}}
            Price in {{currency}}.
            ''')
    write(root, "core/method.toml", '''
        [method]
        title_key = "method.title"
        [[method.anchor]]
        id = "TALK"
        sections = ["talk.*"]
        [[method.anchor]]
        id = "WEEK"
        sections = []
        [[method.anchor]]
        id = "SETUP"
        sections = ["setup.start"]

        [grow]

        [skill]
        [[skill.reference]]
        file = "talk.md"
        sections = ["talk.*"]
        module = "talk"
        formats = ["short", "post"]
        ''')
    write(root, "core/router.toml", '''
        [[route]]
        id = "weekly-talk"
        module = "talk"
        trigger = "The coach says next on talk day."
        trigger_vn = "Người dùng gõ tiếp vào ngày nói chuyện."
        rules = ["One question per message.", "Say 'Got it. Next:' only."]
        loads = ["talk.md"]
        ''')
    write(root, "core/format-checks.toml", '''
        [format.short]
        checks = ["Is the first line under 12 words?", "Is the keyword in once?"]
        checks_vn = ["Câu đầu dưới 18 tiếng?", "Có từ khoá đúng 1 lần?"]
        [format.post]
        checks = ["Is the keyword in once?", "Does it end with one ask?"]
        checks_vn = ["Có từ khoá đúng 1 lần?", "Kết thúc bằng một lời mời?"]
        ''')
    if skill:
        write(root, "core/SKILL.md.tmpl", '''
            ---
            name: {{skill_name}}
            description: "Writes and checks content for {{name}}."
            ---
            # {{name}}
            {{t:contract.output}}
            ''')
    if shiplint:
        write(root, "tools/shiplint.py", SHIPLINT)
        write(root, "tools/cmcore/checks.py", CHECKS)
    write(root, "platform/targets.toml", '''
        [budgets.instructions_block]
        artifact = "1-INSTRUCTIONS.txt"
        unit = "chars_nfc"
        en = 1000
        vn = 1000
        [budgets.method_file]
        artifact = "CONTENT-MACHINE-{EN,VN}.md"
        unit = "bytes"
        en = 51200
        vn = 56320
        [budgets.skill_description]
        artifact = "SKILL.md description"
        unit = "chars_nfc"
        en = 190
        vn = 190
        [budgets.reference_lines]
        artifact = "each skill reference file"
        unit = "lines"
        en = 150
        vn = 150
        [budgets.references_total_bytes]
        artifact = "all skill references"
        unit = "bytes"
        en = 204800
        vn = 204800
        ''')
    return root


class TempRepo(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name).resolve()

    def tearDown(self):
        self._tmp.cleanup()

    def quiet(self, fn, *args):
        """Run a CLI main() and return (exit code, stdout, stderr)."""
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = fn(list(args))
        return code, out.getvalue(), err.getvalue()


# ---------------------------------------------------------------- render

class RenderTests(TempRepo):
    def setUp(self):
        super().setUp()
        make_repo(self.root)
        self.en = cmlib.load_edition("en", self.root)
        self.vn = cmlib.load_edition("vn", self.root)
        self.sections_en, _ = cmlib.load_sections("en", self.root)
        self.sections_vn, _ = cmlib.load_sections("vn", self.root)
        self.router = cmlib.load_toml(self.root / "core/router.toml")
        self.checks = cmlib.load_toml(self.root / "core/format-checks.toml")
        self.ref = cmlib.load_toml(self.root / "core/method.toml")["skill"]["reference"][0]

    def test_render_file_drops_preamble_and_markers(self):
        path = self.root / "core/en/start-block.md"
        kit = render.render_file(path, self.en, "kit", root=self.root)
        phone = render.render_file(path, self.en, "phone", root=self.root)
        self.assertIn("KIT ROUTER", kit)
        self.assertIn("PHONE ONLY", phone)
        self.assertIn("Price in $.", kit)
        for text in (kit, phone):
            self.assertTrue(text.startswith("Always reply in English."), repr(text[:40]))
            self.assertNotIn("Preamble", text)
            self.assertNotIn("@section", text)
            self.assertTrue(text.endswith("\n") and not text.endswith("\n\n"))

    def test_cli_renders_to_stdout_and_reports_errors(self):
        code, out, _ = self.quiet(render.main, "--edition", "vn", "--target", "kit", "--root", str(self.root),
                                  "core/vn/start-block.md")
        self.assertEqual(code, 0)
        self.assertIn("Price in đ.", out)
        write(self.root, "core/en/bad.md", "{{nope}}\n")
        code, _, err = self.quiet(render.main, "--edition", "en", "--target", "kit", "--root", str(self.root),
                                  "core/en/bad.md")
        self.assertEqual(code, 1)
        self.assertTrue(err.startswith("E170 core/en/bad.md: unknown param 'nope'"), err)

    def test_reference_header_and_footer(self):
        text = render.render_reference(self.en, self.ref, self.sections_en, self.router, self.checks)
        lines = text.rstrip("\n").split("\n")
        contract = EN_STRINGS["contract.output"]
        self.assertEqual(lines[0], contract)
        self.assertEqual(lines[-1], contract)
        self.assertIn("WHEN TO USE: The coach says next on talk day.", lines)
        self.assertEqual(lines[lines.index("RULES:") + 1], "- One question per message.")
        check_at = lines.index("CHECK BEFORE ANSWERING:")
        # de-duplicated across the two formats: 3 lines, then the contract line
        self.assertEqual(lines[check_at + 1:-2], ["- Is the first line under 12 words?",
                                                  "- Is the keyword in once?",
                                                  "- Does it end with one ask?"])
        self.assertEqual(lines[-2], "")
        self.assertIn("Ask five questions in $ terms.", text)
        self.assertNotIn("VN only", text)
        self.assertNotIn("CONTENTS:", text)

    def test_reference_vn_uses_localized_router_and_checks(self):
        text = render.render_reference(self.vn, self.ref, self.sections_vn, self.router, self.checks)
        self.assertIn("WHEN TO USE: Người dùng gõ tiếp vào ngày nói chuyện.", text)
        self.assertIn("- Câu đầu dưới 18 tiếng?", text)
        self.assertIn("Chỉ VN.", text)
        self.assertTrue(text.startswith(VN_TEXT["contract.output"] + "\n"))

    def test_reference_over_100_lines_gets_toc(self):
        long_body = "### Long part\n" + "\n".join(f"line {i}" for i in range(120))
        write(self.root, "modules/en/long.md", sections_file({"talk.long": long_body}))
        sections, _ = cmlib.load_sections("en", self.root)
        text = render.render_reference(self.en, self.ref, sections, self.router, self.checks)
        # sections follow file order (long.md loads before talk.md)
        self.assertIn("CONTENTS:\n- Long part\n- Weekly Talk\n- Mini-talk\n", text)
        # the TOC sits between the header and the body
        self.assertLess(text.index("CONTENTS:"), text.index("### Long part"))
        self.assertGreater(text.index("CONTENTS:"), text.index("RULES:"))

    def test_more_than_five_checks_is_an_error(self):
        checks = {"format": {"a": {"checks": ["1?", "2?", "3?"]}, "b": {"checks": ["4?", "5?", "6?"]}}}
        ref = dict(self.ref, formats=["a", "b"])
        with self.assertRaises(CMError) as ctx:
            render.render_reference(self.en, ref, self.sections_en, self.router, checks)
        self.assertEqual(ctx.exception.code, "E170")

    def test_unknown_route_and_format_are_errors(self):
        with self.assertRaises(CMError) as ctx:
            render.render_reference(self.en, dict(self.ref, module="nope"), self.sections_en, self.router, self.checks)
        self.assertEqual(ctx.exception.code, "E130")
        with self.assertRaises(CMError) as ctx:
            render.render_reference(self.en, dict(self.ref, formats=["nope"]), self.sections_en, self.router,
                                    self.checks)
        self.assertEqual(ctx.exception.code, "E161")


# ---------------------------------------------------------------- build

class BuildTests(TempRepo):
    def build_all(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return build.build(self.root, ["en", "vn"])

    def test_method_file_assembly(self):
        make_repo(self.root)
        manifest = self.build_all()
        text = (self.root / "dist/en/CONTENT-MACHINE-EN.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Content Machine · Method\n\nAlways reply in English."))
        self.assertIn("## §CM-TALK · Weekly Talk\n\n### Weekly Talk\nAsk five questions in $ terms.", text)
        self.assertIn("### Mini-talk", text)
        self.assertIn("## §CM-SETUP · SETUP", text)       # no anchor.setup string: the id is the title
        self.assertIn("Say Always reply in English.", text)   # {{t:...}} inside a section
        self.assertNotIn("§CM-WEEK", text)                 # empty anchor skipped ...
        self.assertIn({"edition": "en", "target": "method", "reason": "anchor has no sections yet",
                       "item": "§CM-WEEK"}, manifest["skipped"])   # ... with a note
        self.assertNotIn("@section", text)
        self.assertNotIn("Preamble", text)
        self.assertLess(text.index("§CM-TALK"), text.index("§CM-SETUP"))
        self.assertTrue(text.rstrip("\n").endswith("Always reply in English. One screen per reply."))
        vn = (self.root / "dist/vn/CONTENT-MACHINE-VN.md").read_text(encoding="utf-8")
        self.assertIn("## §CM-TALK · Buổi nói chuyện tuần", vn)
        self.assertIn("Chỉ VN.", vn)

    def test_outputs_and_manifest(self):
        make_repo(self.root)
        manifest = self.build_all()
        dist = self.root / "dist"
        for rel in ("en/1-INSTRUCTIONS.txt", "en/PHONE-STARTER.txt", "en/START-HERE.html",
                    "en/Level-ups/autopilot/content-machine.zip", "vn/Level-ups/autopilot/content-machine-vn.zip"):
            self.assertTrue((dist / rel).is_file(), rel)
        self.assertIn("KIT ROUTER", (dist / "en/1-INSTRUCTIONS.txt").read_text(encoding="utf-8"))
        self.assertIn("PHONE ONLY", (dist / "en/PHONE-STARTER.txt").read_text(encoding="utf-8"))

        art = manifest["artifacts"]["en/1-INSTRUCTIONS.txt"]
        data = (dist / "en/1-INSTRUCTIONS.txt").read_bytes()
        self.assertEqual(art["bytes"], len(data))
        self.assertEqual(art["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual(art["lines"], data.decode().count("\n"))
        budget = art["budgets"]["instructions_block"]
        self.assertEqual(budget["budget"], 1000)
        self.assertEqual(budget["used"], art["nfc_chars"])
        self.assertEqual(budget["percent"], round(art["nfc_chars"] * 100 / 1000, 1))

        self.assertTrue((dist / "maintainer/skill/en/content-machine/SKILL.md").read_text().startswith("---\n"))
        skill_md = manifest["artifacts"]["maintainer/skill/en/content-machine/SKILL.md"]
        self.assertEqual(skill_md["budgets"]["skill_description"]["used"],
                         len("Writes and checks content for Content Machine."))
        ref = manifest["artifacts"]["maintainer/skill/en/content-machine/references/talk.md"]
        self.assertIn("reference_lines", ref["budgets"])
        zip_entry = manifest["artifacts"]["en/Level-ups/autopilot/content-machine.zip"]
        self.assertEqual(zip_entry["budgets"]["references_total_bytes"]["used"], ref["bytes"])
        self.assertEqual(manifest["build_sha256"], package.compute_build_sha256(dist, ["en", "vn"]))
        skipped = {(s["edition"], s["target"]) for s in manifest["skipped"]}
        self.assertIn(("en", "grow"), skipped)
        self.assertIn(("en", "task"), skipped)
        self.assertIn(("vn", "site"), skipped)

    def test_skill_zip_layout_and_self_contained_ship_lint(self):
        make_repo(self.root)
        self.build_all()
        with zipfile.ZipFile(self.root / "dist/en/Level-ups/autopilot/content-machine.zip") as zf:
            names = zf.namelist()
            script = zf.read("content-machine/scripts/ship_lint.py").decode("utf-8")
        self.assertEqual(names, sorted(names))
        self.assertEqual(set(names), {"content-machine/SKILL.md", "content-machine/references/talk.md",
                                      "content-machine/scripts/ship_lint.py"})
        self.assertNotIn("import cmcore", script)
        self.assertNotIn("from cmcore", script)
        self.assertNotIn("checks self-test", script)
        self.assertTrue(script.startswith("#!/usr/bin/env python3\n"))
        with tempfile.TemporaryDirectory() as alone:      # no cmcore next to it
            path = Path(alone) / "ship_lint.py"
            path.write_text(script, encoding="utf-8")
            run = subprocess.run([sys.executable, str(path)], cwd=alone, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(run.stdout.strip(), "3 15 OK")

    def test_missing_later_phase_sources_are_skipped(self):
        make_repo(self.root, skill=False, shiplint=False)
        manifest = self.build_all()
        reasons = {(s["target"], s.get("item")) for s in manifest["skipped"] if s["edition"] == "en"}
        self.assertIn(("skill", None), reasons)
        self.assertFalse((self.root / "dist/en/Level-ups/autopilot").exists())

    def test_empty_skill_builds(self):
        make_repo(self.root, shiplint=False)
        method = (self.root / "core/method.toml").read_text(encoding="utf-8")
        (self.root / "core/method.toml").write_text(method.split("[[skill.reference]]")[0], encoding="utf-8")
        manifest = self.build_all()
        with zipfile.ZipFile(self.root / "dist/en/Level-ups/autopilot/content-machine.zip") as zf:
            self.assertEqual(zf.namelist(), ["content-machine/SKILL.md"])
        self.assertIn({"edition": "en", "target": "skill", "reason": "tools/shiplint.py not present yet",
                       "item": "scripts/ship_lint.py"}, manifest["skipped"])

    def test_render_error_exits_nonzero_with_code(self):
        make_repo(self.root)
        write(self.root, "core/en/start-block.md", "{{t:no.such.key}}\n")
        code, _, err = self.quiet(build.main, "--edition", "en", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertTrue(err.startswith("E170 core/en/start-block.md: unknown string key 'no.such.key'"), err)

    def test_duplicate_section_is_an_error(self):
        make_repo(self.root)
        write(self.root, "modules/en/dupe.md", sections_file({"talk.core": "again"}))
        code, _, err = self.quiet(build.main, "--edition", "en", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertTrue(err.startswith("E114"), err)

    def test_build_twice_is_identical(self):
        make_repo(self.root)
        first = self.build_all()
        zips = {p: package.file_sha256(p) for p in (self.root / "dist").rglob("*.zip")}
        time.sleep(1.1)                    # new mtimes must not change anything
        for p in (self.root / "core").rglob("*"):
            if p.is_file():
                os.utime(p)
        second = self.build_all()
        self.assertEqual(first["build_sha256"], second["build_sha256"])
        self.assertEqual(zips, {p: package.file_sha256(p) for p in (self.root / "dist").rglob("*.zip")})


SAVE_SWAPPED = {"en": 'Save: email the card to yourself. Tomorrow say "{{t:cmd.next}}".',
                "vn": 'Lưu: gửi card vào Zalo. Mai nhắn "{{t:cmd.next}}".'}
COMMANDS = {"en": ("Start", "next"), "vn": ("Bắt đầu", "tiếp")}
PLUGIN_ENTRIES = {
    "content-machine/.claude-plugin/plugin.json",
    "content-machine/README.md",
    "content-machine/skills/content-machine-en/SKILL.md",
    "content-machine/skills/content-machine-en/CONTENT-MACHINE-EN.md",
    "content-machine/skills/content-machine-vn/SKILL.md",
    "content-machine/skills/content-machine-vn/CONTENT-MACHINE-VN.md",
}


def make_portable_repo(root: Path) -> Path:
    """make_repo plus what turns the plugin and the one-file kit on: strings portable.save (and the command words
    it and the plugin use) and the kit's own save line, which the build swaps."""
    make_repo(root)
    for ed, (start, nxt) in COMMANDS.items():
        with open(root / f"strings/{ed}.toml", "a", encoding="utf-8") as fh:
            if ed == "en":
                fh.write(f'"cmd.start" = {toml_str(start)}\n"cmd.next" = {toml_str(nxt)}\n'
                         f'"portable.save" = {toml_str(SAVE_SWAPPED[ed])}\n')
            else:
                for key, text, en in (("cmd.start", start, COMMANDS["en"][0]), ("cmd.next", nxt, COMMANDS["en"][1]),
                                      ("portable.save", SAVE_SWAPPED[ed], SAVE_SWAPPED["en"])):
                    fh.write(f'"{key}" = {{ text = {toml_str(text)}, src = "{cmlib.sha10(en)}" }}\n')
        write_kit(root, ed, build.PORTABLE[ed]["save_from"])
    return root


CHECK_LINES = {"en": "Check for CONTENT-MACHINE-EN.md and the newest BRAND CARD (highest v). Print the check.",
               "vn": "ĐẦU MỖI CHAT: tìm CONTENT-MACHINE-VN.md và BRAND CARD v cao nhất. In dòng kiểm tra."}


def write_kit(root: Path, lang: str, save_line: str | None, check_line: str | None = None) -> None:
    lines = ["Preamble line that must not ship.", "<!-- @section start.block -->", "{{t:contract.output}}",
             "{{#if kit}}KIT ROUTER{{else}}PHONE ONLY{{/if}}"]
    if check_line is not None:
        lines.append(check_line)
    if save_line is not None:
        lines.append(save_line)
    lines.append("Price in {{currency}}.")
    write(root, f"core/{lang}/start-block.md", "\n".join(lines) + "\n")


def swapped(ed: str) -> str:
    return SAVE_SWAPPED[ed].replace("{{t:cmd.next}}", COMMANDS[ed][1])


def front_matter(skill_md: str) -> tuple[dict, str]:
    """name and description from a SKILL.md, and the text after the front matter (description is JSON-quoted)."""
    head, sep, body = skill_md.partition("\n---\n\n")
    lines = head.split("\n")
    assert lines[0] == "---" and sep, skill_md[:80]
    fields = {}
    for line in lines[1:]:
        key, _, value = line.partition(": ")
        fields[key] = json.loads(value) if value.startswith('"') else value
    return fields, body


def anchor_headings(text: str) -> list[str]:
    """The `## §CM-…` heading lines of a method or level-up file, in order."""
    return [ln for ln in text.splitlines() if ln.startswith("## §CM-")]


def count_line(text: str, line: str) -> int:
    """How many times `line` appears in `text` as a whole line."""
    return text.splitlines().count(line)


class PortableTests(TempRepo):
    """dist/content-machine-plugin.zip (one plugin, both editions) and the per-edition one-file kit."""

    def build_all(self, editions=("en", "vn")):
        with contextlib.redirect_stdout(io.StringIO()):
            return build.build(self.root, list(editions))

    @property
    def plugin(self) -> Path:
        return self.root / "dist" / "content-machine-plugin.zip"

    def paths(self, ed: str) -> dict[str, Path]:
        out = self.root / "dist" / ed
        return {"onefile": out / f"CONTENT-MACHINE-{ed.upper()}-1-FILE.md",
                "kit": out / "1-INSTRUCTIONS.txt", "method": out / f"CONTENT-MACHINE-{ed.upper()}.md"}

    def unzip(self) -> dict[str, bytes]:
        with zipfile.ZipFile(self.plugin) as zf:
            return {name: zf.read(name) for name in zf.namelist()}

    def test_plugin_zip_layout(self):
        make_portable_repo(self.root)
        self.build_all()
        files = self.unzip()
        self.assertEqual(list(files), sorted(files))
        self.assertEqual(set(files), PLUGIN_ENTRIES)
        for ed in ("en", "vn"):
            name, method = f"content-machine-{ed}", f"CONTENT-MACHINE-{ed.upper()}.md"
            self.assertEqual(files[f"content-machine/skills/{name}/{method}"], self.paths(ed)["method"].read_bytes())
            self.assertEqual(list((self.root / "dist" / ed).glob("*.zip")), [])    # one plugin, at dist/, not per edition

    def test_plugin_json(self):
        make_portable_repo(self.root)
        self.build_all()
        manifest = json.loads(self.unzip()["content-machine/.claude-plugin/plugin.json"])
        self.assertEqual(set(manifest), {"name", "version", "description", "author", "keywords"})
        self.assertEqual(manifest["name"], "content-machine")
        self.assertEqual(manifest["version"], "1.2.3")                 # the repo's VERSION file
        self.assertEqual(manifest["author"], {"name": "Content Machine"})
        self.assertIn("Tiếng Việt", manifest["description"])           # bilingual
        self.assertIn("English", manifest["description"])
        self.assertEqual(manifest["keywords"], ["content", "coach", "vn", "en"])

    def test_readme_is_bilingual_install_note(self):
        make_portable_repo(self.root)
        self.build_all()
        readme = self.unzip()["content-machine/README.md"].decode("utf-8")
        self.assertLess(readme.index("## Tiếng Việt"), readme.index("## English"))
        for text in ("Customize → Plugins → Add → Upload plugin", "Settings → Security and login",
                     "Developer mode", "`Bắt đầu`", "`Start`", "`tiếp`", "`next`"):
            self.assertIn(text, readme)
        self.assertNotIn("{{", readme)

    def test_both_skills_front_matter_and_body(self):
        make_portable_repo(self.root)
        self.build_all()
        files = self.unzip()
        for ed in ("en", "vn"):
            with self.subTest(ed=ed):
                name, p = f"content-machine-{ed}", self.paths(ed)
                fields, body = front_matter(files[f"content-machine/skills/{name}/SKILL.md"].decode("utf-8"))
                self.assertEqual(set(fields), {"name", "description"})
                self.assertEqual(fields["name"], name)               # the folder name
                desc = fields["description"]
                self.assertLessEqual(len(desc), 200)
                self.assertNotIn("<", desc)
                self.assertNotIn(">", desc)
                for word in COMMANDS[ed]:                              # the coach's own command words
                    self.assertIn(f'"{word}"', desc)
                pointer = f"CONTENT-MACHINE-{ed.upper()}.md"
                self.assertTrue(body.split("\n", 1)[0].count(pointer), body[:100])   # one-line pointer to the method file
                kit, old = p["kit"].read_text(encoding="utf-8"), build.PORTABLE[ed]["save_from"]
                method = p["method"].read_text(encoding="utf-8")
                self.assertIn(old, kit)                                # the kit itself keeps its own line
                self.assertIn(kit.replace(old, swapped(ed)).rstrip(), body)     # the instruction block, save line swapped
                self.assertNotIn(old, body)
                self.assertEqual(body.count(swapped(ed)), 1)
                self.assertTrue(body.endswith(method), "the method file closes SKILL.md")      # ... and then the method

    def test_skill_md_works_alone_it_holds_the_whole_method_file_inline(self):
        """claude.ai cannot read the files bundled next to a SKILL.md without code execution (founder test v10: the
        setup check printed "✗ method file"), so the method file is inside SKILL.md, anchors and all."""
        make_portable_repo(self.root)
        self.build_all()
        files = self.unzip()
        for ed, suffix, h_method in (("en", "EN", "METHOD"), ("vn", "VN", "PHƯƠNG PHÁP")):
            with self.subTest(ed=ed):
                skill = files[f"content-machine/skills/content-machine-{ed}/SKILL.md"].decode("utf-8")
                method = self.paths(ed)["method"].read_text(encoding="utf-8")
                heading = f"## {h_method} (CONTENT-MACHINE-{suffix}.md)"
                self.assertEqual(count_line(skill, heading), 1)
                self.assertIn(f"\n{heading}\n\n{method}", skill)               # the file, byte for byte, under it
                anchors = anchor_headings(method)
                self.assertTrue(anchors)
                for anchor in anchors:                                         # every § anchor of the file, once
                    self.assertEqual(count_line(skill, anchor), 1, anchor)
                self.assertLess(skill.index("\nKIT ROUTER"), skill.index(f"\n{heading}\n"))   # kit first, then method
                pointer = skill.split("---\n\n", 1)[1].split("\n", 1)[0]
                self.assertIn(f"CONTENT-MACHINE-{suffix}.md", pointer)
                self.assertIn(h_method, pointer)                               # "it is under METHOD below"
                self.assertEqual(files[f"content-machine/skills/content-machine-{ed}/CONTENT-MACHINE-{suffix}.md"],
                                 method.encode("utf-8"))                       # the file next to it stays

    def test_the_setup_check_phrase_says_the_method_file_is_the_section_below(self):
        make_portable_repo(self.root)
        for ed in ("en", "vn"):
            write_kit(self.root, ed, build.PORTABLE[ed]["save_from"], CHECK_LINES[ed])
        manifest = self.build_all()
        files = self.unzip()
        want = {"en": "Check for CONTENT-MACHINE-EN.md (it is the METHOD section below, already in this text) and the "
                      "newest BRAND CARD (highest v). Print the check.",
                "vn": "ĐẦU MỖI CHAT: tìm CONTENT-MACHINE-VN.md (chính là phần PHƯƠNG PHÁP bên dưới, đã có sẵn ở đây) "
                      "và BRAND CARD v cao nhất. In dòng kiểm tra."}
        for ed in ("en", "vn"):
            with self.subTest(ed=ed):
                self.assertIn(CHECK_LINES[ed], self.paths(ed)["kit"].read_text(encoding="utf-8"))   # the kit is as is
                skill = files[f"content-machine/skills/content-machine-{ed}/SKILL.md"].decode("utf-8")
                one = self.paths(ed)["onefile"].read_text(encoding="utf-8")
                for name, text in (("SKILL.md", skill), ("1-FILE", one)):
                    self.assertNotIn(CHECK_LINES[ed], text, name)
                    self.assertEqual(text.count(want[ed]), 1, name)
        self.assertEqual([n for n in manifest["notes"] if "setup-check phrase" in n["note"]], [])

    def test_a_kit_without_the_check_phrase_keeps_building_and_leaves_a_note(self):
        make_portable_repo(self.root)                 # the fixture kit prints no setup-check phrase
        manifest = self.build_all()
        self.assertTrue(self.plugin.exists())
        notes = [n for n in manifest["notes"] if "setup-check phrase" in n["note"]]
        self.assertEqual(sorted(n["edition"] for n in notes), ["en", "vn"])    # once per edition, not once per output
        for n in notes:
            self.assertIn("check_from", n["note"])
            self.assertIn("tools/build.py", n["note"])
        pointer = self.unzip()["content-machine/skills/content-machine-en/SKILL.md"].decode("utf-8")
        self.assertIn("is inside this skill, under METHOD below", pointer)    # the pointer line holds either way

    def test_skill_md_sizes_are_in_the_manifest_and_a_huge_one_warns(self):
        make_levelup_repo(self.root)
        manifest = self.build_all()
        entry = manifest["artifacts"]["content-machine-plugin.zip"]
        files = self.unzip()
        sizes = {n.split("/")[2]: len(d) for n, d in files.items() if n.endswith("/SKILL.md")}
        self.assertEqual(entry["skill_md_bytes"], dict(sorted(sizes.items())))
        self.assertEqual(len(sizes), 8)                                         # 2 main skills + 6 companions
        self.assertFalse([n for n in manifest["notes"] if "SKILL.md is" in n["note"]])
        with unittest.mock.patch.object(build, "PLUGIN_SKILL_MD_WARN", 2000), \
                contextlib.redirect_stderr(io.StringIO()) as err:
            warned = self.build_all()
        over = sorted(k for k, v in sizes.items() if v > 2000)
        self.assertTrue(over)
        notes = [n["note"] for n in warned["notes"] if "SKILL.md is" in n["note"]]
        self.assertEqual(len(notes), len(over))
        for skill in over:
            self.assertTrue(any(f"plugin skill {skill}:" in n for n in notes), skill)
            self.assertIn(f"warning: plugin skill {skill}:", err.getvalue())
        self.assertTrue(self.plugin.exists())                                   # a warning, never a stop

    def test_one_file_kit(self):
        make_portable_repo(self.root)
        self.build_all()
        for ed, lead in (("en", "# Content Machine — a file for the AI\n\n"),
                         ("vn", "# Content Machine — file cho AI đọc\n\n")):
            with self.subTest(ed=ed):
                p = self.paths(ed)
                text = p["onefile"].read_text(encoding="utf-8")
                kit, method = p["kit"].read_text(encoding="utf-8"), p["method"].read_text(encoding="utf-8")
                old = build.PORTABLE[ed]["save_from"]
                heads = ("INSTRUCTIONS", "METHOD") if ed == "en" else ("HƯỚNG DẪN", "PHƯƠNG PHÁP")
                self.assertTrue(text.startswith(lead), text[:80])
                self.assertIn(f"\n## {heads[0]}\n\n", text)
                self.assertIn(kit.replace(old, swapped(ed)).rstrip(), text)    # the instruction block, save line swapped
                self.assertNotIn(old, text)
                self.assertTrue(text.endswith(method), "the method file closes the one-file kit")
                self.assertLess(text.index(f"\n## {heads[0]}\n"), text.index(f"\n## {heads[1]}\n\n{method[:20]}"))
                anchors = [ln for ln in method.splitlines() if ln.startswith("## §CM-")]
                self.assertTrue(anchors)
                for heading in anchors:                                        # every §CM anchor of the method file
                    self.assertEqual(text.count("\n" + heading + "\n"), 1, heading)

    def test_outputs_are_deterministic(self):
        make_portable_repo(self.root)
        first_manifest = self.build_all()

        def snapshot():
            return {"plugin": self.plugin.read_bytes(),
                    **{ed: self.paths(ed)["onefile"].read_bytes() for ed in ("en", "vn")}}

        first = snapshot()
        time.sleep(1.1)                    # new mtimes must not change anything
        for p in self.root.rglob("*"):
            if p.is_file():
                os.utime(p)
        second_manifest = self.build_all()
        self.assertEqual(first, snapshot())
        self.assertEqual(first_manifest["build_sha256"], second_manifest["build_sha256"])
        self.assertEqual(first_manifest["artifacts"]["content-machine-plugin.zip"],
                         second_manifest["artifacts"]["content-machine-plugin.zip"])
        with zipfile.ZipFile(self.plugin) as zf:
            for info in zf.infolist():
                self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0), info.filename)
                self.assertEqual(info.external_attr >> 16, 0o100644, info.filename)

    def test_manifest_records_the_outputs(self):
        make_portable_repo(self.root)
        manifest = self.build_all()
        art = manifest["artifacts"]["content-machine-plugin.zip"]
        self.assertEqual((art["edition"], art["target"]), ("all", "plugin"))
        self.assertEqual(art["sha256"], package.file_sha256(self.plugin))
        self.assertEqual(art["entries"], sorted(PLUGIN_ENTRIES))
        for ed in ("en", "vn"):
            one = manifest["artifacts"][f"{ed}/CONTENT-MACHINE-{ed.upper()}-1-FILE.md"]
            self.assertEqual(one["target"], "onefile")
            self.assertEqual(one["sha256"], package.file_sha256(self.paths(ed)["onefile"]))
        self.assertFalse([s for s in manifest["skipped"] if s["target"] in ("plugin", "onefile")])

    def test_without_the_save_string_the_outputs_are_skipped(self):
        make_repo(self.root)                # no strings portable.save: a later phase writes it
        manifest = self.build_all()
        self.assertIn({"edition": "en", "target": "onefile", "reason": "strings key portable.save not present yet"},
                      manifest["skipped"])
        self.assertIn({"edition": "all", "target": "plugin",
                       "reason": "vn: strings key portable.save not present yet"}, manifest["skipped"])
        self.assertFalse(self.plugin.exists())
        self.assertFalse(self.paths("en")["onefile"].exists())

    def test_a_one_edition_build_keeps_both_skills_and_never_leaves_a_stale_plugin(self):
        make_portable_repo(self.root)
        self.build_all()
        before = self.plugin.read_bytes()
        self.build_all(("en",))             # vn is read from dist/vn as the full build left it
        self.assertEqual(self.plugin.read_bytes(), before)
        self.assertEqual(set(self.unzip()), PLUGIN_ENTRIES)
        strings = self.root / "strings/en.toml"
        strings.write_text("".join(ln for ln in strings.read_text(encoding="utf-8").splitlines(True)
                                   if not ln.startswith('"portable.save"')), encoding="utf-8")
        manifest = self.build_all(("en",))  # en can no longer build its half: no old zip next to the new kit
        self.assertFalse(self.plugin.exists())
        self.assertNotIn("content-machine-plugin.zip", manifest["artifacts"])

    def test_a_kit_that_loses_its_save_line_stops_the_build(self):
        save = build.PORTABLE["en"]["save_from"]
        for count, line in ((0, None), (2, save + "\n" + save)):
            with self.subTest(found=count):
                make_portable_repo(self.root)
                write_kit(self.root, "en", line)
                code, _, err = self.quiet(build.main, "--edition", "en", "--root", str(self.root))
                self.assertEqual(code, 1)
                self.assertTrue(err.startswith("E170 dist/en/1-INSTRUCTIONS.txt: the kit's save line must appear "
                                               "exactly once"), err)
                self.assertIn(f"found {count};", err)
                self.assertIn("PORTABLE['en']['save_from']", err)

    def test_the_real_kits_print_the_save_line_exactly_once(self):
        for ed in ("en", "vn"):
            with self.subTest(ed=ed):
                start_block = cmlib.ROOT / "core" / ed / "start-block.md"
                if not start_block.is_file():
                    self.skipTest(f"{start_block} not present")
                kit = render.render_file(start_block, cmlib.load_edition(ed, cmlib.ROOT), "kit", root=cmlib.ROOT)
                self.assertEqual(kit.count(build.PORTABLE[ed]["save_from"]), 1)


class BundleShiplintTests(TempRepo):
    def test_plain_copy_without_cmcore(self):
        write(self.root, "tools/shiplint.py", "import json\nprint(json.dumps(1))\n")
        self.assertEqual(build.bundle_shiplint(self.root), "import json\nprint(json.dumps(1))\n")

    def test_non_stdlib_import_is_an_error(self):
        write(self.root, "tools/shiplint.py", "import cmlib\n")
        with self.assertRaises(CMError):
            build.bundle_shiplint(self.root)

    def test_missing_checks_is_an_error(self):
        write(self.root, "tools/shiplint.py", "from cmcore.checks import x\n")
        with self.assertRaises(CMError) as ctx:
            build.bundle_shiplint(self.root)
        self.assertEqual(ctx.exception.code, "E161")

    def test_future_import_is_hoisted(self):
        write(self.root, "tools/shiplint.py", '"""Doc."""\nfrom cmcore.checks import count_words\n'
                                              'print(count_words("a b"))\n')
        write(self.root, "tools/cmcore/checks.py", CHECKS)
        script = build.bundle_shiplint(self.root)
        self.assertEqual(script.splitlines()[1], "from __future__ import annotations")
        compile(script, "ship_lint.py", "exec")


# ---------------------------------------------------------------- package

class PackageTests(TempRepo):
    def make_tree(self, base: Path):
        write(base, "b.txt", "bee\n")
        write(base, "a/one.md", "one\n")
        write(base, ".hidden", "x")
        write(base, ".git/config", "x")
        write(base, "a/.DS_Store", "x")
        write(base, "__MACOSX/a/._one.md", "x")

    def test_zip_is_deterministic_and_clean(self):
        src = self.root / "src"
        self.make_tree(src)
        first = self.root / "one.zip"
        entries = package.make_zip(src, first, prefix="pack")
        self.assertEqual(entries, ["pack/a/one.md", "pack/b.txt"])
        time.sleep(1.1)
        for p in src.rglob("*"):
            os.utime(p)
        second = self.root / "two.zip"
        package.make_zip(src, second, prefix="pack")
        self.assertEqual(first.read_bytes(), second.read_bytes())
        with zipfile.ZipFile(first) as zf:
            for info in zf.infolist():
                self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
                self.assertEqual(info.external_attr >> 16, 0o100644)
                self.assertFalse(any(part.startswith(".") or part == "__MACOSX"
                                     for part in info.filename.split("/")))

    def test_non_ascii_name_is_e150(self):
        src = self.root / "src"
        write(src, "Hướng-dẫn.md", "x\n")
        with self.assertRaises(CMError) as ctx:
            package.make_zip(src, self.root / "out.zip")
        self.assertEqual(ctx.exception.code, "E150")

    def test_package_edition_and_qa_guard(self):
        make_repo(self.root)
        with contextlib.redirect_stdout(io.StringIO()):
            build.build(self.root, ["en", "vn"])
        code, out, err = self.quiet(package.main, "--root", str(self.root))
        self.assertEqual(code, 0, err)
        self.assertTrue((self.root / "dist/Content-Machine-EN-v1.2.3.zip").is_file())
        self.assertTrue((self.root / "dist/Content-Machine-VN-v1.2.3.zip").is_file())
        write(self.root, "dist/en/qa/verdict.md", "x\n")
        with self.assertRaises(CMError) as ctx:
            package.package_edition(self.root, "en", "1.2.3")
        self.assertEqual(ctx.exception.code, "E153")

    def test_release_gate(self):
        make_repo(self.root)
        with contextlib.redirect_stdout(io.StringIO()):
            manifest = build.build(self.root, ["en", "vn"])
        code, _, err = self.quiet(package.main, "--root", str(self.root), "--release")
        self.assertEqual(code, 1)
        self.assertIn("RELEASE-VERDICT.md", err)
        rel = "qa/releases/v1.2.3"
        # a "Result: PASS" first line is not enough: the verdict must be valid (QA spec §5.5)
        write(self.root, f"{rel}/RELEASE-VERDICT.md", "Result: PASS\nScore: 20/20\nCritical items failed: 2\n")
        write(self.root, f"{rel}/RELEASE-VERDICT.second-read.md", "Result: PASS\n")
        write(self.root, f"{rel}/SIGNOFF.md", f"Decision: SHIP\nBuild: {manifest['build_sha256']}\n")
        code, _, err = self.quiet(package.main, "--root", str(self.root), "--release")
        self.assertEqual(code, 1)
        self.assertIn("RELEASE-VERDICT.md: not a valid verdict", err)
        write(self.root, f"{rel}/RELEASE-VERDICT.md", release_verdict(manifest["build_sha256"]))
        write(self.root, f"{rel}/RELEASE-VERDICT.second-read.md", release_verdict(manifest["build_sha256"]))
        write(self.root, f"{rel}/SIGNOFF.md", f"Decision: SHIP\nBuild: {'0' * 64}\n")
        code, _, err = self.quiet(package.main, "--root", str(self.root), "--release")
        self.assertEqual(code, 1)
        self.assertIn("sha256", err)
        write(self.root, f"{rel}/SIGNOFF.md", f"Decision: SHIP\nBuild: {manifest['build_sha256']}\n")
        code, _, err = self.quiet(package.main, "--root", str(self.root), "--release")
        self.assertEqual(code, 0, err)
        write(self.root, "dist/en/extra.txt", "tampered\n")
        code, _, err = self.quiet(package.main, "--root", str(self.root), "--release")
        self.assertEqual(code, 1)
        self.assertIn("changed since the build", err)

    def test_release_gate_needs_every_packaged_edition_in_the_signed_build(self):
        make_repo(self.root)
        with contextlib.redirect_stdout(io.StringIO()):
            build.build(self.root, ["en", "vn"])
            manifest = build.build(self.root, ["en"])   # a later EN-only build; dist/vn/ is now unsigned
        rel = "qa/releases/v1.2.3"
        write(self.root, f"{rel}/RELEASE-VERDICT.md", release_verdict(manifest["build_sha256"]))
        write(self.root, f"{rel}/RELEASE-VERDICT.second-read.md", release_verdict(manifest["build_sha256"]))
        write(self.root, f"{rel}/SIGNOFF.md", f"Decision: SHIP\nBuild: {manifest['build_sha256']}\n")
        code, _, err = self.quiet(package.main, "--root", str(self.root), "--release")
        self.assertEqual(code, 1)
        self.assertIn("does not cover edition(s) vn", err)
        code, _, err = self.quiet(package.main, "--root", str(self.root), "--release", "--edition", "en")
        self.assertEqual(code, 0, err)


# ---------------------------------------------------------------- ics

class IcsTests(TempRepo):
    EVENTS = [{"summary": "Weekly Talk, with a semicolon; and a comma", "description": "A " + "long line " * 20,
               "weekday": "Tue", "time": "09:30", "start": "2026-10-05"}]

    def test_rfc5545_shape(self):
        text = ics.make_ics(self.EVENTS)
        self.assertTrue(text.endswith("\r\n"))
        self.assertNotIn("\n", text.replace("\r\n", ""))         # no bare LF
        for raw in text.split("\r\n")[:-1]:
            self.assertLessEqual(len(raw.encode("utf-8")), 75, raw)
        lines = ics.unfold(text)
        self.assertEqual(lines[0], "BEGIN:VCALENDAR")
        self.assertEqual(lines[-1], "END:VCALENDAR")
        for prop in ("VERSION:2.0", "BEGIN:VEVENT", "END:VEVENT", "RRULE:FREQ=WEEKLY;BYDAY=TU",
                     "DTSTART:20261006T093000", "DURATION:PT15M"):
            self.assertIn(prop, lines)
        self.assertIn("SUMMARY:Weekly Talk\\, with a semicolon\\; and a comma", lines)
        self.assertTrue(any(ln.startswith("PRODID:") for ln in lines))
        self.assertTrue(any(ln.startswith("DTSTAMP:") and ln.endswith("Z") for ln in lines))
        self.assertFalse(any("TZID" in ln for ln in lines))          # floating local time
        self.assertEqual(lines.count("BEGIN:VEVENT"), lines.count("END:VEVENT"))

    def test_uid_is_deterministic(self):
        uid = [ln for ln in ics.unfold(ics.make_ics(self.EVENTS)) if ln.startswith("UID:")]
        again = [ln for ln in ics.unfold(ics.make_ics(self.EVENTS)) if ln.startswith("UID:")]
        other = [ln for ln in ics.unfold(ics.make_ics([dict(self.EVENTS[0], time="10:00")]))
                 if ln.startswith("UID:")]
        self.assertEqual(uid, again)
        self.assertNotEqual(uid, other)

    def test_folding_keeps_utf8_characters_whole(self):
        text = ics.make_ics([{"summary": "Buổi nói chuyện tuần " * 6, "weekday": "MO", "time": "9:00",
                              "start": "2026-10-05"}])
        data = text.encode("utf-8")
        for raw in data.split(b"\r\n"):
            raw.decode("utf-8")                                      # raises if a character was split
            self.assertLessEqual(len(raw), 75)

    def test_edition_strings_and_defaults(self):
        make_repo(self.root)
        vn = cmlib.load_edition("vn", self.root)
        lines = ics.unfold(ics.make_ics(ics.default_events(vn, start="2026-10-05")))
        self.assertIn("SUMMARY:Buổi nói chuyện tuần · Content Machine", lines)
        self.assertIn("RRULE:FREQ=WEEKLY;BYDAY=FR", lines)
        self.assertIn("DTSTART:20261009T160000", lines)
        code, out, _ = self.quiet(ics.main, "--edition", "en", "--root", str(self.root),
                                  "--out", str(self.root / "r.ics"), "--start", "2026-10-05")
        self.assertEqual(code, 0)
        self.assertIn(b"SUMMARY:Weekly Talk \xc2\xb7 Content Machine\r\n", (self.root / "r.ics").read_bytes())

    def test_fixed_offset_zone(self):
        try:
            text = ics.make_ics(self.EVENTS, tz_floating=False, tz="Asia/Ho_Chi_Minh")
        except ValueError as exc:                                   # no tz database on this machine
            self.skipTest(str(exc))
        lines = ics.unfold(text)
        self.assertIn("DTSTART;TZID=Asia/Ho_Chi_Minh:20261006T093000", lines)
        self.assertIn("TZOFFSETTO:+0700", lines)


# ---------------------------------------------------------------- level-up files, companion skills, agents

REPO = TOOLS.parent
LEVELUP_AREAS = {   # area -> (file, [anchor ids]) as core/method.toml [levelup.<area>] lists them (P3-P5 proposals)
    "research": ("RESEARCH", ["RESEARCH", "RESEARCH-PLAN", "LISTEN", "RESEARCH-ROOT", "RESEARCH-LOOP", "CHANNELS",
                              "AUDIENCE", "NICHE"]),
    "launch": ("LAUNCH", ["LAUNCH", "LAUNCH-BRIEF", "LAUNCH-STEPS", "LAUNCH-DAYS", "LAUNCH-DESK", "LAUNCH-POSTS",
                          "LAUNCH-MESSAGES", "LAUNCH-LIVE", "LAUNCH-DEBRIEF", "ADS"]),
    "board": ("BOARD", ["HUB-NOTION", "HUB-MD", "BOARD", "BOARD-COLUMNS", "BOARD-ROWS", "BOARD-CAMPAIGNS", "NUDGES",
                        "HUB-TASKS", "NUDGE-JOBS", "NUDGE-RULES", "NUDGE-TEXTS", "NUDGE-CLAUDE", "NUDGE-LAUNCH"]),
    "strategy": ("STRATEGY", ["STRATEGY", "SEASON", "WHAT-TO-SAY", "MONTH", "STRATEGY-REVIEW", "CHARACTER-DEEP",
                              "CHARACTER-SCENES", "IDEAS", "MOMENTS", "LIKED", "PACKAGING", "HOOKS", "TEXT-FORMATS",
                              "LONG", "LONG-INTRO", "LONG-CUTS"]),
    "playbook": ("PLAYBOOK", ["STRATEGY-ENGINE", "TIERS", "CONTENT-LINES", "CALENDAR", "STRATEGY-DOC"]),
    "hooks": ("HOOKS", ["HOOK-LIBRARY", "HOOK-FLIP", "HOOK-PROOF", "HOOK-SCENE", "HOOK-CALLOUT", "HOOK-MISTAKE",
                        "HOOK-SHORT", "HOOK-TITLES", "HOOK-TEXT", "HOOK-ADS", "HOOK-CTA"]),
    "campaigns": ("CAMPAIGNS", ["CAMPAIGNS", "CAMPAIGN-FOUNDING", "CAMPAIGN-GIFT", "CAMPAIGN-CLASS", "CAMPAIGN-EVENT",
                                "CAMPAIGN-APPLY", "CAMPAIGN-RELAUNCH", "LAUNCH-PREP", "OBJECTIONS", "LAUNCH-FAQ",
                                "SALES-PAGE", "LAUNCH-SEQUENCES", "RUN-OF-SHOW", "LIVE-SELLING", "LAUNCH-TIMING",
                                "LAUNCH-AFTER"]),
    "banks": ("BANKS", ["BANKS", "CTA-BANK", "MAGNET-BANK", "RESEARCH-BANK", "STORY-BANK", "PROOF-BANK"]),
    "copy": ("COPY", ["COPY", "COPY-FRAMEWORKS", "COPY-STORIES", "COPY-BELIEFS", "COPY-PROBLEM", "COPY-PROOF",
                      "COPY-LONG", "COPY-LISTS", "STORYTELLING", "PERSUASION", "COPY-VOICE"]),
}
LEVELUP_BUDGETS = {   # bytes (en, vn) where an area is not the 30,720 B default
    "strategy": (36864, 36864),      # +MONTH, LIKED (7 Oct)
    "hooks": (45056, 58368),         # the hook library, built size + ~15% (7 Oct)
    "campaigns": (53248, 72704),     # the launch campaign library, built size + ~15% (7 Oct)
    "research": (41984, 54272),      # +CHANNELS, AUDIENCE, NICHE (9 Oct)
    "board": (35840, 47104),         # the hub and the tasks that read and write it (9 Oct)
    "playbook": (34816, 45056),      # the strategy engine, tiers, lines, calendar (9 Oct)
    "banks": (32768, 40960),         # the banks (9 Oct)
    "copy": (40960, 53248),          # the writing frameworks, storytelling, persuasion (9 Oct)
}
PLUGIN_SKILLS = ["cm-board", "cm-launch", "cm-research", "cm-strategy", "cm-playbook", "cm-hooks", "cm-campaigns",
                 "cm-banks", "cm-copy"]
PLUGIN_AGENTS = ["cm-listener", "cm-researcher", "cm-reviewer", "cm-writer"]
FIXTURE_AREAS = ("research", "launch", "board")      # the areas make_levelup_repo builds (a subset of the real nine)

LEVELUP_METHOD = '''
[levelup.research]
file = "RESEARCH"
skill = "cm-research"
title_key = "levelup.research.title"
budget = "levelup_research"
[[levelup.research.anchor]]
id = "RESEARCH"
sections = ["research.grow-rules"]
[[levelup.research.anchor]]
id = "RESEARCH-PLAN"
sections = ["research.grow-plan", "research.grow-listen"]

[levelup.launch]
file = "LAUNCH"
skill = "cm-launch"
title_key = "levelup.launch.title"
budget = "levelup_launch"
[[levelup.launch.anchor]]
id = "LAUNCH"
sections = ["launch.grow-start"]

[levelup.board]
file = "BOARD"
skill = "cm-board"
title_key = "levelup.board.title"
budget = "levelup_board"
assets = "Board"
assets_from = "templates/sheets/{lang}"
[[levelup.board.anchor]]
id = "BOARD"
sections = ["hub.grow-board"]
'''


def make_levelup_repo(root: Path) -> Path:
    """make_portable_repo plus three level-up areas (research with two anchors, launch with one, board with CSV
    assets), the real plugin/companions.toml and plugin/agents/: what turns the level-up files and the companion
    skills on."""
    make_portable_repo(root)
    en = {"research.grow-rules": "### Rules\nRead first. The plan is in §CM-RESEARCH-PLAN.",
          "research.grow-plan": "### Plan\nOne buyer.{{#if vn}} VN only.{{/if}}",
          "research.grow-listen": "### Listen\nRead-only. {{t:contract.output}}",
          "launch.grow-start": "### Start\nPick a type; the real limits are in §CM-LAUNCH.",
          "hub.grow-board": "### Board\nOne sheet, five tabs: the files are in Level-ups/Board."}
    vn = {"research.grow-rules": "### Luật\nĐọc trước. Kế hoạch ở §CM-RESEARCH-PLAN.",
          "research.grow-plan": "### Kế hoạch\nMột tệp khách.{{#if vn}} Chỉ VN.{{/if}}",
          "research.grow-listen": "### Nghe\nChỉ đọc. {{t:contract.output}}",
          "launch.grow-start": "### Mở đầu\nChọn kiểu; giới hạn thật ở §CM-LAUNCH.",
          "hub.grow-board": "### Bảng\nMột sheet, năm tab: file ở Level-ups/Board."}
    for module in ("research", "launch", "hub"):
        e = {k: v for k, v in en.items() if k.startswith(module + ".")}
        v = {k: x for k, x in vn.items() if k.startswith(module + ".")}
        write(root, f"modules/en/{module}.md", sections_file(e))
        write(root, f"modules/vn/{module}.md", sections_file(v, {k: cmlib.sha10(b) for k, b in e.items()}))
    method = (root / "core/method.toml").read_text(encoding="utf-8")
    write(root, "core/method.toml", method + LEVELUP_METHOD)
    titles = {"levelup.research.title": ("{{name}} · Research", "{{name}} · Nghiên cứu"),
              "levelup.launch.title": ("{{name}} · Launch", "{{name}} · Mở bán"),
              "levelup.board.title": ("{{name}} · Board", "{{name}} · Bảng"),
              "anchor.research": ("Rules", "Luật"), "anchor.research-plan": ("Plan and listening", "Kế hoạch và nghe"),
              "anchor.launch": ("Launch start", "Mở bán"), "anchor.board": ("Your board", "Bảng của bạn")}
    with open(root / "strings/en.toml", "a", encoding="utf-8") as fh:
        for key, (e, _) in titles.items():
            fh.write(f'"{key}" = {toml_str(e)}\n')
    with open(root / "strings/vn.toml", "a", encoding="utf-8") as fh:
        for key, (e, v) in titles.items():
            fh.write(f'"{key}" = {{ text = {toml_str(v)}, src = "{cmlib.sha10(e)}" }}\n')
    targets = (root / "platform/targets.toml").read_text(encoding="utf-8")
    budgets = "".join(f'\n[budgets.levelup_{a}]\nartifact = "Level-ups/{LEVELUP_AREAS[a][0]}-{{EN,VN}}.md"\n'
                      f'unit = "bytes"\nen = 2000\nvn = 3000\nlimit = ""\n' for a in FIXTURE_AREAS)
    write(root, "platform/targets.toml", targets + budgets)
    write(root, "templates/sheets/en/Campaigns.csv", "Key,Campaign\n")
    write(root, "templates/sheets/vn/Chien-dich.csv", "Mã,Chiến dịch\n")
    for rel in ["plugin/companions.toml"] + [f"plugin/agents/{n}.md" for n in PLUGIN_AGENTS]:
        write(root, rel, (REPO / rel).read_text(encoding="utf-8"))
    return root


class LevelUpTests(TempRepo):
    """Level-ups/<FILE>-<SUFFIX>.md, one per area per edition, from core/method.toml [levelup.<area>]."""

    def build_all(self, editions=("en", "vn")):
        with contextlib.redirect_stdout(io.StringIO()):
            return build.build(self.root, list(editions))

    def test_one_file_per_area_with_its_anchors(self):
        make_levelup_repo(self.root)
        manifest = self.build_all()
        for ed, suffix in (("en", "EN"), ("vn", "VN")):
            self.assertFalse((self.root / "dist" / ed / "Level-ups" / f"GROW-{suffix}.md").exists())
            for file in ("RESEARCH", "LAUNCH", "BOARD"):
                self.assertTrue((self.root / "dist" / ed / "Level-ups" / f"{file}-{suffix}.md").is_file(), file)
        text = (self.root / "dist/en/Level-ups/RESEARCH-EN.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Content Machine · Research\n\n## §CM-RESEARCH · Rules\n\n### Rules\n"),
                        text[:90])
        self.assertLess(text.index("§CM-RESEARCH ·"), text.index("§CM-RESEARCH-PLAN ·"))
        self.assertIn("### Plan\nOne buyer.", text)
        self.assertIn("### Listen\nRead-only. Always reply in English.", text)   # two sections, one anchor
        self.assertNotIn("VN only", text)
        self.assertNotIn("@section", text)
        self.assertEqual(text.count("Always reply in English."), 1)      # the contract only inside the section's own tag
        self.assertTrue(text.endswith("\n") and not text.endswith("\n\n"))
        vn = (self.root / "dist/vn/Level-ups/RESEARCH-VN.md").read_text(encoding="utf-8")
        self.assertTrue(vn.startswith("# Content Machine · Nghiên cứu\n\n## §CM-RESEARCH · Luật\n"), vn[:80])
        self.assertIn("Chỉ VN.", vn)
        art = manifest["artifacts"]["en/Level-ups/RESEARCH-EN.md"]
        self.assertEqual((art["target"], art["level_up"]), ("grow", "research"))
        self.assertEqual(art["budgets"]["levelup_research"]["budget"], 2000)
        self.assertEqual(set(art["anchors"]), {"§CM-RESEARCH", "§CM-RESEARCH-PLAN"})
        # a level-up anchor may hold several sections: lint checks them one by one, so no per-anchor budget here
        self.assertNotIn("method_section", art["anchors"]["§CM-RESEARCH"].get("budgets", {}))
        self.assertEqual(manifest["artifacts"]["vn/Level-ups/LAUNCH-VN.md"]["budgets"]["levelup_launch"]["budget"], 3000)

    def test_board_files_ship_next_to_the_board_file(self):
        make_levelup_repo(self.root)
        manifest = self.build_all()
        self.assertEqual((self.root / "dist/en/Level-ups/Board/Campaigns.csv").read_text(encoding="utf-8"),
                         "Key,Campaign\n")
        self.assertEqual((self.root / "dist/vn/Level-ups/Board/Chien-dich.csv").read_text(encoding="utf-8"),
                         "Mã,Chiến dịch\n")
        self.assertEqual(manifest["artifacts"]["en/Level-ups/Board/Campaigns.csv"]["level_up"], "board")
        self.assertFalse((self.root / "dist/en/Level-ups/Board/Chien-dich.csv").exists())

    def test_anchor_ids_are_unique_across_files(self):
        make_levelup_repo(self.root)
        method = self.root / "core/method.toml"
        method.write_text(method.read_text(encoding="utf-8").replace('id = "LAUNCH"', 'id = "TALK"'), encoding="utf-8")
        code, _, err = self.quiet(build.main, "--edition", "en", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertTrue(err.startswith("E161 core/method.toml: anchor id 'TALK' is in [method] and [levelup.launch]"),
                        err)

    def test_without_level_up_tables_the_target_is_skipped(self):
        make_repo(self.root)
        manifest = self.build_all()
        self.assertIn({"edition": "en", "target": "grow",
                       "reason": "core/method.toml has no [levelup.<area>] tables yet"}, manifest["skipped"])
        self.assertEqual(list((self.root / "dist/en").glob("Level-ups/*.md")), [])

    def test_plugin_has_a_companion_skill_per_area_and_the_agents(self):
        make_levelup_repo(self.root)
        self.build_all()
        with zipfile.ZipFile(self.root / "dist/content-machine-plugin.zip") as zf:
            files = {n: zf.read(n) for n in zf.namelist()}
        self.assertEqual(list(files), sorted(files))
        skills = {n.split("/")[2] for n in files if n.startswith("content-machine/skills/")}
        stems = ("cm-research", "cm-launch", "cm-board")
        want = {f"content-machine-{ed}" for ed in ("en", "vn")} | {f"{s}-{ed}" for s in stems for ed in ("en", "vn")}
        self.assertEqual(skills, want)
        for ed, suffix in (("en", "EN"), ("vn", "VN")):
            edition = cmlib.load_edition(ed, self.root)
            for stem, file in (("cm-research", "RESEARCH"), ("cm-launch", "LAUNCH"), ("cm-board", "BOARD")):
                name = f"{stem}-{ed}"
                fields, body = front_matter(files[f"content-machine/skills/{name}/SKILL.md"].decode("utf-8"))
                self.assertEqual(set(fields), {"name", "description"})
                self.assertEqual(fields["name"], name)
                self.assertTrue(0 < len(fields["description"]) <= 200)
                self.assertNotIn("<", fields["description"])
                self.assertNotIn(">", fields["description"])
                self.assertTrue(body.startswith(render.render_string("contract.output", edition, "kit")), body[:80])
                self.assertIn(f"{file}-{suffix}.md", body)
                self.assertIn(f"content-machine-{ed}", body)
                for other in stems:
                    self.assertEqual(f"{other}-{ed}" in body, other != stem, (name, other))   # siblings, never itself
                self.assertEqual(files[f"content-machine/skills/{name}/{file}-{suffix}.md"],
                                 (self.root / "dist" / ed / "Level-ups" / f"{file}-{suffix}.md").read_bytes())
            main = files[f"content-machine/skills/content-machine-{ed}/SKILL.md"].decode("utf-8")
            first = main.split("---\n\n", 1)[1].split("\n", 1)[0]
            self.assertIn(f"CONTENT-MACHINE-{suffix}.md", first)      # the pointer is still one line ...
            for stem in stems:
                self.assertIn(f"{stem}-{ed}", first)                   # ... and names the companions
        self.assertIn("content-machine/skills/cm-board-en/Board/Campaigns.csv", files)
        self.assertIn("content-machine/skills/cm-board-vn/Board/Chien-dich.csv", files)
        self.assertEqual({n for n in files if n.startswith("content-machine/agents/")},
                         {f"content-machine/agents/{a}.md" for a in PLUGIN_AGENTS})
        manifest = json.loads(files["content-machine/.claude-plugin/plugin.json"])
        self.assertEqual(manifest["keywords"], ["content", "coach", "vn", "en"])
        self.assertIn("Companions", manifest["description"])

    def test_a_companion_skill_md_works_alone_it_holds_its_level_up_file_and_the_board_files_inline(self):
        make_levelup_repo(self.root)
        self.build_all()
        with zipfile.ZipFile(self.root / "dist/content-machine-plugin.zip") as zf:
            files = {n: zf.read(n).decode("utf-8") for n in zf.namelist() if n.endswith((".md", ".csv"))}
        for ed, suffix in (("en", "EN"), ("vn", "VN")):
            for stem, file in (("cm-research", "RESEARCH"), ("cm-launch", "LAUNCH"), ("cm-board", "BOARD")):
                with self.subTest(skill=f"{stem}-{ed}"):
                    base = f"content-machine/skills/{stem}-{ed}"
                    skill, level = files[f"{base}/SKILL.md"], files[f"{base}/{file}-{suffix}.md"]
                    heading = f"## FILE ({file}-{suffix}.md)"
                    self.assertEqual(count_line(skill, heading), 1)
                    self.assertIn(f"\n{heading}\n\n{level.rstrip()}\n", skill)        # the file, whole, under it
                    for anchor in anchor_headings(level):
                        self.assertEqual(count_line(skill, anchor), 1, anchor)
                    body = skill.split(f"\n{heading}\n", 1)[0]
                    self.assertIn(f'under "FILE ({file}-{suffix}.md)" below' if ed == "en"
                                  else f'ở phần "FILE ({file}-{suffix}.md)" bên dưới', body)
                    self.assertNotIn("sits next to this file", body)
                    self.assertNotIn("nằm cạnh file này", body)
        board = {"en": ("Campaigns.csv", "Key,Campaign\n", "FILES IN Board/"),
                 "vn": ("Chien-dich.csv", "Mã,Chiến dịch\n", "FILE TRONG Board/")}
        for ed, (name, content, heading) in board.items():
            skill = files[f"content-machine/skills/cm-board-{ed}/SKILL.md"]
            self.assertEqual(count_line(skill, f"## {heading}"), 1)
            self.assertIn(f"### Board/{name}\n\n```csv\n{content.rstrip()}\n```", skill)
            self.assertTrue(skill.endswith("```\n"))                                   # the CSV rows close SKILL.md
            self.assertIn(f'"{heading}"', skill.split(f"\n## {heading}\n", 1)[0])     # the BOARD FILES line names it
            for other in ("research", "launch"):                                       # only the board has files
                self.assertNotIn("```csv", files[f"content-machine/skills/cm-{other}-{ed}/SKILL.md"])

    def test_every_companion_body_carries_the_house_rules_and_the_harness(self):
        make_levelup_repo(self.root)
        self.build_all()
        rules = {"en": ("one NEXT line", "[NEEDS: …]", "never post, react, follow, DM or join",
                        "subagents or parallel tasks", "separate reviewer", "sees only the result",
                        "Claude in Chrome or ChatGPT Work", "asking once", "never on Day 0", "fake scarcity"),
                 "vn": ("một dòng TIẾP", "[CẦN {XƯNG HÔ}: …]", "không đăng, thả cảm xúc, theo dõi, nhắn tin hay vào nhóm",
                        "trợ lý con hay việc song song", "người soát riêng", "Coach chỉ thấy kết quả",
                        "Claude in Chrome hay ChatGPT Work", "hỏi đúng một lần", "không bao giờ ngày 0",
                        "khan hiếm giả")}
        with zipfile.ZipFile(self.root / "dist/content-machine-plugin.zip") as zf:
            for ed, phrases in rules.items():
                for stem in ("cm-research", "cm-launch", "cm-board"):
                    body = zf.read(f"content-machine/skills/{stem}-{ed}/SKILL.md").decode("utf-8")
                    for phrase in phrases:
                        self.assertIn(phrase, body, (stem, ed))

    def test_agents_are_valid_and_short(self):
        for name in PLUGIN_AGENTS:
            text = (REPO / "plugin" / "agents" / f"{name}.md").read_text(encoding="utf-8")
            lines = text.splitlines()
            self.assertLessEqual(len(lines), 60, name)
            self.assertEqual(lines[0], "---")
            end = lines.index("---", 1)
            fields = {ln.split(":", 1)[0]: ln.split(":", 1)[1].strip() for ln in lines[1:end]}
            self.assertEqual(fields["name"], name)
            self.assertTrue(fields["description"].startswith('"') and "/" in fields["description"], name)   # EN / VN
        for name, must in (("cm-researcher", ("Never post", "role only", "VERBATIM")),
                           ("cm-listener", ("2 or more different people in 2 or more independent places", "WATCH")),
                           ("cm-writer", ("ONE piece", "[NEEDS: …]", "[CẦN BẠN: …]")),
                           ("cm-reviewer", ("never rewrite", "fake scarcity", "Vietnamese naturalness"))):
            text = (REPO / "plugin" / "agents" / f"{name}.md").read_text(encoding="utf-8")
            for phrase in must:
                self.assertIn(phrase.lower(), text.lower(), (name, phrase))
        for name in ("cm-listener", "cm-writer", "cm-reviewer"):     # these never touch the web or write files
            text = (REPO / "plugin" / "agents" / f"{name}.md").read_text(encoding="utf-8")
            self.assertIn("\ntools: Read, Grep, Glob\n", text, name)

    def test_a_missing_level_up_file_skips_the_plugin_not_the_edition(self):
        make_levelup_repo(self.root)
        self.build_all()
        (self.root / "dist/vn/Level-ups/BOARD-VN.md").unlink()
        manifest = self.build_all(("en",))                  # vn is read from dist/vn as it stands
        self.assertIn({"edition": "all", "target": "plugin",
                       "reason": "vn: Level-ups/BOARD-VN.md is not built yet"}, manifest["skipped"])
        self.assertFalse((self.root / "dist/content-machine-plugin.zip").exists())

    def test_companion_description_over_200_characters_stops_the_build(self):
        make_levelup_repo(self.root)
        path = self.root / "plugin/companions.toml"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("Content Machine hub and scheduled tasks:",
                                     "Content Machine hub and scheduled tasks: " + "x" * 120, 1), encoding="utf-8")
        code, _, err = self.quiet(build.main, "--edition", "all", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertTrue(err.startswith("E102 plugin/companions.toml: cm-board-en: description is"), err)

    def test_an_agent_over_60_lines_stops_the_build(self):
        make_levelup_repo(self.root)
        path = self.root / "plugin/agents/cm-writer.md"
        path.write_text(path.read_text(encoding="utf-8") + "extra line\n" * 40, encoding="utf-8")
        code, _, err = self.quiet(build.main, "--edition", "all", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertIn("E161 plugin/agents/cm-writer.md", err)
        self.assertIn("over the 60", err)

    def test_the_plugin_is_deterministic(self):
        make_levelup_repo(self.root)
        first = self.build_all()
        zip1 = (self.root / "dist/content-machine-plugin.zip").read_bytes()
        time.sleep(1.1)
        for p in self.root.rglob("*"):
            if p.is_file():
                os.utime(p)
        second = self.build_all()
        self.assertEqual(zip1, (self.root / "dist/content-machine-plugin.zip").read_bytes())
        self.assertEqual(first["build_sha256"], second["build_sha256"])


class TaskTargetTests(TempRepo):
    """automation/*.tmpl rendered for lint; automation/tasks.toml names what each one is."""

    def build_all(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return build.build(self.root, ["en", "vn"])

    def make(self):
        make_repo(self.root)
        en = "### Nudge\nOpen {{name}} and say 'next'."
        vn = "### Nhắc\nMở {{name}} rồi nhắn 'tiếp'."
        ids = ("automation.grow-task-week", "automation.grow-task-today")
        write(self.root, "modules/en/automation.md", sections_file({i: en for i in ids}))
        write(self.root, "modules/vn/automation.md", sections_file({i: vn for i in ids}, {i: cmlib.sha10(en) for i in ids}))
        write(self.root, "automation/task-nudge.tmpl", "{{>automation.grow-task-week}}\n")
        write(self.root, "automation/task-nudge-today.tmpl", "{{>automation.grow-task-today}}\n")
        write(self.root, "automation/tasks.toml", textwrap.dedent('''
            schema_version = 1
            [[task]]
            id = "week"
            template = "task-nudge.tmpl"
            section = "automation.grow-task-week"
            [[task]]
            id = "today"
            template = "task-nudge-today.tmpl"
            section = "automation.grow-task-today"
            '''))
        targets = (self.root / "platform/targets.toml").read_text(encoding="utf-8")
        write(self.root, "platform/targets.toml", targets + textwrap.dedent('''
            [budgets.task_nudge]
            artifact = "automation/task-nudge.tmpl rendered"
            unit = "chars_nfc"
            en = 900
            vn = 900
            limit = ""
            '''))

    def test_every_nudge_stem_carries_the_task_nudge_budget_and_its_task_id(self):
        self.make()
        manifest = self.build_all()
        for ed in ("en", "vn"):
            for stem, task in (("task-nudge", "week"), ("task-nudge-today", "today")):
                art = manifest["artifacts"][f"maintainer/tasks/{ed}/{stem}.txt"]
                self.assertEqual(art["target"], "task")
                self.assertEqual(art["task_id"], task)
                self.assertEqual(art["budgets"]["task_nudge"]["budget"], 900, (ed, stem))
        self.assertIn("Open Content Machine and say 'next'.",
                      (self.root / "dist/maintainer/tasks/en/task-nudge-today.txt").read_text(encoding="utf-8"))

    def test_a_task_that_names_a_missing_template_or_section_stops_the_build(self):
        self.make()
        path = self.root / "automation/tasks.toml"
        good = path.read_text(encoding="utf-8")
        path.write_text(good.replace('"task-nudge-today.tmpl"', '"task-nudge-gone.tmpl"'), encoding="utf-8")
        code, _, err = self.quiet(build.main, "--edition", "en", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertTrue(err.startswith("E161 automation/tasks.toml: [[task]] 'today' names template "
                                       "'task-nudge-gone.tmpl'"), err)
        path.write_text(good.replace('section = "automation.grow-task-today"', 'section = "automation.grow-task-none"'),
                        encoding="utf-8")
        code, _, err = self.quiet(build.main, "--edition", "en", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertIn("section 'automation.grow-task-none', which does not exist", err)


class RealRepoLevelUps(unittest.TestCase):
    """The real source tree, built once into a temp folder: the nine level-up files, the Board CSVs, the nudge
    texts and the plugin with its 20 skills and 4 agents."""

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls._tmp.name).resolve()
        for name in ("core", "modules", "strings", "editions", "platform", "schemas", "locales", "templates",
                     "automation", "plugin"):
            if (REPO / name).is_dir():
                shutil.copytree(REPO / name, cls.root / name, ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy(REPO / "VERSION", cls.root / "VERSION")
        with contextlib.redirect_stdout(io.StringIO()):
            cls.manifest = build.build(cls.root, ["en", "vn"])
        cls.method = tomllib.loads((cls.root / "core/method.toml").read_text(encoding="utf-8"))
        cls.targets = tomllib.loads((cls.root / "platform/targets.toml").read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_the_nine_level_up_tables_hold_the_proposed_anchors_in_order(self):
        tables = {a: cfg for a, cfg in cmlib.levelup_tables(self.method)}
        self.assertEqual(list(tables), list(LEVELUP_AREAS))
        for area, (file, anchors) in LEVELUP_AREAS.items():
            self.assertEqual(tables[area]["file"], file)
            self.assertEqual([a["id"] for a in tables[area]["anchor"]], anchors, area)
            self.assertEqual(tables[area]["skill"], f"cm-{area}")
        self.assertNotIn("grow", self.method)           # the one GROW file is gone

    def test_every_anchor_renders_in_both_editions_within_the_budget(self):
        for ed, suffix in (("en", "EN"), ("vn", "VN")):
            edition = cmlib.load_edition(ed, self.root)
            titles = edition.strings
            for area, (file, anchors) in LEVELUP_AREAS.items():
                with self.subTest(edition=ed, area=area):
                    path = self.root / "dist" / ed / "Level-ups" / f"{file}-{suffix}.md"
                    text = path.read_text(encoding="utf-8")
                    heads = [ln for ln in text.splitlines() if ln.startswith("## §CM-")]
                    self.assertEqual([h.split(" ")[1] for h in heads], [f"§CM-{a}" for a in anchors])
                    for head, anchor in zip(heads, anchors):
                        title = cmlib.render(titles[f"anchor.{anchor.lower()}"], edition, "grow").strip()
                        self.assertEqual(head, f"## §CM-{anchor} · {title}")      # a title string, never the bare id
                    self.assertTrue(text.startswith("# Content Machine · "), text[:60])
                    self.assertNotIn("@section", text)
                    self.assertNotIn("{{", text)
                    budget = self.targets["budgets"][f"levelup_{area}"][ed]
                    self.assertEqual(budget, LEVELUP_BUDGETS.get(area, (30720, 30720))[ed == "vn"])
                    self.assertLessEqual(len(text.encode("utf-8")), budget, f"{path.name}: {len(text.encode('utf-8'))} B")
                    entry = self.manifest["artifacts"][f"{ed}/Level-ups/{file}-{suffix}.md"]
                    self.assertEqual(entry["budgets"][f"levelup_{area}"]["budget"], budget)
                    self.assertEqual(entry["bytes"], len(text.encode("utf-8")))

    def test_no_matt_gray_framework_names_in_the_level_up_files(self):
        banned = ("Content Waterfall", "Content GPS", "4-3-2-1", "Authenticity Machine", "Founder OS")
        for path in sorted((self.root / "dist").glob("*/Level-ups/*.md")):
            text = path.read_text(encoding="utf-8")
            for word in banned:
                self.assertNotIn(word, text, path.name)

    def test_the_board_files_are_in_level_ups_board_and_match_the_schema(self):
        hub = tomllib.loads((self.root / "schemas/hub.toml").read_text(encoding="utf-8"))
        for ed, fkey, nkey in (("en", "file", "name"), ("vn", "file_vn", "name_vn")):
            for table in hub["campaign_board"]["tables"]:
                path = self.root / "dist" / ed / "Level-ups" / "Board" / table[fkey]
                self.assertTrue(path.is_file(), path)
                header = next(csv.reader(io.StringIO(path.read_text(encoding="utf-8"))))
                self.assertEqual(header, [cmlib.nfc(c[nkey]) for c in table["columns"]], f"{ed} {table[fkey]}")
            self.assertEqual(len(list((self.root / "dist" / ed / "Level-ups" / "Board").glob("*.csv"))), 5)

    def test_the_column_lines_of_the_board_prose_match_the_schema(self):
        hub = tomllib.loads((self.root / "schemas/hub.toml").read_text(encoding="utf-8"))
        for ed, nkey in (("en", "name"), ("vn", "name_vn")):
            text = (self.root / "dist" / ed / "Level-ups" / f"BOARD-{ed.upper()}.md").read_text(encoding="utf-8")
            block = text.split("## §CM-BOARD-COLUMNS", 1)[1].split("\n## §CM-", 1)[0]
            lines = {ln.split(":", 1)[0]: ln.split(":", 1)[1] for ln in block.splitlines() if ":" in ln}
            for table in hub["campaign_board"]["tables"]:
                want = [cmlib.nfc(c[nkey]) for c in table["columns"]]
                got = [re.sub(r"\s*\(.*\)$", "", c.strip()) for c in lines[cmlib.nfc(table[nkey])].split(" · ")]
                self.assertEqual(got, want, f"{ed} {table[nkey]}")

    def test_nudge_texts_are_within_the_task_nudge_budget(self):
        tasks = tomllib.loads((self.root / "automation/tasks.toml").read_text(encoding="utf-8"))
        self.assertEqual(tasks["caps"]["max_chars_filled"], self.targets["budgets"]["task_nudge"]["en"])
        for ed in ("en", "vn"):
            for row in tasks["task"]:
                stem = row["template"].removesuffix(".tmpl")
                path = self.root / "dist/maintainer/tasks" / ed / f"{stem}.txt"
                self.assertLessEqual(cmlib.nfc_len(path.read_text(encoding="utf-8")), 900, (ed, stem))
                art = self.manifest["artifacts"][f"maintainer/tasks/{ed}/{stem}.txt"]
                self.assertEqual((art["task_id"], art["budgets"]["task_nudge"]["budget"]), (row["id"], 900))

    def test_the_plugin_has_the_twenty_skills_and_four_agents(self):
        with zipfile.ZipFile(self.root / "dist/content-machine-plugin.zip") as zf:
            files = {n: zf.read(n) for n in zf.namelist()}
        skills = sorted({n.split("/")[2] for n in files if n.startswith("content-machine/skills/")})
        want = sorted([f"content-machine-{ed}" for ed in ("en", "vn")]
                      + [f"{s}-{ed}" for s in PLUGIN_SKILLS for ed in ("en", "vn")])
        self.assertEqual(len(skills), 20)
        self.assertEqual(skills, want)
        for ed, suffix in (("en", "EN"), ("vn", "VN")):
            for area, (file, anchors) in LEVELUP_AREAS.items():
                name = f"cm-{area}-{ed}"
                fields, body = front_matter(files[f"content-machine/skills/{name}/SKILL.md"].decode("utf-8"))
                self.assertEqual(set(fields), {"name", "description"})
                self.assertEqual(fields["name"], name)
                self.assertLessEqual(len(fields["description"]), 200, name)
                self.assertGreater(len(fields["description"]), 80, name)
                self.assertTrue(re.fullmatch(r"[a-z0-9-]{1,64}", name))
                self.assertNotIn("claude", name)
                for ch in "<>":
                    self.assertNotIn(ch, fields["description"])
                if ed == "vn":     # the description is Vietnamese
                    self.assertRegex(fields["description"], "[ạảãàáâấầẩẫậăắằẳẵặẹẻẽèéêếềểễệịỉĩìíọỏõòóôốồổỗộơớờởỡợụủũùúưứừửữựỳỷỹýđ]")
                self.assertGreaterEqual(fields["description"].count('"'), 4)     # >= 2 quoted plain trigger phrases
                self.assertEqual(files[f"content-machine/skills/{name}/{file}-{suffix}.md"],
                                 (self.root / "dist" / ed / "Level-ups" / f"{file}-{suffix}.md").read_bytes())
                for anchor in anchors:        # the body points at every part of its file
                    self.assertIn(f"§CM-{anchor}", body, (name, anchor))
        self.assertEqual(sorted(n for n in files if n.startswith("content-machine/agents/")),
                         [f"content-machine/agents/{a}.md" for a in PLUGIN_AGENTS])
        entry = self.manifest["artifacts"]["content-machine-plugin.zip"]
        self.assertEqual(entry["entries"], sorted(files))

    def test_every_plugin_skill_works_from_its_skill_md_alone(self):
        """The founder's v10 run printed "✗ method file (compact mode)": in claude.ai the files next to a SKILL.md are
        not readable without code execution. So each SKILL.md holds its file whole, with every § anchor."""
        with zipfile.ZipFile(self.root / "dist/content-machine-plugin.zip") as zf:
            files = {n: zf.read(n).decode("utf-8") for n in zf.namelist() if n.endswith((".md", ".csv"))}
        sizes = {}
        for ed, suffix in (("en", "EN"), ("vn", "VN")):
            h_method = "METHOD" if ed == "en" else "PHƯƠNG PHÁP"
            jobs = [(f"content-machine-{ed}", f"CONTENT-MACHINE-{suffix}.md", f"{h_method} (CONTENT-MACHINE-{suffix}.md)")]
            jobs += [(f"cm-{area}-{ed}", f"{file}-{suffix}.md", f"FILE ({file}-{suffix}.md)")
                     for area, (file, _) in LEVELUP_AREAS.items()]
            for skill, file, heading in jobs:
                with self.subTest(skill=skill):
                    base = f"content-machine/skills/{skill}"
                    text, whole = files[f"{base}/SKILL.md"], files[f"{base}/{file}"]
                    sizes[skill] = len(text.encode("utf-8"))
                    self.assertEqual(count_line(text, f"## {heading}"), 1)
                    self.assertIn(f"\n## {heading}\n\n{whole.rstrip()}\n", text)       # the file, whole
                    anchors = anchor_headings(whole)
                    self.assertTrue(anchors)
                    for anchor in anchors:                                              # every § anchor of the file
                        self.assertEqual(count_line(text, anchor), 1, anchor)
                    if skill.startswith("content-machine-"):
                        self.assertTrue(text.endswith(whole), "the method closes the main SKILL.md")
        self.assertEqual(self.manifest["artifacts"]["content-machine-plugin.zip"]["skill_md_bytes"],
                         dict(sorted(sizes.items())))                                   # sizes are reported
        warned = {n["note"].split(":")[0] for n in self.manifest["notes"] if "SKILL.md is" in n["note"]}
        self.assertEqual(warned, {f"plugin skill {k}" for k, v in sizes.items() if v > build.PLUGIN_SKILL_MD_WARN})
        for ed, board in (("en", "Campaigns.csv"), ("vn", "Chien-dich.csv")):
            skill = files[f"content-machine/skills/cm-board-{ed}/SKILL.md"]
            for csv_path in sorted((self.root / "dist" / ed / "Level-ups" / "Board").glob("*.csv")):
                row = csv_path.read_text(encoding="utf-8").rstrip()
                self.assertIn(f"### Board/{csv_path.name}\n\n```csv\n{row}\n```", skill, csv_path.name)

    def test_the_setup_check_is_true_in_skill_mode_and_the_one_file_kit_holds_the_method(self):
        with zipfile.ZipFile(self.root / "dist/content-machine-plugin.zip") as zf:
            skills = {ed: zf.read(f"content-machine/skills/content-machine-{ed}/SKILL.md").decode("utf-8")
                      for ed in ("en", "vn")}
        for ed, suffix, h_method in (("en", "EN", "METHOD"), ("vn", "VN", "PHƯƠNG PHÁP")):
            with self.subTest(ed=ed):
                edition = cmlib.load_edition(ed, self.root)
                line = render.render_string("setup.check", edition, "kit")
                text = skills[ed]
                pointer = text.split("---\n\n", 1)[1].split("\n", 1)[0]
                self.assertIn(f"CONTENT-MACHINE-{suffix}.md", pointer)       # the pointer names the file and where it is
                self.assertIn(h_method, pointer)
                self.assertIn(line, text)                                      # the kit's own "✓ method file" check line
                phrase = build.PORTABLE[ed]["check_to"].replace("{{file_suffix}}", suffix).replace("{{h_method}}", h_method)
                swapped_in = phrase in text
                noted = [n for n in self.manifest["notes"] if n["edition"] == ed and "setup-check phrase" in n["note"]]
                self.assertTrue(swapped_in != bool(noted), (ed, "swapped or noted, never neither"))
                # the one-file kit: the instruction block, then the whole method file
                one = (self.root / "dist" / ed / f"CONTENT-MACHINE-{suffix}-1-FILE.md").read_text(encoding="utf-8")
                method = (self.root / "dist" / ed / f"CONTENT-MACHINE-{suffix}.md").read_text(encoding="utf-8")
                self.assertTrue(one.endswith(method))
                self.assertEqual(count_line(one, f"## {h_method}"), 1)
                self.assertEqual(phrase in one, swapped_in)
                for anchor in anchor_headings(method):
                    self.assertEqual(count_line(one, anchor), 1, anchor)

    def test_the_main_skill_pointer_names_the_nine_companions(self):
        with zipfile.ZipFile(self.root / "dist/content-machine-plugin.zip") as zf:
            for ed, suffix in (("en", "EN"), ("vn", "VN")):
                text = zf.read(f"content-machine/skills/content-machine-{ed}/SKILL.md").decode("utf-8")
                first = text.split("---\n\n", 1)[1].split("\n", 1)[0]
                self.assertIn(f"CONTENT-MACHINE-{suffix}.md", first)
                for stem in PLUGIN_SKILLS:
                    self.assertIn(f"{stem}-{ed}", first)
                self.assertIn("Level-ups", first)

    def test_the_kits_level_up_line_names_files_that_exist(self):
        for ed, suffix in (("en", "EN"), ("vn", "VN")):
            kit = (self.root / "dist" / ed / f"CONTENT-MACHINE-{suffix}.md").read_text(encoding="utf-8")
            line = next(ln for ln in kit.splitlines() if "{LAUNCH-" in ln)
            self.assertIn(f"{{LAUNCH-{suffix}.md}}", line)
            self.assertTrue((self.root / "dist" / ed / "Level-ups" / f"LAUNCH-{suffix}.md").is_file())
            self.assertNotIn("GROW", kit)

    def test_the_instruction_block_routes_to_every_level_up_file(self):
        """The kit's LEVEL-UPS line is the router: each level-up file is named there, or a coach never learns it exists."""
        for ed, suffix in (("en", "EN"), ("vn", "VN")):
            kit = (self.root / "dist" / ed / "1-INSTRUCTIONS.txt").read_text(encoding="utf-8")
            line = next(ln for ln in kit.splitlines() if f"RESEARCH-{suffix}.md" in ln)
            for area, (file, _) in LEVELUP_AREAS.items():
                self.assertIn(f"{file}-{suffix}.md", line, (ed, file))
            self.assertLessEqual(cmlib.nfc_len(kit), {"en": 6500, "vn": 7500}[ed], ed)

    def test_the_strategy_and_launch_skills_point_to_the_hook_and_campaign_skills(self):
        with zipfile.ZipFile(self.root / "dist/content-machine-plugin.zip") as zf:
            for ed in ("en", "vn"):
                strategy = zf.read(f"content-machine/skills/cm-strategy-{ed}/SKILL.md").decode("utf-8")
                launch = zf.read(f"content-machine/skills/cm-launch-{ed}/SKILL.md").decode("utf-8")
                self.assertIn("§CM-HOOK-LIBRARY (cm-hooks)", strategy, ed)
                self.assertIn("§CM-CAMPAIGNS (cm-campaigns)", launch, ed)

    def test_claude_plugin_validate_passes(self):
        cli = shutil.which("claude") or "/opt/node22/bin/claude"
        if not Path(cli).exists():
            self.skipTest("the claude CLI is not installed")
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(self.root / "dist/content-machine-plugin.zip") as zf:
                zf.extractall(tmp)
            for target in ("content-machine", "content-machine/skills", "content-machine/agents"):
                done = subprocess.run([cli, "plugin", "validate", str(Path(tmp) / target)], capture_output=True,
                                      text=True, timeout=120)
                self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
                self.assertIn("Validation passed", done.stdout)

    def test_building_the_real_tree_twice_gives_the_same_bytes(self):
        def snapshot():
            return {p.relative_to(self.root).as_posix(): package.file_sha256(p)
                    for p in sorted((self.root / "dist").rglob("*")) if p.is_file() and p.name != "manifest.json"}

        before = snapshot()
        time.sleep(1.1)
        for p in self.root.rglob("*"):
            if p.is_file() and "dist" not in p.parts:
                os.utime(p)
        with contextlib.redirect_stdout(io.StringIO()):
            second = build.build(self.root, ["en", "vn"])
        self.assertEqual(before, snapshot())
        self.assertEqual(second["build_sha256"], self.manifest["build_sha256"])


if __name__ == "__main__":
    unittest.main()
