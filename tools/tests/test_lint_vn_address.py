"""E147 (tools/lint.py): a bare "bạn" in a VN coach-facing line must fail lint (v13.5, founder: no "bạn" for an
anh/chị coach). Each test plants one bad line in the small valid repo of test_lint_fixtures and asserts E147; the
look-alikes (quoted samples, {…} slots, the pair notation, "bạn bè", buyer-facing strings) stay clean."""
from __future__ import annotations

import unittest

from test_lint_fixtures import LintCase, VN_PROSE


def e147(report) -> list[str]:
    return [str(f) for f in report.errors if f.code == "E147"]


class BareBanInVnCoachLines(LintCase):
    def test_planted_bare_ban_in_a_vn_string(self):
        self.repo.set_string("en", "card.stop_lines", "That's today done. This card is how I remember you.")
        self.repo.set_string("vn", "card.stop_lines", "Hôm nay xong rồi. Có tấm card này mình mới nhớ được bạn.")
        self.assertCatches("E147", where="strings/vn.toml")

    def test_planted_needs_tag_in_a_vn_string(self):
        self.repo.set_string("en", "needs.tag", "[NEEDS: {question}]")
        self.repo.set_string("vn", "needs.tag", "[CẦN BẠN: {question}]")
        self.assertCatches("E147", where="strings/vn.toml")

    def test_planted_bare_ban_in_the_vn_instruction_block(self):
        body = VN_PROSE["core/vn/start-block.md"][0][2].replace(
            "SHIP CHECK", "Dòng cuối: hỏi bạn một câu.\nSHIP CHECK")
        self.repo.set_section("vn", "core/vn/start-block.md", "start.core", body)
        self.assertCatches("E147", where="core/vn/start-block.md")

    def test_planted_markers_in_a_vn_module(self):
        for planted in ("Thiếu số thì ghi [CẦN BẠN: …].", "Hỏi: giờ [anh/chị] thấy khó nhất chỗ nào?",
                        "Lưu khung vào Bài bạn thích."):
            with self.subTest(planted=planted):
                self.repo.set_section("vn", "modules/vn/talk.md", "talk.core",
                                      f"### Buổi nói chuyện tuần\nHỏi năm câu. {planted}")
                self.assertCatches("E147", where="modules/vn/talk.md")

    def test_planted_needs_tag_in_a_buyer_facing_vn_string(self):
        self.repo.set_string("en", "cta.default", "DM me WORD. [NEEDS: the start date]")
        self.repo.set_string("vn", "cta.default", "Nhắn mình chữ KHOA. [CẦN BẠN: ngày khai giảng]")
        self.assertCatches("E147", where="strings/vn.toml")

    def test_planted_needs_tag_outside_the_sections(self):
        for rel in ("plugin/agents/cm-listener.md", "plugin/companions.toml", "automation/task-nudge.tmpl"):
            with self.subTest(rel=rel):
                self.repo.write(rel, "A missing fact is [NEEDS: …] ([CẦN BẠN: …]).\n")
                self.assertCatches("E147", where=rel)
                self.repo.write(rel, "A missing fact is [NEEDS: …] ([CẦN {XƯNG HÔ}: …]).\n"
                                     "Never [CẦN BẠN: …] for an anh/chị coach. <!-- lint-ok: E147 -->\n")
                self.assertEqual(e147(self.repo.lint()), [])
                (self.repo.root / rel).unlink()

    def test_slots_quotes_pairs_and_friends_are_clean(self):
        self.repo.set_string("en", "card.stop_lines", "That's today done. This card is how I remember you.")
        self.repo.set_string("vn", "card.stop_lines", "Có tấm card này {tự xưng} mới nhớ được {xưng hô}, gửi bạn bè cũng được.")
        self.repo.set_string("en", "needs.tag", "[NEEDS: {question}]")
        self.repo.set_string("vn", "needs.tag", "[CẦN {XƯNG HÔ}: {question}]")
        self.repo.set_string("en", "ask3.question", "When you first found me, what were you stuck on?")
        self.repo.set_string("vn", "ask3.question", "Hồi mới tìm đến mình, bạn đang loay hoay nhất chuyện gì?")
        body = VN_PROSE["core/vn/start-block.md"][0][2].replace(
            "SHIP CHECK", 'XƯNG HÔ: trả lời 1 xưng mình–bạn, hỏi "gọi bạn là anh, chị hay bạn?"; bạn → mình–bạn; '
                          'kết bạn Zalo. {xưng hô}\nSHIP CHECK')
        self.repo.set_section("vn", "core/vn/start-block.md", "start.core", body)
        self.repo.set_section("vn", "modules/vn/talk.md", "talk.core",
                              "### Buổi nói chuyện tuần\nHỏi năm câu; thiếu thì [CẦN {XƯNG HÔ}: …], bạn bè của khách.")
        self.assertEqual(e147(self.repo.lint()), [])

    def test_waiver_covers_a_line(self):
        body = VN_PROSE["core/vn/start-block.md"][0][2].replace(
            "SHIP CHECK", "Dòng cuối: hỏi bạn một câu. <!-- lint-ok: E147 -->\nSHIP CHECK")
        self.repo.set_section("vn", "core/vn/start-block.md", "start.core", body)
        self.assertEqual(e147(self.repo.lint()), [])


if __name__ == "__main__":
    unittest.main()
