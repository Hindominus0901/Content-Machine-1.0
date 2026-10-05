"""Tests for render.py, build.py, package.py and ics.py on a tiny temporary repo."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
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
        write(self.root, f"{rel}/RELEASE-VERDICT.md", "Result: PASS\nScore: 20/20\n")
        write(self.root, f"{rel}/RELEASE-VERDICT.second-read.md", "Result: PASS\n")
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


if __name__ == "__main__":
    unittest.main()
