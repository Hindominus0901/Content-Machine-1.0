"""E148 (tools/lint.py): a test persona's own facts must not appear in kit sources (v13.8, COMPARE v13.7 new defect 1:
the v13.7 kit's hook examples were built from the sales-coach fixture, "14 lên 33 lịch hẹn", "10 năm làm sale",
ĐỂ CHỊ SUY NGHĨ, so a demo run could not tell thinking from copying). The curated list is
evals/personas/leak-terms.toml. Planted tests use the small valid repo of test_lint_fixtures; the last class checks
the real list against the real fixtures and the real kit sources."""
from __future__ import annotations

import sys
import tomllib
import unittest
import unicodedata
from pathlib import Path

from test_lint_fixtures import LintCase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import cmlib  # noqa: E402
import lint  # noqa: E402

TERMS = """[sales-coach]
fixture = "evals/personas/vn/sales-coach"
terms = ["chị Trâm", "112 tin", "10 năm làm sale"]
echoes = ["14 lên 33", "Tram's spa"]
"""


def e148(report) -> list[str]:
    return [str(f) for f in report.errors if f.code == "E148"]


class PlantedPersonaFacts(LintCase):
    def setUp(self) -> None:
        super().setUp()
        self.repo.write(lint.LEAK_TERMS_FILE, TERMS)

    def test_no_terms_file_means_no_check(self):
        (self.repo.root / lint.LEAK_TERMS_FILE).unlink()
        self.repo.set_section("vn", "modules/vn/talk.md", "talk.core",
                              "### Buổi nói chuyện tuần\nVí dụ: \"Một spa từ 14 lên 33 lịch hẹn mỗi tháng.\"")
        self.assertEqual(e148(self.repo.lint()), [])

    def test_term_in_a_vn_module_section(self):
        self.repo.set_section("vn", "modules/vn/talk.md", "talk.core",
                              "### Buổi nói chuyện tuần\nVí dụ: \"Một spa từ 14 lên 33 lịch hẹn mỗi tháng.\"")
        self.assertCatches("E148", where="modules/vn/talk.md")

    def test_term_in_an_en_core_section_and_an_echo(self):
        self.repo.set_section("en", "core/en/start-block.md", "start.core",
                              "{{t:contract.output}}\n### Start\nNever insider detail (\"112 tin, Tram's spa\").\n"
                              "SHIP CHECK · silent · once per batch\n{{t:contract.output}}")
        found = e148(self.repo.lint())
        self.assertTrue(any("112 tin" in f for f in found) and any("Tram's spa" in f for f in found), found)

    def test_term_in_a_string_and_in_plugin(self):
        self.repo.set_string("en", "card.stop_lines", "That's today done.")
        self.repo.set_string("vn", "card.stop_lines", "Xong hôm nay. Như chị Trâm nè.")
        self.assertCatches("E148", where="strings/vn.toml key 'card.stop_lines'")
        self.repo.set_string("vn", "card.stop_lines", "Xong hôm nay.")
        self.repo.write("plugin/agents/cm-writer.md", "The bar: \"10 NĂM LÀM SALE, mình sửa một chỗ.\"\n")
        self.assertCatches("E148", where="plugin/agents/cm-writer.md:1")

    def test_word_edges_and_waiver(self):
        self.repo.set_section("vn", "modules/vn/talk.md", "talk.core",
                              "### Buổi nói chuyện tuần\n1112 tin nhắn, 214 lên 330 khách, chị Trâmy.\n"
                              "Lịch sử lỗi: \"14 lên 33\" từng là ví dụ. <!-- lint-ok: E148 -->")
        self.assertEqual(e148(self.repo.lint()), [])


class RealListAndKit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = tomllib.loads((ROOT / lint.LEAK_TERMS_FILE).read_text(encoding="utf-8"))

    def test_every_term_is_in_its_fixture(self):
        missing = []
        for persona, block in self.data.items():
            folder = ROOT / block["fixture"]
            self.assertTrue(folder.is_dir(), f"{persona}: {folder} is not a fixture folder")
            text = unicodedata.normalize("NFC", "\n".join(
                p.read_text(encoding="utf-8") for p in sorted(folder.iterdir()) if p.is_file())).lower()
            missing += [f"{persona}: {t}" for t in block["terms"]
                        if unicodedata.normalize("NFC", t).lower() not in text]
        self.assertEqual(missing, [], "terms no longer in their fixture (rewrite or drop them)")

    def test_every_fixture_folder_has_a_block(self):
        listed = {block["fixture"] for block in self.data.values()}
        folders = {p.parent.relative_to(ROOT).as_posix() for p in (ROOT / "evals/personas").glob("*/*/persona.toml")}
        self.assertEqual(sorted(folders - listed), [])

    def test_kit_sources_carry_no_persona_fact(self):
        terms = lint.load_leak_terms(ROOT)
        hits = []
        texts = []
        for top in ("core", "modules"):
            for path in sorted((ROOT / top).rglob("*.md")):
                _, secs = cmlib.parse_sections(path.read_text(encoding="utf-8"), str(path))
                texts += [(f"{path.relative_to(ROOT)} {s.id}", s.body) for s in secs]
        for path in sorted((ROOT / "strings").glob("*.toml")) + sorted((ROOT / "plugin").rglob("*")):
            if path.is_file() and path.suffix in (".md", ".toml", ".json", ".txt"):
                texts.append((str(path.relative_to(ROOT)), path.read_text(encoding="utf-8")))
        for where, text in texts:
            for line in cmlib.nfc(text).splitlines():
                if lint.waived(line, "E148"):
                    continue
                hits += [f"{where}: {term} ({persona})" for persona, term, rx in terms if rx.search(line)]
        self.assertEqual(hits, [])


if __name__ == "__main__":
    unittest.main()
