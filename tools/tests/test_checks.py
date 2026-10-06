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

    def test_month_name_dates_and_retirement_accounts(self):
        """G1 review (I8): month-name dates are dates and 401(k) / 403(b) are names, never claim numbers."""
        text = ("Thu, Oct 8 · TUE, OCT 13: the talk · Monday, Oct 19 · Note (Oct 6, 2026) · 6 Oct 2026 · Oct 12–18 · "
                "Oct 8th · May 2025 · her 401(k), a 401k, a 403(b) · $401k raised")
        nums = {n.raw: n for n in ck.numbers_in(text)}
        for raw in ("Oct 8", "OCT 13", "Oct 19", "Oct 6, 2026", "6 Oct 2026", "Oct 12", "18", "Oct 8th", "May 2025"):
            self.assertEqual(nums[raw].kind, "date", raw)
        for raw in ("401(k)", "401k", "403(b)"):
            self.assertTrue(nums[raw].structural and nums[raw].kind == "id", raw)
        self.assertEqual(nums["$401k"].value, 401_000)                     # money stays money
        self.assertEqual(raws("you may 2x it in 12 months; march 3 miles"), ["2x", "12", "3"])   # verbs, not months
        self.assertEqual(raws("Oct 8:30 call"), ["8:30"])                   # a time after a month is no day
        self.assertEqual(ck.number_keys(nums["Oct 8"]), ck.allowed_number_keys(["oct 08"]))
        self.assertEqual(ck.unsupported_numbers("Doors close Oct 31.", ["Oct 31"]), [])
        self.assertEqual(ck.unsupported_numbers("Doors close Oct 31.", ["2026-10-30"]), ["Oct 31"])

    def test_counts_beside_month_names_and_money_401k_stay_numbers(self):
        """G1 verifier: a date reading must not swallow an invented count or amount next to a month name."""
        for text, want in (("Oct 2026: 400 clients signed up.", ["400"]),
                           ("In October 20 clients joined.", ["20"]),
                           ("Since Oct 8 – 25 women booked a call.", ["25"]),
                           ("May 3 clients said yes.", ["3"]),
                           ("By June 30 women had an offer.", ["30"]),
                           ("In October 25% of them", ["25%"]),
                           ("Oct 20k followers, Oct 20+ clients", ["20k", "20+"]),
                           ("We did 401k in revenue last year.", ["401k"]),
                           ("I made 457k last year", ["457k"]),
                           ("9/10 clients got hired.", ["9", "10"]), ("3/4 of my clients", ["3", "4"])):
            with self.subTest(text=text):
                self.assertEqual([n.raw for n in ck.numbers_in(text) if n.kind != "date" and not n.structural], want)
        for text in ("Oct 7 email", "Oct 8 is talk day", "Oct 12th–18th", "Oct 12–18: plan", "her 401k/pension",
                     "your 401(k), pension", "Talk day 13/10", "Đăng ngày 13/10 nhé"):
            with self.subTest(text=text):
                self.assertEqual([n.raw for n in ck.numbers_in(text) if n.kind != "date" and not n.structural], [])

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

    def test_app_counts_from_someone_elses_post(self):
        """wf13 I8: a liked post's counts as apps print them are read by value (2.1M, 52,7 N, 1,2 Tr)."""
        nums = {n.raw: n.value for n in ck.numbers_in("▶ 2.1M · ♥ 88.4K · 52,7 N lượt xem · 1,2 Tr · 5Tr")}
        self.assertEqual(nums, {"2.1M": 2_100_000, "88.4K": 88_400, "52,7 N": 52_700, "1,2 Tr": 1_200_000,
                                "5Tr": 5_000_000})
        self.assertEqual(ck.unsupported_numbers("Cô ấy có 52.700 lượt xem", ["52,7 N"]), [])
        self.assertEqual([n.raw for n in ck.numbers_in("3 Nhóm, 2 Mbps, 3 Trang")], ["3", "2", "3"])

    def test_video_timestamps_are_labels(self):
        """Baseline vn/hanh I8 false positive: "15" and "35" were the beat marks of a TikTok script."""
        text = ("🎬 **0–3 giây (Hook):** nhìn thẳng camera\n🎬 **3–15 giây:** câu đầu\n🎬 **15–35 giây:** tối mưa\n"
                "Ở giây 35 thì cắt cảnh. 0:15 cut to the car. 0:45–1:10 the steps. Beat at 0–3s, then 20 s of b-roll.")
        self.assertEqual(ck.unsupported_numbers(text, []), [])
        self.assertEqual(ck.unsupported_numbers("Closes 11:59. Women in their 40s. 41 thẻ trong 3 tháng.", ["3"]),
                         ["11:59", "40s", "41"])                       # deadlines, decades and counts stay claims


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

    def test_hypothetical_speakers_are_not_attributed(self):
        """Review G13: a scenario ('someone asks …') is not a claim that someone said it; a past event still is."""
        for text in ('DM REPLY 1 · someone asks the price, or "can you do my room"',
                     'If anyone says "too expensive", send the list.', 'Khi ai đó hỏi "giá sao em", gửi bảng giá.'):
            with self.subTest(text=text):
                self.assertFalse(ck.quotes_in(text, "vn" if "ai đó" in text else "en")[0].attributed)
        self.assertTrue(ck.quotes_in('Someone told me "you saved my job".')[0].attributed)
        self.assertTrue(ck.quotes_in('Lorraine said "can you do my room".')[0].attributed)
        # verifier: a reported message and an everyone-says claim stay attributed
        self.assertTrue(ck.quotes_in('A reader writes: "your post saved my marriage"')[0].attributed)
        self.assertFalse(ck.quotes_in('If a reader writes "too long", cut it.')[0].attributed)
        self.assertTrue(ck.quotes_in('Ai cũng hỏi "giá sao em"', "vn")[0].attributed)
        self.assertFalse(ck.quotes_in('Có ai hỏi "giá sao em" thì gửi bảng giá.', "vn")[0].attributed)

    def test_glossed_terms_are_not_attributed_quotes(self):
        """Baseline vn/hanh I9 false positive: the assistant explaining an English word."""
        text = '(Mấy chữ tiếng Anh: "pillar" là nhóm chủ đề, "CTA" là câu mời khách nhắn tin, "insight" là điều khách nghĩ.)'
        self.assertEqual([q.attributed for q in ck.quotes_in(text, "vn")], [False, False, False])
        self.assertFalse(ck.quotes_in('She said "ROI" means the money back.', "en")[0].attributed)
        self.assertTrue(ck.quotes_in('She said "I finally feel like me again" and cried.', "en")[0].attributed)

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


class CopyRunTests(unittest.TestCase):
    """wf13 DISTANCE: shared runs of 6 EN words / 8 VN tiếng with someone else's post."""

    EN_SOURCE = ("You don't need a better résumé. You need five conversations. Ask for 20 minutes, not a job. "
                 "Comment GUIDE and I'll DM you my conversation guide. Link in bio for the full guide to pricing "
                 "your offer.")
    VN_SOURCE = ("Shop mới mở hay tính giá bán bằng cách lấy giá nhập nhân đôi. Sai rồi nhé. Mình làm sẵn một file "
                 "tính giá vốn từng đơn: phí sàn, ship, bao bì, quảng cáo chia theo đơn. Comment bên dưới mình gửi "
                 "file nhé.")
    EN_STOCK = ["link in bio", "comment below", "let me know in the comments"]
    VN_STOCK = ["comment bên dưới", "link ở bio"]

    def test_tokens_are_nfc_casefolded_and_punctuation_free(self):
        self.assertEqual(ck.copy_tokens("“Don’t” SEND—résumés; $2,400!"), ["dont", "send", "résumés", "2400"])
        self.assertEqual(ck.copy_tokens("lãi ảo"), ["lãi", "ảo"])                 # NFD in, NFC out

    def test_en_runs(self):
        self.assertEqual(ck.copy_runs("Here's the truth: you need five conversations. Ask for 20 minutes, not a job.",
                                      self.EN_SOURCE, "en"),
                         ["you need five conversations ask for 20 minutes not a job"])
        self.assertEqual(ck.copy_runs("YOU DON'T NEED A BETTER RÉSUMÉ!", self.EN_SOURCE, "en"),
                         ["you dont need a better résumé"])
        self.assertEqual(ck.copy_runs("You don't need a better job.", self.EN_SOURCE, "en"), [])     # 5 words
        self.assertEqual(ck.copy_runs("Coffee before resume: one stranger a week.", self.EN_SOURCE, "en"), [])
        self.assertEqual(ck.copy_runs("need a better résumé", self.EN_SOURCE, "en", n=4), ["need a better résumé"])

    def test_en_stock_phrases_are_left_out_first(self):
        text = "Link in bio for the full guide."
        self.assertEqual(ck.copy_runs(text, self.EN_SOURCE, "en"), ["link in bio for the full guide"])
        self.assertEqual(ck.copy_runs(text, self.EN_SOURCE, "en", stock=self.EN_STOCK), [])   # 4 words left
        self.assertEqual(ck.copy_runs("Link in bio for the full guide to pricing your offer.", self.EN_SOURCE, "en",
                                      stock=self.EN_STOCK), ["for the full guide to pricing your offer"])

    def test_vn_runs_count_tieng(self):
        eight = "Chị em ơi, mình làm sẵn một file tính giá vốn từng đơn cho chị em."
        self.assertEqual(ck.copy_runs(eight, self.VN_SOURCE, "vn"), ["mình làm sẵn một file tính giá vốn từng đơn"])
        seven = "Có một file tính giá vốn từng đơn."                               # 7 tiếng shared
        self.assertEqual(ck.copy_runs(seven, self.VN_SOURCE, "vn"), [])
        self.assertEqual(ck.copy_runs("Đã làm sẵn một file tính giá vốn từng đơn.", self.VN_SOURCE, "vn"),
                         ["làm sẵn một file tính giá vốn từng đơn"])               # 9 tiếng
        self.assertEqual(ck.copy_runs("Em có file tính giá vốn từng đơn.", self.VN_SOURCE, "vn"), [])   # 6 tiếng
        self.assertEqual(ck.copy_runs("tính giá vốn từng đơn", self.VN_SOURCE, "en"), [])    # EN n = 6, 5 tokens

    def test_vn_stock_phrases_are_left_out_first(self):
        text = "Quảng cáo chia theo đơn. Comment bên dưới mình gửi file nhé."
        self.assertEqual(ck.copy_runs(text, self.VN_SOURCE, "vn"),
                         ["quảng cáo chia theo đơn comment bên dưới mình gửi file nhé"])
        self.assertEqual(ck.copy_runs(text, self.VN_SOURCE, "vn", stock=self.VN_STOCK),
                         ["quảng cáo chia theo đơn mình gửi file nhé"])            # 9 tiếng still shared
        self.assertEqual(ck.copy_runs("Comment bên dưới mình gửi file nhé.", self.VN_SOURCE, "vn",
                                      stock=self.VN_STOCK), [])

    def test_stock_phrase_list(self):
        body = "# comment\n\nlink in bio\n  comment below  \nlink in bio\n"
        self.assertEqual(ck.stock_phrase_list(body), ["link in bio", "comment below"])

    def test_point_order_mirror(self):
        source = ("Who calls you when something breaks? What do you fix that isn't in your job description? "
                  "What would stop working the week you left? You have skills nobody ever gave a title to.")
        mirrored = ("Ask who calls you when something breaks at work. Write what you fix that is not in your job "
                    "description. Picture what would stop working the week you left.")
        own = ("I sat at the kitchen table at 48 with 63 applications. Then I stopped applying. "
               "I bought one coffee a week for a stranger. Coffee before resume.")
        self.assertTrue(ck.point_order_mirror(mirrored, source))
        self.assertFalse(ck.point_order_mirror(own, source))
        reordered = ". ".join(reversed(mirrored.split(". ")))
        self.assertFalse(ck.point_order_mirror(reordered, source))

    def test_copy_note(self):
        en = ("Note: this follows their post closely. Platforms may show copies less, and the words belong to them. "
              "Posting is your call.")
        vn = ("Lưu ý: bài này bám sát bài của họ. Nền tảng có thể giảm hiển thị bài giống bài khác, và chữ là của "
              "họ. Đăng hay không là quyền của bạn.")
        self.assertEqual(ck.copy_note_marker(en), "this follows their post closely")
        self.assertEqual(ck.copy_note_marker(vn), "bài này bám sát bài của họ")
        self.assertEqual(ck.copy_note_marker("Note (5 Oct 2026): {name} follows their post closely."),
                         "follows their post closely")
        self.assertTrue(ck.has_copy_note("NOTE (5 Oct 2026) — This follows their post closely! Your call.", en))
        self.assertTrue(ck.has_copy_note("Lưu ý: bài này bám sát bài của họ. Đăng hay không là quyền của chị.", vn))
        self.assertTrue(ck.has_copy_note("…it follows their post closely…"))         # fallback markers
        self.assertFalse(ck.has_copy_note("Here is your translation.", en))
        self.assertFalse(ck.has_copy_note("Đây là bản dịch của chị."))


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


EN_COPY_NOTE = ("Note: this follows their post closely. Platforms may show copies less, and the words belong to them. "
                "Posting is your call.")
COPY_BATCH = {
    "lang": "en",
    "sources": [
        {"id": "W-1", "text": "You don't need a better résumé. You need five conversations. "
                              "Ask for twenty minutes, not a job. Comment GUIDE and I'll DM you my guide."},
        {"id": "W-2", "text": "Who calls you when something breaks? What do you fix that isn't in your job "
                              "description? What would stop working the week you left?"},
    ],
    "pieces": [
        {"id": "N1", "format": "native-short", "hook": "Five conversations beat fifty applications.",
         "body": "Ask for twenty minutes, not a job. That is how I got hired.", "cites": ["W-1"]},
        {"id": "N2", "format": "native-short", "hook": "Ask for twenty minutes, not a job.", "body": "Then listen."},
        {"id": "N3", "format": "native-short", "hook": "Coffee before résumé.",
         "body": "One stranger a week. Twenty minutes. That is the whole plan.", "cites": ["W-1"]},
        {"id": "N4", "format": "text-post", "hook": "Three questions.",
         "body": "Ask yourself: who calls you when something at work breaks? Then list what you fix that is "
                 "outside your job description. Last, picture what would stop working if you left that week.",
         "cites": ["W-2"]},
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

    def lint(self, batch: dict, *args: str) -> dict[str, str]:
        code, out, err = self.run_main("-", *args, stdin=json.dumps(batch, ensure_ascii=False))
        self.assertEqual(code, 0, err)
        return {line.split(" ", 1)[0]: line for line in out.strip().splitlines()}

    def test_cited_source_copy_runs(self):
        lines = self.lint(COPY_BATCH)
        self.assertEqual(lines["N1"], "N1 FAIL: copy run: 'ask for twenty minutes not a job'")
        self.assertEqual(lines["N2"], "N2 PASS")                      # does not cite W-1
        self.assertEqual(lines["N3"], "N3 PASS")                      # the shape, not the words
        self.assertEqual(lines["N4"], "N4 FAIL: point order mirrors W-2")

    def test_stock_phrases_never_make_a_copy_run(self):
        batch = {"lang": "en",
                 "sources": [{"id": "W-1", "text": "Big news. Let me know in the comments what you think, friends."},
                             {"id": "W-2", "text": "Big news. Tell me in the DMs what you think, friends."}],
                 "pieces": [{"id": "N1", "format": "text-post", "body": "Let me know in the comments what you "
                                                                       "think, friends.", "cites": ["W-1"]},
                            {"id": "N2", "format": "text-post", "body": "Tell me in the DMs what you think, friends.",
                             "cites": ["W-2"]}]}
        lines = self.lint(batch)
        self.assertEqual(lines["N1"], "N1 PASS")                      # locales/en/stock-phrases.txt
        self.assertEqual(lines["N2"], "N2 FAIL: copy run: 'tell me in the dms what you think friends'")
        lines = self.lint(dict(batch, stock_phrases=["tell me in the DMs"]))
        self.assertEqual(lines["N2"], "N2 PASS")                      # payload stock_phrases

    def test_explicit_copy_needs_the_copy_note(self):
        source = COPY_BATCH["sources"][0]["text"]
        batch = {"lang": "en", "copy_note": EN_COPY_NOTE,
                 "sources": [{"id": "W-1", "text": source, "explicit_copy": True}],
                 "pieces": [{"id": "N1", "format": "text-post", "body": source, "cites": ["W-1"]},
                            {"id": "N2", "format": "text-post", "body": "As you asked:\n" + source, "cites": ["W-1"],
                             "note": EN_COPY_NOTE},
                            {"id": "N3", "format": "text-post", "body": "Word for word:\n" + source, "cites": ["W-1"],
                             "verdict_line": "Ready to post · this follows their post closely."}]}
        lines = self.lint(batch)
        self.assertEqual(lines["N1"], "N1 FAIL: explicit copy without the copy note")
        self.assertEqual(lines["N2"], "N2 PASS")
        self.assertEqual(lines["N3"], "N3 PASS")
        del batch["copy_note"]                                          # fallback marker
        lines = self.lint(batch)
        self.assertEqual(lines["N1"], "N1 FAIL: explicit copy without the copy note")
        self.assertEqual(lines["N2"], "N2 PASS")

    def test_vn_explicit_copy_and_copy_runs(self):
        source = ("Shop mới mở hay tính giá bán bằng cách lấy giá nhập nhân đôi. Sai rồi nhé. Mình làm sẵn một "
                  "file tính giá vốn từng đơn.")
        batch = {"lang": "vn",
                 "sources": [{"id": "W-1", "text": source}, {"id": "W-2", "text": source, "explicit_copy": True}],
                 "pieces": [{"id": "N1", "format": "text-post", "body": "Chị làm sẵn một file tính giá vốn từng đơn "
                                                                       "cho các em.", "cites": ["W-1"]},
                            {"id": "N2", "format": "text-post", "body": "Chị có file tính giá vốn từng đơn.",
                             "cites": ["W-1"]},
                            {"id": "N3", "format": "text-post", "body": source, "cites": ["W-2"],
                             "note": "Lưu ý: bài này bám sát bài của họ. Đăng hay không là quyền của chị."}]}
        lines = self.lint(batch)
        self.assertEqual(lines["N1"], "N1 FAIL: copy run: 'làm sẵn một file tính giá vốn từng đơn'")
        self.assertEqual(lines["N2"], "N2 PASS")                      # 6 tiếng
        self.assertEqual(lines["N3"], "N3 PASS")

    def test_source_file_applies_to_every_piece(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "their-post.txt"
            path.write_text(COPY_BATCH["sources"][0]["text"], encoding="utf-8")
            batch = {"lang": "en", "pieces": [
                {"id": "N1", "format": "text-post", "body": "You need five conversations. Ask for twenty minutes."},
                {"id": "N2", "format": "text-post", "body": "Coffee before résumé. One stranger a week."}]}
            lines = self.lint(batch, "--source", str(path))
            self.assertEqual(lines["N1"], "N1 FAIL: copy run: 'you need five conversations ask for twenty minutes'")
            self.assertEqual(lines["N2"], "N2 PASS")
            self.assertEqual(self.lint(batch)["N1"], "N1 PASS")         # no source, no check
            code, _, err = self.run_main("-", "--source", str(Path(tmp) / "missing.txt"), stdin=json.dumps(batch))
            self.assertEqual(code, 2)
            self.assertIn("invalid input", err)

    def test_invalid_sources_exit_2(self):
        piece = '"pieces": [{"id": "N1", "body": "x"}]'
        for bad in ('{"sources": {}, ' + piece + "}", '{"sources": [{"text": "x"}], ' + piece + "}",
                    '{"sources": [{"id": "W-1", "text": 3}], ' + piece + "}",
                    '{"sources": [{"id": "W-1", "explicit_copy": "yes"}], ' + piece + "}",
                    '{"copy_note": 1, ' + piece + "}", '{"stock_phrases": [1], ' + piece + "}",
                    '{"pieces": [{"id": "N1", "note": 3}]}'):
            code, _, err = self.run_main("-", stdin=bad)
            self.assertEqual(code, 2, bad)
            self.assertIn("invalid input", err)

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
            (alone / "copy.json").write_text(json.dumps(COPY_BATCH), encoding="utf-8")
            run = subprocess.run([sys.executable, "ship_lint.py", "batch.json"], cwd=alone,
                                 capture_output=True, text=True)
            copy_run = subprocess.run([sys.executable, "ship_lint.py", "copy.json"], cwd=alone,
                                      capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertNotIn("from cmcore", script)
        _, direct, _ = self.run_main("-", stdin=json.dumps(BATCH))
        self.assertEqual(run.stdout, direct)
        _, direct_copy, _ = self.run_main("-", stdin=json.dumps(COPY_BATCH))
        self.assertEqual(copy_run.stdout, direct_copy, copy_run.stderr)


if __name__ == "__main__":
    unittest.main()
