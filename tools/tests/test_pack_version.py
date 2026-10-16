"""v13.15: the Brand Card's pack_version comes from VERSION through the {{pack_version}} build param,
never from a literal in the sources (a literal went stale at 1.3.10 while the pack shipped 1.3.14)."""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import cmlib  # noqa: E402

SOURCE_DIRS = ("core", "modules", "plugin", "strings", "templates", "automation", "guides", "locales", "schemas")
LITERAL = re.compile(r"pack_version\s*[=:]\s*\d+\.")


class PackVersionTest(unittest.TestCase):
    def test_no_literal_pack_version_in_sources(self):
        hits = []
        for d in SOURCE_DIRS:
            base = ROOT / d
            if not base.exists():
                continue
            for path in sorted(base.rglob("*")):
                if not path.is_file() or path.suffix not in (".md", ".toml", ".tmpl", ".txt", ".csv", ".json"):
                    continue
                for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    if LITERAL.search(line):
                        hits.append(f"{path.relative_to(ROOT)}:{n}")
        self.assertEqual(hits, [], "use {{pack_version}} (filled from VERSION), not a literal")

    def test_param_filled_from_version(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        for ed in ("en", "vn"):
            edition = cmlib.load_edition(ed, ROOT)
            self.assertEqual(edition.params.get("pack_version"), version)

    def test_card_template_uses_param(self):
        for lang in ("en", "vn"):
            text = (ROOT / "modules" / lang / "brain.md").read_text(encoding="utf-8")
            self.assertIn("pack_version={{pack_version}}", text)


if __name__ == "__main__":
    unittest.main()
