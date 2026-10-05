"""Shared check core for the runtime lint (tools/shiplint.py) and the transcript graders.

Everything lives in `checks.py`, which must stay standard-library only with no
imports from the repo: tools/build.py inlines it into the skill's single-file
scripts/ship_lint.py.
"""
