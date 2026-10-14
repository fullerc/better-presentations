#!/usr/bin/env python3
"""Build shareable skill archives, or check their contents against the source."""

import argparse
from io import BytesIO
from pathlib import Path
import re
import sys
from zipfile import BadZipFile, ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]


def skill_files(skill):
    """Use an explicit file policy so local caches cannot enter a download."""
    if skill.is_symlink():
        raise ValueError(f"Skill folder must not be a symlink: {skill.name}")
    name = skill.name
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise ValueError(f"Invalid skill folder name: {name}")
    files = {}
    for path in sorted(skill.rglob("*")):
        relative = path.relative_to(skill)
        if path.is_symlink():
            raise ValueError(f"Symlinks are not packaged: {name}/{relative}")
        if any(part.startswith(".") or part == "__pycache__" for part in relative.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix != ".md" and relative.as_posix() != "agents/openai.yaml":
            raise ValueError(f"Unsupported file; review packaging rules: {name}/{relative}")
        files[f"{name}/{relative.as_posix()}"] = path.read_bytes()
    entry = files.get(f"{name}/SKILL.md", b"").decode("utf-8")
    if not entry.startswith("---\n"):
        raise ValueError(f"Missing SKILL.md frontmatter: {name}")
    parts = entry.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError(f"Unclosed SKILL.md frontmatter: {name}")
    fields = parts[1].splitlines()
    if f"name: {name}" not in fields or not any(line.startswith("description:") and line[12:].strip() for line in fields):
        raise ValueError(f"Expected matching name and nonempty description: {name}")
    files[f"{name}/LICENSE"] = (ROOT / "LICENSE").read_bytes()
    return files


def archive_bytes(files):
    output = BytesIO()
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(files.items()):
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, data)
    return output.getvalue()


def check_archive(path, expected):
    with ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or set(names) != set(expected):
            raise ValueError(f"Archive file list differs from source: {path.name}")
        for name, data in expected.items():
            if archive.read(name) != data:
                raise ValueError(f"Archive content differs from source: {path.name}: {name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify downloads without writing files")
    args = parser.parse_args()
    skills = sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No skills found")
    if not args.check:
        (ROOT / "downloads").mkdir(exist_ok=True)
    for skill in skills:
        files = skill_files(skill)
        paths = [ROOT / "downloads" / f"{skill.name}{suffix}" for suffix in (".zip", ".skill")]
        if args.check:
            for path in paths:
                check_archive(path, files)
            if paths[0].read_bytes() != paths[1].read_bytes():
                raise ValueError(f"ZIP and .skill downloads differ: {skill.name}")
            print(f"Verified {skill.name}: {len(files)} files in each download")
        else:
            data = archive_bytes(files)
            for path in paths:
                path.write_bytes(data)
            print(f"Packaged {skill.name}: {len(files)} files in each download")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, BadZipFile, UnicodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
