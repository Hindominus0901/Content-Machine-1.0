"""Params as printed in edition text: a float takes the edition's decimal separator (VN 3,5; EN 3.5)."""
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import cmlib  # noqa: E402

REPO = Path(__file__).resolve().parent.parent.parent


def make_edition(root: Path, ed: str, extra_cfg: str = "") -> cmlib.Edition:
    (root / "editions").mkdir(exist_ok=True)
    (root / "editions" / f"{ed}.toml").write_text(textwrap.dedent(f"""
        [edition]
        id = "{ed}"
        lang = "{ed}"
        skill_name = "cm-{ed}"
        file_suffix = "{ed.upper()}"
        zip_name = "CM-{ed.upper()}"
        {extra_cfg}
        [params]
        word_rate = 3.5
        quote_cap = 25
        money_example = "1.500.000đ"
        launch_default_days = 14
        whole_rate = 2.0
    """), encoding="utf-8")
    return cmlib.load_edition(ed, root)


class DecimalSeparatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_vn_floats_take_a_decimal_comma(self):
        ed = make_edition(self.root, "vn")
        self.assertEqual(ed.decimal_sep, ",")
        out = cmlib.render("{{word_rate}} tiếng mỗi giây · {{whole_rate}}", ed, "kit")
        self.assertEqual(out, "3,5 tiếng mỗi giây · 2,0\n")

    def test_en_floats_keep_the_dot(self):
        ed = make_edition(self.root, "en")
        self.assertEqual(ed.decimal_sep, ".")
        self.assertEqual(cmlib.render("{{word_rate}} words per second", ed, "kit"), "3.5 words per second\n")

    def test_integers_and_strings_are_unchanged(self):
        ed = make_edition(self.root, "vn")
        out = cmlib.render("{{quote_cap}} · {{launch_default_days}} · {{money_example}}", ed, "kit")
        self.assertEqual(out, "25 · 14 · 1.500.000đ\n")

    def test_edition_can_set_its_own_separator(self):
        ed = make_edition(self.root, "en", 'decimal_sep = ","')
        self.assertEqual(cmlib.render("{{word_rate}}", ed, "kit"), "3,5\n")

    def test_the_real_vn_edition_prints_its_word_rate_with_a_comma(self):
        ed = cmlib.load_edition("vn", REPO)
        rate = ed.params["word_rate"]
        self.assertIsInstance(rate, float)
        self.assertEqual(cmlib.render("{{word_rate}}", ed, "kit"), str(rate).replace(".", ",") + "\n")
        en = cmlib.load_edition("en", REPO)
        self.assertEqual(cmlib.render("{{word_rate}}", en, "kit"), str(en.params["word_rate"]) + "\n")


if __name__ == "__main__":
    unittest.main()
