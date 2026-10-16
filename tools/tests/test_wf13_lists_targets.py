"""wf13 P1 patch data on the real repo files: deny-lists, stock phrases, targets, acceptance.

docs/research/wf13-inspiration-spec.md §1 (words the coach never sees), §4 (DISTANCE),
§6 (QA) and §7 (P1 patch). Standard library only.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(REPO / "evals"))

import cmlib  # noqa: E402
import graders  # noqa: E402

# Coach-visible text that must hit each edition's deny-list, and text that must not.
DENY_HITS = ["Saved to your swipe file.", "Saved to the swipe file", "That one was an outlier.",
             "Its outlier ratio is 8.", "a views ratio of 3", "their median views", "a proven shape",
             "it passed the same-feed test", "the white space in your niche", "from social listening",
             "the VoC drip", "LIKED: wrong-fix · list", "W-12", "O-3", "R-1", "K-2", "I-4", "C-9", "A-1", "B-5",
             "V-1", "S-2", "P-3", "X-9"]
DENY_MISSES = ["Saved to Posts you like.", "I liked that one.", "about 6× their usual", "W-", "the median",
               "proven", "Your angle"]
VN_HITS = ["trung vị", "lượt xem trung vị của họ", "tỉ lệ vượt", "tỷ lệ vượt 6 lần", "lưu vào file swipe", "VOC"]
VN_MISSES = ["Bài bạn thích", "vóc dáng", "giữ voc dang", "Góc nhìn riêng", "tỉ lệ vượt qua kỳ thi",
             "tỷ lệ vượt trội", "tỉ lệ vượt chỉ tiêu của đội sale", "món miền Trung vị cay", "tập trung vị trí"]

NEW_LIMITS = {
    "claude_social_links_blocked", "chatgpt_social_link_read", "youtube_link_transcript_in_chat",
    "chatgpt_free_image_counts_as_upload", "vn_screenshot_ocr_ok", "grid_counts_legible_phone",
    "vn_count_format_parse", "share_sheet_new_chat", "comment_name_echo_chatgpt", "copy_run_baseline",
    "browse_profile_listing",
}
RELEASE_BLOCKING = {"chatgpt_free_image_counts_as_upload", "vn_screenshot_ocr_ok", "copy_run_baseline"}


class DenyListsCoverLikedWords(unittest.TestCase):
    def terms(self, lang: str):
        return graders.load_term_list(REPO / "locales" / lang / "deny-list.txt")

    def hits(self, terms, text: str) -> list[str]:
        return [label for label, pattern in terms if pattern.search(cmlib.nfc(text))]

    def test_research_words_and_every_bank_id_are_denied(self):
        for lang in cmlib.EDITIONS:
            terms = self.terms(lang)
            for text in DENY_HITS + (VN_HITS if lang == "vn" else []):
                with self.subTest(lang=lang, hit=text):
                    self.assertTrue(self.hits(terms, text), f"{lang} deny-list misses {text!r}")

    def test_plain_coach_words_pass(self):
        for lang in cmlib.EDITIONS:
            terms = self.terms(lang)
            for text in DENY_MISSES + (VN_MISSES if lang == "vn" else []):
                with self.subTest(lang=lang, miss=text):
                    self.assertEqual(self.hits(terms, text), [], f"{lang} deny-list flags {text!r}")


class StockPhrases(unittest.TestCase):
    WANTED = {
        "en": ["let me know in the comments", "link in bio", "comment below", "follow for more"],
        "vn": ["comment bên dưới", "link ở bio", "nhắn tin cho mình", "theo dõi để xem phần 2"],
    }

    def phrases(self, lang: str) -> list[str]:
        text = (REPO / "locales" / lang / "stock-phrases.txt").read_text(encoding="utf-8")
        return [line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("#")]

    def test_lists_hold_the_common_calls_to_action(self):
        for lang, wanted in self.WANTED.items():
            phrases = [cmlib.nfc(p).lower() for p in self.phrases(lang)]
            for phrase in wanted:
                with self.subTest(lang=lang, phrase=phrase):
                    self.assertIn(cmlib.nfc(phrase).lower(), phrases)

    def test_entries_are_plain_unique_phrases(self):
        for lang in cmlib.EDITIONS:
            phrases = self.phrases(lang)
            self.assertTrue(phrases, lang)
            self.assertEqual(len(phrases), len({p.lower() for p in phrases}), f"{lang}: a phrase repeats")
            for p in phrases:
                with self.subTest(lang=lang, phrase=p):
                    self.assertFalse(p.startswith("re:"), "stock phrases are plain text")
                    self.assertEqual(p, cmlib.nfc(p))


class TargetsForLikedPosts(unittest.TestCase):
    def setUp(self):
        self.targets = cmlib.load_toml(REPO / "platform" / "targets.toml")

    def test_the_eleven_limits_are_there(self):
        limits = self.targets["limits"]
        self.assertLessEqual(NEW_LIMITS, set(limits))
        blocking = {n for n in NEW_LIMITS if limits[n].get("release_blocking")}
        self.assertEqual(blocking, RELEASE_BLOCKING)
        data = limits["claude_social_links_blocked"]
        self.assertEqual((data["evidence"], data["verified_on"]), ("DATA", "2026-10-05"))
        self.assertIn("wf13-platform-facts", data["source"])
        for name in NEW_LIMITS - {"claude_social_links_blocked"}:
            with self.subTest(limit=name):
                self.assertEqual((limits[name]["evidence"], limits[name]["verified_on"]), ("VERIFY", ""))

    def test_brand_card_budget_rises_and_visible_stays(self):
        budgets = self.targets["budgets"]
        self.assertEqual((budgets["brand_card"]["en"], budgets["brand_card"]["vn"]), (5700, 6600))
        # wf13 kept the visible part at 900; wf15-simple-surface-spec §4 then cut it to a 3-line top ≤500.
        self.assertEqual((budgets["brand_card_visible"]["en"], budgets["brand_card_visible"]["vn"]), (500, 500))


class AcceptanceForLikedPosts(unittest.TestCase):
    def test_copy_thresholds_and_case_minimum(self):
        acc = cmlib.load_toml(REPO / "evals" / "acceptance.toml")
        self.assertEqual(acc["copy"], {"en_words": 6, "vn_tieng": 8, "false_hit_max": 0.01,
                                       "same_post_yes_max": 0.05})
        self.assertGreaterEqual(acc["cases"]["liked_min"], acc["cases"]["per_module_min"])


if __name__ == "__main__":
    unittest.main()
