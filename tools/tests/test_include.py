"""{{>section.id}} includes in the template engine and lint's static walk."""
import os
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import cmlib  # noqa: E402
import lint  # noqa: E402


def make_repo(root: Path) -> None:
    (root / "editions").mkdir()
    (root / "editions" / "en.toml").write_text(textwrap.dedent("""
        [edition]
        id = "en"
        lang = "en"
        skill_name = "content-machine"
        file_suffix = "EN"
        zip_name = "Content-Machine-EN"
        [params]
        currency = "$"
    """))
    (root / "core" / "en").mkdir(parents=True)
    (root / "core" / "en" / "ship-check.md").write_text(textwrap.dedent("""
        <!-- @section ship.kit -->
        SHIP CHECK · {{#if kit}}kit{{else}}other{{/if}} · {{currency}}
        <!-- @section ship.loop -->
        A {{>ship.loop}}
    """))


class IncludeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        make_repo(self.root)
        self.ed = cmlib.load_edition("en", self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_include_renders_with_same_flags(self):
        out = cmlib.render("top\n{{>ship.kit}}\nend", self.ed, "kit")
        self.assertIn("SHIP CHECK · kit · $", out)
        self.assertNotIn("@section", out)
        out = cmlib.render("{{>ship.kit}}", self.ed, "skill")
        self.assertIn("SHIP CHECK · other", out)

    def test_unknown_section_is_an_error(self):
        with self.assertRaises(cmlib.CMError) as cm:
            cmlib.render("{{>ship.nope}}", self.ed, "kit")
        self.assertEqual(cm.exception.code, "E170")

    def test_self_include_stops(self):
        with self.assertRaises(cmlib.CMError) as cm:
            cmlib.render("{{>ship.loop}}", self.ed, "kit")
        self.assertIn("too deep", cm.exception.message)

    def test_lint_static_walk_flags_unknown_include(self):
        probs = lint.template_problems("{{#if vn}}{{>ship.missing}}{{/if}}", self.ed)
        self.assertTrue(any("ship.missing" in m for m, _ in probs))
        self.assertEqual(lint.template_problems("{{>ship.kit}}", self.ed), [])


if __name__ == "__main__":
    unittest.main()
