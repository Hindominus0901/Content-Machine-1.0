"""Tests for tools/cmcore/checks.py (EN + VN) and the runtime lint tools/shiplint.py."""
from __future__ import annotations

import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import shiplint  # noqa: E402
from cmcore import checks as ck  # noqa: E402


def raws(text: str) -> list[str]:
    return [n.raw for n in ck.numbers_in(text) if not n.structural]


class CountTests(unittest.TestCase):
    def test_words_and_tieng(self):
        self.assertEqual(ck.count_words("You're not too old — you're too vague."), 7)
        self.assertEqual(ck.count_tieng("Bán thì đắt mà cuối tháng không thấy tiền đâu?"), 10)
        self.assertEqual(ck.count_words("  · · $2,400  "), 1)

    def test_nfd_input_counts_like_nfc(self):
        nfd = "lãi ảo"            # "lãi ảo" typed with combining marks
        self.assertEqual(ck.nfc(nfd), "lãi ảo")
        self.assertEqual(ck.keyword_count(nfd, "lãi ảo"), 1)


class NumberTests(unittest.TestCase):
    def test_vn_money_forms(self):
        nums = {n.raw: n for n in ck.numbers_in("Giá 1.990.000đ, hoặc 1,99tr; ship 99k; lãi 4,99 triệu; 1,2 tỷ")}
        self.assertEqual(nums["1.990.000đ"].value, 1_990_000)
        self.assertEqual(nums["1.990.000đ"].kind, "money")
        self.assertEqual(nums["1,99tr"].value, 1_990_000)
        self.assertEqual(nums["99k"].value, 99_000)
        self.assertEqual(nums["4,99 triệu"].value, 4_990_000)
        self.assertEqual(nums["1,2 tỷ"].value, 1_200_000_000)

    def test_en_money_percent_and_suffixes(self):
        nums = {n.raw: n for n in ck.numbers_in("$2,400 or 30% or 90 percent; women 45+ in their 40s")}
        self.assertEqual(nums["$2,400"].value, 2400)
        self.assertTrue(nums["30%"].percent)
        self.assertTrue(nums["90 percent"].percent)
        self.assertIn("45+", nums)
        self.assertIn("40s", nums)

    def test_times_dates_ranges(self):
        kinds = {n.raw: n.kind for n in ck.numbers_in("Closes 11:59, 23h59, 20h on 02/12/2026 (2026-10-05); 2–3 tháng")}
        self.assertEqual(kinds["11:59"], "time")
        self.assertEqual(kinds["23h59"], "time")
        self.assertEqual(kinds["02/12/2026"], "date")
        self.assertEqual(kinds["2026-10-05"], "date")
        self.assertEqual([r for r in raws("2–3 tháng")], ["2", "3"])

    def test_labels_ids_and_tags_are_not_claims(self):
        text = "1. Beat 2: N2 cites P-3 and B2B (≤12 words)\n2) Week 1 · $249 (my guess) [NEEDS: 30% or not?]"
        claims = [n.raw for n in ck.numbers_in(text) if not n.structural and not n.tagged]
        self.assertEqual(claims, [])

    def test_unsupported_numbers(self):
        allowed = ["11", "$2,400", "6 năm", "40 triệu", "8%", "11:59"]
        self.assertEqual(ck.unsupported_numbers("11 clients paid $2,400; closes 11:59", allowed), [])
        self.assertEqual(ck.unsupported_numbers("90% of clients; Pam got $15,000 more", allowed), ["90%", "$15,000"])
        self.assertEqual(ck.unsupported_numbers("Lãi 40tr sau 6 năm, đơn giảm 8%", allowed), [])
        self.assertEqual(ck.unsupported_numbers("đơn giảm 8 khách", ["8%"]), ["8"])     # a percent is not a count


class QuoteTests(unittest.TestCase):
    def test_quotes_and_attribution(self):
        quotes = ck.quotes_in('Lorraine said, “the best trade I ever made.” Say "fix N2". '
                              'Ngân nhắn "chị ơi hóa ra em toàn lãi ảo"', "vn")
        self.assertEqual([(q.text, q.attributed) for q in quotes],
                         [("the best trade I ever made.", True), ("fix N2", False),
                          ("chị ơi hóa ra em toàn lãi ảo", True)])

    def test_instructions_are_not_attributed_quotes(self):
        for text, lang in (('Cần bạn · Hôm đó chị ấy nói gì? (Hoặc nhắn "bỏ qua".)', "vn"),
                           ('Bạn gõ "tiếp" nhé. Mình sẽ gửi "bản nháp" sau.', "vn"),
                           ('Draft · the stance is soft. Say "fix N2" and I\'ll sharpen it.', "en"),
                           ('Comment "CHAPTER" and text me "coffee".', "en")):
            self.assertEqual([q.attributed for q in ck.quotes_in(text, lang)], [False] * len(ck.quotes_in(text, lang)),
                             text)
        self.assertTrue(ck.quotes_in('Chị Lan nói "mệt quá"', "vn")[0].attributed)
        self.assertTrue(ck.quotes_in('Một chị học viên kể "em toàn lãi ảo"', "vn")[0].attributed)

    def test_quote_ok(self):
        sources = ["Calls it 'the best trade I ever made'.", "Chị ơi hóa ra em toàn lãi ảo"]
        self.assertTrue(ck.quote_ok("The best trade I ever made!", sources, 15))
        self.assertTrue(ck.quote_ok("chị ơi, hóa ra em toàn lãi ảo", sources, 25, "vn"))
        self.assertFalse(ck.quote_ok("the best decision I ever made", sources, 15))
        long_quote = " ".join(["word"] * 16)
        self.assertIn("cap 15", ck.quote_problem(long_quote, [long_quote], 15))
        self.assertIsNone(ck.quote_problem(" ".join(["tiếng"] * 25), [" ".join(["tiếng"] * 25)], 25, "vn"))


class HookKeywordPraiseTests(unittest.TestCase):
    def test_hedges(self):
        self.assertEqual(ck.hedges_in_hook("Maybe you're not too old. I think you're vague.", "en"),
                         ["maybe", "I think"])
        self.assertEqual(ck.hedges_in_hook("Có lẽ chị đang lãi ảo", "vn"), ["có lẽ"])
        self.assertEqual(ck.hedges_in_hook("You're not too old. You're too vague.", "en"), [])
        self.assertEqual(ck.hedges_in_hook("Mightily", "en"), [])

    def test_keyword_count_en(self):
        self.assertEqual(ck.keyword_count("Comment CHAPTER. chapter? Chapters don't count.", "CHAPTER"), 2)
        self.assertEqual(ck.keyword_count("one more chapter", "one more chapter"), 1)

    def test_keyword_count_vn_without_diacritics(self):
        text = "Lãi ảo là gì? Comment lai ao. Đừng lại áo nhé. LÃI ẢO"
        self.assertEqual(ck.keyword_count(text, "lãi ảo"), 3)                    # "lại áo" is another word
        self.assertEqual(ck.keyword_count("nhắn DANG KY ngay", "ĐĂNG KÝ"), 1)
        self.assertEqual(ck.keyword_count("đăng kí ngay", "đăng ký", ["đăng kí"]), 1)

    def test_hook_stem(self):
        self.assertEqual(ck.hook_stem("Here's the thing nobody tells you!"), "thing nobody tells")
        self.assertEqual(ck.hook_stem("“Is it too late for me?” she asked."), "late asked")
        self.assertEqual(ck.hook_stem("Chị ơi, bán thì đắt mà cuối tháng không thấy tiền"), "bán đắt cuối")

    def test_praise(self):
        self.assertEqual(ck.praise_words("Great answer! Love this story.", "en"), ["great", "love this"])
        self.assertEqual(ck.praise_words("Tuyệt vời chị ơi, xuất sắc", "vn"), ["tuyệt vời", "xuất sắc"])
        self.assertEqual(ck.praise_words("Here is your script.", "en"), [])


class UrgencyBracketTests(unittest.TestCase):
    def test_urgency_lines_en(self):
        text = "Only 2 spots left\nthe only way out\nmy last day at HQ\nCart closes Friday\nToday only: $95"
        self.assertEqual(ck.urgency_lines(text, "en"), ["Only 2 spots left", "Cart closes Friday", "Today only: $95"])

    def test_urgency_lines_vn(self):
        text = "Chỉ còn 3 suất\nđóng đơn mỗi tối\nđóng cổng lúc 23h59\nHạn chót 30/11\nCòn 2 ngày"
        self.assertEqual(ck.urgency_lines(text, "vn"),
                         ["Chỉ còn 3 suất", "đóng cổng lúc 23h59", "Hạn chót 30/11", "Còn 2 ngày"])

    def test_needs_brackets(self):
        self.assertEqual(ck.needs_brackets("a [NEEDS: her words] b [CẦN BẠN: số đơn] c [CẦN CHỊ: giá] [guess]"),
                         ["[NEEDS: her words]", "[CẦN BẠN: số đơn]", "[CẦN CHỊ: giá]"])
        self.assertEqual(ck.needs_brackets("unclosed [NEEDS: what she said"), ["[NEEDS: what she said"])

    def test_ready_with_open_bracket(self):
        self.assertTrue(ck.ready_with_open_bracket("**Ready to film** · I'd post it: CHAPTER", "x [NEEDS: y]"))
        self.assertTrue(ck.ready_with_open_bracket("Sẵn sàng quay · Mình sẽ đăng: lãi ảo", "[CẦN BẠN: giá]"))
        self.assertTrue(ck.ready_with_open_bracket("✓ Checked: one idea", "[NEEDS: proof]"))
        self.assertFalse(ck.ready_with_open_bracket("Needs you · What did she say?", "[NEEDS: y]"))
        self.assertFalse(ck.ready_with_open_bracket("Ready to post · I'd post it: CHAPTER", "clean text"))
        self.assertEqual(ck.conditional_ready("Ready after one fix"), ["Ready after"])


class ClassTests(unittest.TestCase):
    LONG = " ".join(["word"] * 45)

    def test_classes_by_format(self):
        self.assertEqual(ck.output_class("x", "Message Map", "en"), "Structured")
        self.assertEqual(ck.output_class("x", "hook options", "en"), "Idea")
        self.assertEqual(ck.output_class(self.LONG, "offer post", "en"), "Script-claims")
        self.assertEqual(ck.output_class(self.LONG, "background_text", "en"), "Micro")

    def test_classes_by_text(self):
        self.assertEqual(ck.output_class("Only 2 spots left. DM me.", "text-post", "en"), "Micro")
        self.assertEqual(ck.output_class(self.LONG, "native-short", "en"), "Script")
        self.assertEqual(ck.output_class(self.LONG + " 11 paying clients", "native-short", "en"), "Script-claims")
        self.assertEqual(ck.output_class(self.LONG + " the only way", "native-short", "en"), "Script")
        vn = " ".join(["chữ"] * 70)
        self.assertEqual(ck.output_class(vn, "native-short", "vn"), "Script")
        self.assertEqual(ck.output_class(vn + " chỉ còn 3 suất", "native-short", "vn"), "Script-claims")
        self.assertEqual(ck.output_class(vn + " shop tốt nhất", "native-short", "vn"), "Script-claims")
        self.assertEqual(ck.output_class(" ".join(["chữ"] * 50), "native-short", "vn"), "Micro")

    def test_result_claims_and_names(self):
        text = "11 paying clients in 2 years\n12 weeks, $2,400\n30% off today\nLorraine got hired in 11 weeks"
        self.assertEqual(ck.result_claims(text, "en"), ["11 paying clients in 2 years", "Lorraine got hired in 11 weeks"])
        self.assertEqual(ck.result_claims("Ngân lãi thật 21 triệu một tháng\nKhóa 6 tuần", "vn"),
                         ["Ngân lãi thật 21 triệu một tháng"])
        self.assertEqual(ck.names_in("My client Lorraine, 54, said yes. On Monday said nothing.", "en"), ["Lorraine"])
        self.assertEqual(ck.names_in("chị Lan và em Ngân nói", "vn"), ["Lan", "Ngân"])

    def test_budgets(self):
        self.assertEqual(ck.budget_problems("bg-post", "", "x" * 140, "en"), ["140 characters (max 130)"])
        self.assertEqual(ck.budget_problems("drop", "", "w " * 121, "en"), ["121 words (max 120)"])
        hook = " ".join(["w"] * 13)
        self.assertEqual(ck.budget_problems("native-short", hook, "", "en"), ["hook 13 words (max 12)"])
        self.assertEqual(ck.budget_problems("native-short", hook, "", "vn"), [])          # 18 tiếng in VN
        self.assertEqual(ck.budget_problems("short", "", "w " * 75, "en", seconds=30), [])
        self.assertEqual(ck.budget_problems("short", "", "w " * 100, "en", seconds=30), ["100 words (max 86)"])


# ---------------------------------------------------------------- shiplint

BATCH = {
    "lang": "en",
    "keyword": "CHAPTER",
    "allowed_numbers": ["$2,400"],
    "allowed_names": ["Dana"],
    "bank": [
        {"id": "P-1", "text": "Lorraine, 54: job offer in 11 weeks. Calls it 'the best trade I ever made'.",
         "substantiated": True, "consent": True, "uses": ["posts", "case-study"]},
        {"id": "P-5", "text": "About 90 percent of my people end up somewhere better.",
         "substantiated": False, "consent": False},
        {"id": "S-1", "text": "24 years at HQ, restructured out at 48; 63 applications in 7 months, 2 interviews."},
    ],
    "ledger": [{"id": "L-1", "cap": 4, "deadline": "2027-01-20", "enforced": False}],
    "recent_hook_stems": ["old start"],
    "pieces": [
        {"id": "N1", "format": "native-short", "hook": "Sixty-three applications. Two interviews.",
         "body": "That was me at 48 after 24 years at HQ. Then I stopped applying and started having coffee. "
                 "Comment CHAPTER and I'll send you the coffee script.",
         "cites": ["S-1"], "verdict_line": "Ready to film · I'd post it: your 63 applications and CHAPTER."},
        {"id": "N2", "format": "text-post", "hook": "Maybe you're not too old.",
         "body": "90% of my clients land a job in 12 weeks. Pam got a $15,000 raise. Only 2 spots left. "
                 "CHAPTER chapter",
         "cites": ["P-5"], "verdict_line": "Ready to post · I'd post it: [NEEDS: a real number]"},
        {"id": "N3", "format": "native-short", "hook": "Not too old to start",
         "body": 'Lorraine said "the best decision I ever made" and meant it. Comment CHAPTER.',
         "cites": ["P-1", "X-9"], "verdict_line": "Ready to film · I'd post it: Lorraine's words."},
        {"id": "N4", "format": "ad", "hook": "Eleven weeks to an offer.",
         "body": "Lorraine got the offer in 11 weeks. Comment CHAPTER.",
         "cites": ["P-1"], "verdict_line": "Ready to post · written as a case story."},
    ],
}


class ShiplintTests(unittest.TestCase):
    def run_main(self, *args, stdin: str | None = None) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        old_stdin = sys.stdin
        try:
            if stdin is not None:
                sys.stdin = io.StringIO(stdin)
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = shiplint.main(list(args))
        finally:
            sys.stdin = old_stdin
        return code, out.getvalue(), err.getvalue()

    def lines(self) -> dict[str, str]:
        code, out, _ = self.run_main("-", stdin=json.dumps(BATCH))
        self.assertEqual(code, 0)
        return {line.split(" ", 1)[0]: line for line in out.strip().splitlines()}

    def test_clean_piece_passes(self):
        self.assertEqual(self.lines()["N1"], "N1 PASS")

    def test_known_defects_are_named(self):
        n2 = self.lines()["N2"]
        self.assertTrue(n2.startswith("N2 FAIL: "), n2)
        for defect in ('number "$15,000" not in cited rows', 'name "Pam" not in cited rows',
                       "Ready with an open [NEEDS]", "result claim without a Substantiated+consent P-row",
                       'urgency without an enforced Ledger row: "Only 2 spots left."', "keyword ×2",
                       'hedge in hook: "maybe"'):
            self.assertIn(defect, n2)

    def test_quote_ids_and_hook_stem(self):
        n3 = self.lines()["N3"]
        self.assertIn("cited ID does not resolve: X-9", n3)
        self.assertIn('quote not verbatim in the sources: "the best decision I ever made"', n3)
        self.assertIn('hook stem "old start" used recently', n3)

    def test_ad_needs_ads_consent(self):
        self.assertIn("result claim without a Substantiated+consent P-row", self.lines()["N4"])

    def test_json_output_has_class(self):
        code, out, _ = self.run_main("-", "--json", stdin=json.dumps(BATCH))
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual([d["id"] for d in data], ["N1", "N2", "N3", "N4"])
        self.assertEqual(data[0]["result"], "PASS")
        self.assertIn(data[0]["class"], ("Micro", "Script", "Script-claims"))

    def test_vn_batch(self):
        batch = {"lang": "vn", "keyword": "lãi ảo",
                 "bank": [{"id": "P-1", "text": "Em Ngân: lãi thật 9 triệu, 3 tháng sau 21 triệu một tháng.",
                           "substantiated": True, "consent": True, "uses": ["posts"]}],
                 "pieces": [{"id": "N1", "format": "native-short", "hook": "Bán đắt mà vẫn lai ao?",
                             "body": "Em Ngân từ lãi 9tr lên 21tr một tháng sau 3 tháng.", "cites": ["P-1"],
                             "verdict_line": "Sẵn sàng quay · Mình sẽ đăng: chuyện của Ngân."},
                            {"id": "N2", "format": "native-short", "hook": "Có lẽ chị đang lãi ảo",
                             "body": "Chỉ còn 3 suất. Lãi gấp đôi sau 30 ngày.", "cites": [],
                             "verdict_line": "Sẵn sàng đăng · Mình sẽ đăng: [CẦN BẠN: số thật]"}]}
        code, out, _ = self.run_main("-", stdin=json.dumps(batch, ensure_ascii=False))
        self.assertEqual(code, 0)
        n1, n2 = out.strip().splitlines()
        self.assertEqual(n1, "N1 PASS")
        for defect in ('number "30" not in cited rows', 'hedge in hook: "có lẽ"', "Ready with an open [NEEDS]",
                       "urgency without an enforced Ledger row", "result claim without a Substantiated+consent"):
            self.assertIn(defect, n2)
        self.assertNotIn("keyword", n2)

    def test_invalid_input_exits_2(self):
        for bad in ("not json", "[]", '{"pieces": []}', '{"pieces": [{"body": "x"}]}', '{"lang": "fr", "pieces": [{"id": "a"}]}'):
            code, out, err = self.run_main("-", stdin=bad)
            self.assertEqual(code, 2, bad)
            self.assertIn("invalid input", err)
            self.assertEqual(out, "")

    def test_bundled_ship_lint_is_self_contained(self):
        """tools/build.py inlines cmcore/checks.py; the single file gives the same output."""
        import build
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            (root / "tools" / "cmcore").mkdir(parents=True)
            shutil.copy(TOOLS / "shiplint.py", root / "tools" / "shiplint.py")
            shutil.copy(TOOLS / "cmcore" / "checks.py", root / "tools" / "cmcore" / "checks.py")
            script = build.bundle_shiplint(root)
            alone = Path(tmp) / "alone"
            alone.mkdir()
            (alone / "ship_lint.py").write_text(script, encoding="utf-8")
            (alone / "batch.json").write_text(json.dumps(BATCH), encoding="utf-8")
            run = subprocess.run([sys.executable, "ship_lint.py", "batch.json"], cwd=alone,
                                 capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertNotIn("from cmcore", script)
        _, direct, _ = self.run_main("-", stdin=json.dumps(BATCH))
        self.assertEqual(run.stdout, direct)


if __name__ == "__main__":
    unittest.main()
