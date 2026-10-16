# Retest VG7 (VN Hạnh + Tuấn) on kit 99e3dde: summary

Simulations only; no independent review this round (founder asked for speed). Both runs valid, 0 edits, 0 quits.

| Run | Coach turns | Map turn | Film-ready (active min) | Early win (min after dump prompt) | Failed checks |
|---|---|---|---|---|---|
| vg7 Hạnh | 9 | 7 | 19.1 | 2.8 | day0_shape (keyword guess tag), vn_natural (17% vs her 54%) |
| vg7 Tuấn | 8 | 6 | 16.2 | 3.3 | vn_natural (18% vs his 38%; bar 19%) |

- **Keyword guess tag (K42/VK-39 did not land).**
  - Hạnh's dump gives "ngại chào" from one named client (Thảo) plus "bao nhiêu em nói y hệt". The Map printed it untagged.
  - The simulated machine reads "they all say it" as heard. DECISIONS keeps that case a guess.
  - Founder call: keep the strict reading, or count a coach's "everyone says it" as heard.
- **Particles (VK-38/VK-40 did not land).**
  - This is the fourth round of wording changes to §CM-NATURAL 4 with no gain (15–18% against the coach's 38–54%).
  - Wording alone is not moving the simulated machine. Next options:
    - a concrete per-piece ratio in the always-read block, which needs block room;
    - a check step that rewrites flat endings before printing.
  - The founder's real-account test decides whether real ChatGPT/Claude output has the same gap.
- Kit gaps the simulators flagged, for the next fix round:
  - "chờ chút" vs the soft cut in the same send;
  - a voice-mode reminder after reply 2;
  - no main `keyword` field in §CM-CARD 3;
  - two near-duplicate one-question Zalo messages when there is no list;
  - a listing the coach must close this month has no Map slot.
