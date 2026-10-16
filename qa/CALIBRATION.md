# Calibration (gate G3b) and judge validation

judge_validated: no

The judge's P results count only after validation:
- ≥40 founder-labelled pieces per edition, ≥20 of them "don't post";
- ≥85% post/don't-post agreement;
- the judge fails ≥90% of the founder's "don't post" pieces.

Until then every judge-scored result is **provisional**. See `evals/acceptance.toml` `[judge]` and `[calibration]`.

## Per release

| Release | Edition | Lane | Format | Runtime Ready / judge FAIL | Self-Edge − judge-Edge | Manual-lint miss rate (worst check) | Draft rate | Notes |
|---|---|---|---|---|---|---|---|---|
