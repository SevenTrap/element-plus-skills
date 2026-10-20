#!/usr/bin/env python3
"""Offline structural checks for the Element Plus 2.14.6 skill library.

Requires PyYAML. Checks every non-hidden Markdown file, without executing examples
or downloading sources. It validates link targets, not fragment identifiers or
the semantic accuracy of component APIs.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

VERSION = "2.14.6"
TAG_COMMIT = "5ac2b162180d3922d77c50990bb40c2f02376796"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]*>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\s*\)")
REFERENCE = re.compile(r"^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]*>|\S+)", re.MULTILINE)
SINCE = re.compile(r"(?:\bsince\s+|\^\(\s*)(\d+\.\d+\.\d+)", re.IGNORECASE)


def markdown_body(text, path, errors):
    """Remove fenced code while checking matching backtick/tilde delimiters."""
    lines = []
    opening = None
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE.match(line)
        if opening is None:
            if match:
                opening = (match[1][0], len(match[1]), number)
                lines.append("")
            else:
                lines.append(line)
        else:
            if (match and match[1][0] == opening[0]
                    and len(match[1]) >= opening[1] and not match[2].strip()):
                opening = None
            lines.append("")
    if opening:
        errors.append(f"{path}:{opening[2]}: unclosed code fence")
    return "\n".join(lines)


def link_targets(body):
    """Include inline/image links and reference definitions (including resources)."""
    return [match[1].strip("<>") for pattern in (LINK, REFERENCE)
            for match in pattern.finditer(body)]


def local_target(target, document, root, errors):
    try:
        parsed = urlsplit(target)
    except ValueError as error:
        errors.append(f"{document.relative_to(root)}: invalid URL {target!r}: {error}")
        return None
    if target.startswith("#") or parsed.scheme or target.startswith("//"):
        return None
    relative = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not relative:
        return None
    resolved = (document.parent / relative).resolve()
    if not resolved.is_relative_to(root):
        errors.append(f"{document.relative_to(root)}: link outside repository: {target}")
        return None
    if not resolved.exists():
        errors.append(f"{document.relative_to(root)}: missing local link target: {target}")
    return resolved


def skill_metadata(text, path, errors, names):
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.DOTALL)
    if not match:
        errors.append(f"{path}: missing or unterminated YAML frontmatter")
        return
    try:
        metadata = yaml.safe_load(match[1])
    except yaml.YAMLError as error:
        errors.append(f"{path}: invalid YAML frontmatter: {error}")
        return
    if not isinstance(metadata, dict):
        errors.append(f"{path}: YAML frontmatter must be a mapping")
        return
    name = metadata.get("name")
    if not isinstance(name, str) or len(name) > 64 or not NAME.fullmatch(name):
        errors.append(f"{path}: invalid skill name (lowercase hyphenated name, max 64 characters)")
    elif name in names:
        errors.append(f"{path}: duplicate skill name {name!r}, first used in {names[name]}")
    else:
        names[name] = str(path)
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{path}: description must be a nonempty string")
    extra = metadata.get("metadata")
    if not isinstance(extra, dict) or extra.get("element-plus-version") != VERSION:
        errors.append(f"{path}: metadata.element-plus-version must be {VERSION}")


def manifest_path(value, field, root, errors):
    """Validate manifest paths before accessing any referenced local file."""
    if (not isinstance(value, str) or not value or Path(value).is_absolute()
            or any(part in ("..", ".") for part in value.split("/")) or "\\" in value):
        errors.append(f"source-manifest.json: unsafe manifest path for {field}: {value!r}")
        return None
    path = root / value
    if not path.resolve().is_relative_to(root):
        errors.append(f"source-manifest.json: {field} outside repository: {value}")
        return None
    return path


def validate_manifest(root, paths, errors):
    manifest = root / "references/source-manifest.json"
    if not manifest.exists():
        return
    if not manifest.resolve().is_relative_to(root):
        errors.append("source-manifest.json: manifest outside repository")
        return
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        errors.append(f"invalid source manifest: {error}")
        return
    if not isinstance(data, dict):
        errors.append("source-manifest.json: manifest must be an object")
        return
    for field, expected in (("element_plus_version", VERSION), ("tag_commit", TAG_COMMIT)):
        if data.get(field) != expected:
            errors.append(f"source-manifest.json: {field} must be {expected}")
    if not isinstance(data.get("dev_commit"), str) or not re.fullmatch(r"[0-9a-f]{40}", data["dev_commit"]):
        errors.append("source-manifest.json: dev_commit must be a 40-character SHA")
    entries = data.get("components")
    if not isinstance(entries, list):
        errors.append("source-manifest.json: components must be an array")
        return
    expected = {str(path.relative_to(root)) for path in paths
                if path.name == "SKILL.md" and path.relative_to(root).parts[0] == "components"
                and path.parent.name.startswith("el-")}
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("source-manifest.json: component entry must be an object")
            continue
        checked = {field: manifest_path(entry.get(field), field, root, errors)
                   for field in ("skill", "reference", "source")}
        skill = entry.get("skill")
        if checked["skill"] is not None:
            if skill not in expected:
                errors.append(f"source-manifest.json: unknown component {skill}")
            if skill in seen:
                errors.append(f"source-manifest.json: duplicate component {skill}")
            seen.add(skill)
            component = checked["skill"].parent
            if entry.get("reference") != str((component / "references/api.md").relative_to(root)):
                errors.append(f"source-manifest.json: reference must belong to {skill}")
            source = f"docs/en-US/component/{component.name.removeprefix('el-')}.md"
            if entry.get("source") != source:
                errors.append(f"source-manifest.json: source for {skill} must be {source}")
        for field in ("source_sha256", "reference_sha256"):
            if not isinstance(entry.get(field), str) or not re.fullmatch(r"[0-9a-f]{64}", entry[field]):
                errors.append(f"source-manifest.json: {field} must be a SHA-256 digest")
        reference = checked["reference"]
        if reference is not None:
            try:
                actual = hashlib.sha256(reference.read_bytes()).hexdigest()
            except OSError as error:
                errors.append(f"source-manifest.json: cannot read reference {entry.get('reference')}: {error}")
            else:
                if entry.get("reference_sha256") != actual:
                    errors.append(f"source-manifest.json: reference_sha256 mismatch for {entry.get('reference')}")
    for missing in sorted(expected - seen):
        errors.append(f"source-manifest.json: missing component {missing}")


def validate(root):
    """Return all validation errors, leaving the library unchanged."""
    root = Path(root).resolve()
    if not root.is_dir():
        return [f"{root}: repository root is not a directory"]
    errors = []
    names = {}
    paths = sorted(path for path in root.rglob("*.md")
                   if not any(part.startswith(".") for part in path.relative_to(root).parts))
    if not any(path.name == "SKILL.md" for path in paths):
        errors.append("No SKILL.md files found")
    for path in paths:
        relative = path.relative_to(root)
        if not path.resolve().is_relative_to(root):
            errors.append(f"{relative}: Markdown file outside repository")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{relative}: cannot read Markdown: {error}")
            continue
        body = markdown_body(text, relative, errors)
        targets = [local_target(target, path, root, errors) for target in link_targets(body)]
        if path.name == "SKILL.md":
            skill_metadata(text, relative, errors, names)
            if relative.parts[0] == "components" and path.parent.name.startswith("el-"):
                api = path.parent / "references/api.md"
                if not api.is_file():
                    errors.append(f"{relative}: missing references/api.md")
                if api.resolve() not in targets:
                    errors.append(f"{relative}: body must link references/api.md")
        if path.name == "api.md":
            for match in SINCE.finditer(body):
                version = tuple(int(value) for value in match[1].split("."))
                line_start = body.rfind("\n", 0, match.start()) + 1
                context = body[line_start:match.start()]
                if version >= (3, 0, 0) and re.search(r"\bremov(?:ed|al)\b", context, re.IGNORECASE):
                    continue
                if version > (2, 14, 6):
                    errors.append(f"{relative}: API since {match[1]} is newer than {VERSION}")
    validate_manifest(root, paths, errors)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, help="library directory")
    parser.add_argument("--root", type=Path, help="library directory (alternative to positional)")
    args = parser.parse_args()
    if args.root and args.directory:
        parser.error("use either directory or --root")
    root = args.root or args.directory or Path(__file__).resolve().parent.parent
    errors = validate(root)
    if errors:
        print("\n".join(errors))
        print(f"Validation failed: {len(errors)} error(s).")
        return 1
    print(f"Validation passed: Element Plus {VERSION} skills in {root.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
