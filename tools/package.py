#!/usr/bin/env python3
"""Deterministic zips for Content Machine (docs/BUILD.md §6).

    python3 tools/package.py [--edition en|vn|all] [--root PATH] [--release]

Zips dist/<edition>/ into dist/<zip_name>-v<VERSION>.zip. Entries are sorted,
timestamps are fixed at 1980-01-01 00:00, permissions are fixed (0644), and
dotfiles, __MACOSX and .DS_Store never go in. Non-ASCII names are an error
(E150). build.py uses make_zip() for the inner skill zip as well.

--release refuses to package unless qa/releases/v<VERSION>/ holds a PASS
RELEASE-VERDICT.md, a PASS RELEASE-VERDICT.second-read.md and a SIGNOFF.md
that says SHIP against the build_sha256 in dist/maintainer/manifest.json.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cmlib  # noqa: E402
from cmlib import CMError  # noqa: E402

ZIP_DATE = (1980, 1, 1, 0, 0, 0)
FILE_MODE = 0o100644          # regular file, rw-r--r--
EXCLUDED_NAMES = {"__MACOSX", ".DS_Store", "Thumbs.db", "desktop.ini"}
SHIPPED_FORBIDDEN_DIRS = {"qa", "evals"}   # E153


def is_excluded(rel_parts: tuple[str, ...]) -> bool:
    """True for dotfiles, dot-directories and OS litter anywhere in the path."""
    return any(p.startswith(".") or p in EXCLUDED_NAMES for p in rel_parts)


def collect_files(src_dir: Path) -> list[tuple[str, Path]]:
    """Every shippable file under src_dir as (posix relative path, absolute path), sorted."""
    out: list[tuple[str, Path]] = []
    for dirpath, dirnames, filenames in os.walk(src_dir):
        dirnames[:] = sorted(d for d in dirnames if not is_excluded((d,)))
        for name in filenames:
            path = Path(dirpath) / name
            relp = path.relative_to(src_dir)
            if is_excluded(relp.parts):
                continue
            out.append((relp.as_posix(), path))
    out.sort(key=lambda item: item[0])
    return out


def check_ascii(name: str, where: str) -> None:
    if not name.isascii():
        raise CMError("E150", f"non-ASCII file name '{name}'", where)


def make_zip(src_dir, out_path, prefix: str = "") -> list[str]:
    """Write a deterministic zip of src_dir to out_path; return the entry names.

    `prefix` (e.g. the skill folder name) is prepended to every entry.
    """
    src_dir, out_path = Path(src_dir), Path(out_path)
    if not src_dir.is_dir():
        raise CMError("E161", "folder to zip does not exist", str(src_dir))
    prefix = prefix.strip("/")
    if prefix:
        check_ascii(prefix, str(out_path))
    entries: list[tuple[str, Path]] = []
    for relp, path in collect_files(src_dir):
        arcname = f"{prefix}/{relp}" if prefix else relp
        check_ascii(arcname, str(out_path))
        entries.append((arcname, path))
    entries.sort(key=lambda item: item[0])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_name(out_path.name + ".tmp")
    with zipfile.ZipFile(tmp, "w") as zf:
        for arcname, path in entries:
            info = zipfile.ZipInfo(arcname, date_time=ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3          # unix, so external_attr means the same everywhere
            info.external_attr = FILE_MODE << 16
            zf.writestr(info, path.read_bytes(), compresslevel=9)
    os.replace(tmp, out_path)
    return [a for a, _ in entries]


def file_sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def compute_build_sha256(dist: Path, editions: list[str]) -> str:
    """One sha256 over every file in dist/<edition>/ (sorted), names included."""
    h = hashlib.sha256()
    for ed in sorted(editions):
        base = Path(dist) / ed
        if not base.is_dir():
            continue
        for relp, path in collect_files(base):
            h.update(f"{ed}/{relp}\0{file_sha256(path)}\n".encode("utf-8"))
    return h.hexdigest()


def read_version(root: Path) -> str:
    try:
        version = (root / "VERSION").read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        raise CMError("E161", "file not found", "VERSION")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise CMError("E161", f"bad version '{version}'", "VERSION")
    return version


# ---------------------------------------------------------------- release gate

class ReleaseRefused(Exception):
    """--release preconditions not met; the message lists every problem."""


def _first_line(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""
    return text.splitlines()[0].strip() if text.strip() else ""


def check_release(root: Path, version: str) -> str:
    """Return the signed build sha256, or raise ReleaseRefused naming every problem."""
    rel_dir = f"qa/releases/v{version}"
    folder = root / rel_dir
    problems: list[str] = []
    if _first_line(folder / "RELEASE-VERDICT.md") != "Result: PASS":
        problems.append(f"{rel_dir}/RELEASE-VERDICT.md: first line is not 'Result: PASS'")
    if _first_line(folder / "RELEASE-VERDICT.second-read.md") != "Result: PASS":
        problems.append(f"{rel_dir}/RELEASE-VERDICT.second-read.md: first line is not 'Result: PASS'")

    manifest_path = root / "dist" / "maintainer" / "manifest.json"
    build_sha = ""
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        build_sha = manifest.get("build_sha256", "")
    except (FileNotFoundError, json.JSONDecodeError):
        problems.append("dist/maintainer/manifest.json missing or unreadable (run tools/build.py)")
        manifest = {}
    if build_sha:
        actual = compute_build_sha256(root / "dist", manifest.get("editions", []))
        if actual != build_sha:
            problems.append("dist/ changed since the build (build_sha256 no longer matches); rebuild")

    try:
        signoff = (folder / "SIGNOFF.md").read_text(encoding="utf-8")
    except FileNotFoundError:
        signoff = ""
        problems.append(f"{rel_dir}/SIGNOFF.md missing")
    if signoff:
        if not re.search(r"\bSHIP\b", signoff) or re.search(r"\b(NO|NOT|DON'T|DO NOT)\s+SHIP\b", signoff, re.I):
            problems.append(f"{rel_dir}/SIGNOFF.md does not say SHIP")
        hashes = {h.lower() for h in re.findall(r"\b[0-9a-fA-F]{64}\b", signoff)}
        if not build_sha or build_sha.lower() not in hashes:
            problems.append(f"{rel_dir}/SIGNOFF.md does not carry this build's sha256 ({build_sha or 'none'})")
    if problems:
        raise ReleaseRefused("release refused:\n  " + "\n  ".join(problems))
    return build_sha


# ---------------------------------------------------------------- packaging

def package_edition(root: Path, edition_id: str, version: str) -> Path:
    edition = cmlib.load_edition(edition_id, root)
    src = root / "dist" / edition_id
    if not src.is_dir():
        raise CMError("E161", "build output missing; run tools/build.py first", f"dist/{edition_id}")
    for relp, _ in collect_files(src):
        if relp.split("/", 1)[0] in SHIPPED_FORBIDDEN_DIRS:
            raise CMError("E153", f"'{relp}' would ship qa/ or evals/ content", f"dist/{edition_id}")
    out = root / "dist" / f"{edition.zip_name}-v{version}.zip"
    make_zip(src, out)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--edition", default="all", choices=[*cmlib.EDITIONS, "all"])
    ap.add_argument("--root", type=Path, default=None, help="repo root (default: CM_ROOT or this repo)")
    ap.add_argument("--release", action="store_true", help="refuse without PASS verdicts and a SHIP sign-off")
    args = ap.parse_args(argv)
    root = (args.root or cmlib.ROOT).resolve()
    editions = list(cmlib.EDITIONS) if args.edition == "all" else [args.edition]
    try:
        version = read_version(root)
        if args.release:
            sha = check_release(root, version)
            print(f"release checks passed for v{version} (build {sha[:12]})")
        for ed in editions:
            out = package_edition(root, ed, version)
            with zipfile.ZipFile(out) as zf:
                empty = "  (empty: nothing built for this edition yet)" if not zf.namelist() else ""
            print(f"{cmlib.rel(out, root)}  {file_sha256(out)}{empty}")
    except (CMError, ReleaseRefused) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
