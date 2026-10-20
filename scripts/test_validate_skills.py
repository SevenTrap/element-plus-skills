"""Regression tests for the offline skill-library validator."""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from validate_skills import validate


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill(self.root, "library")

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def skill(self, directory, name, body=""):
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Example skill\nmetadata:\n"
            '  element-plus-version: "2.14.6"\n---\n' + body,
            encoding="utf-8",
        )

    def test_valid_library_with_relative_resources_and_code_examples(self):
        self.write("README.md", "[guide](references/guide.md#topic)\n```md\n[missing](missing.md)\n```\n")
        self.write("references/guide.md", "# Topic\n")
        self.skill(self.root / "components/el-button", "el-button", "[API](references/api.md)\n")
        self.write("components/el-button/references/api.md", "Added (since 2.14.0), badge ^(2.14.6).\nRemoved in 3.0.0.\n")
        self.assertEqual(validate(self.root), [])

    def test_duplicate_and_invalid_names(self):
        self.skill(self.root / "duplicate", "library")
        self.skill(self.root / "invalid", "Bad_Name")
        errors = "\n".join(validate(self.root))
        self.assertIn("duplicate skill name", errors)
        self.assertIn("invalid skill name", errors)

    def test_missing_frontmatter_fields_and_wrong_version(self):
        self.write("SKILL.md", "---\nname: library\nmetadata:\n  element-plus-version: 2.15.0\n---\n")
        errors = "\n".join(validate(self.root))
        self.assertIn("description", errors)
        self.assertIn("2.14.6", errors)

    def test_malformed_yaml_and_missing_frontmatter(self):
        self.write("SKILL.md", "---\nname: [\n---\n")
        self.assertIn("YAML", "\n".join(validate(self.root)))
        self.write("SKILL.md", "# Skill\n")
        self.assertIn("frontmatter", "\n".join(validate(self.root)))

    def test_scans_readme_and_agents_for_unclosed_fences_and_links(self):
        self.write("README.md", "[missing](absent.md)\n~~~python\nprint('hello')\n")
        self.write("AGENTS.md", "[missing][guide]\n\n[guide]: no-guide.md\n")
        errors = "\n".join(validate(self.root))
        self.assertIn("unclosed code fence", errors)
        self.assertIn("absent.md", errors)
        self.assertIn("no-guide.md", errors)

    def test_links_cannot_escape_repository_including_symlinks(self):
        self.write("README.md", "[outside](../outside.md)\n[absolute](/etc/passwd)\n[symlink](external)\n")
        (self.root / "external").symlink_to("/etc/passwd")
        errors = validate(self.root)
        self.assertEqual(sum("outside repository" in error for error in errors), 3)

    def test_external_anchors_titles_encoded_paths_and_reference_links(self):
        self.write("README.md", '[url](https://example.com) [anchor](#topic) [email](mailto:a@b.com)\n'
                   '[space](<my guide.md> "title") [encoded](my%20guide.md)\n'
                   '[ref][guide]\n[guide]: <my guide.md> "title"\n')
        self.write("my guide.md", "# Topic\n")
        self.assertEqual(validate(self.root), [])

    def test_malformed_urls_report_document_location_without_crashing(self):
        self.write("README.md", "[broken](http://[)\n[broken-relative](//[)\n")
        errors = validate(self.root)
        self.assertEqual(sum("README.md: invalid URL" in error for error in errors), 2)

    def test_component_requires_api_file_and_body_link(self):
        self.skill(self.root / "components/el-button", "el-button")
        self.assertIn("references/api.md", "\n".join(validate(self.root)))
        self.write("components/el-button/references/api.md", "# API\n")
        self.assertIn("body must link", "\n".join(validate(self.root)))

    def test_future_since_versions_are_rejected_but_removal_notice_is_allowed(self):
        self.write("references/api.md", "(since 2.15.0) ^(2.14.7)\nRemoval in 3.0.0\n"
                   "Deprecated, and **will be** removed in (since 3.0.0).\n")
        errors = validate(self.root)
        self.assertEqual(sum("newer than 2.14.6" in error for error in errors), 2)

    def test_hidden_directories_are_excluded(self):
        self.write(".upstream-audit/SKILL.md", "invalid")
        self.write(".validation/README.md", "```\n[bad](missing)\n")
        self.assertEqual(validate(self.root), [])

    def test_cli_exit_codes_and_default_root_argument(self):
        script = Path(__file__).with_name("validate_skills.py")
        result = subprocess.run([sys.executable, str(script), str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.write("README.md", "[missing](missing.md)")
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing.md", result.stdout + result.stderr)

    def manifest(self):
        self.skill(self.root / "components/el-button", "el-button", "[API](references/api.md)\n")
        reference = self.write("components/el-button/references/api.md", "# API\n")
        return {
            "element_plus_version": "2.14.6",
            "tag_commit": "5ac2b162180d3922d77c50990bb40c2f02376796",
            "dev_commit": "a" * 40,
            "components": [{
                "skill": "components/el-button/SKILL.md",
                "reference": "components/el-button/references/api.md",
                "source": "docs/en-US/component/button.md",
                "source_sha256": "b" * 64,
                "reference_sha256": hashlib.sha256(reference.read_bytes()).hexdigest(),
            }],
        }

    def test_manifest_matches_component_and_hash(self):
        self.write("references/source-manifest.json", json.dumps(self.manifest()))
        self.assertEqual(validate(self.root), [])
        self.write("components/el-button/references/api.md", "Changed reference\n")
        self.assertIn("reference_sha256 mismatch", "\n".join(validate(self.root)))

    def test_manifest_detects_missing_duplicate_and_extra_components(self):
        manifest = self.manifest()
        self.write("references/source-manifest.json", json.dumps({**manifest, "components": []}))
        self.assertIn("missing component", "\n".join(validate(self.root)))
        entry = manifest["components"][0]
        self.write("references/source-manifest.json", json.dumps({**manifest, "components": [entry, entry]}))
        self.assertIn("duplicate component", "\n".join(validate(self.root)))
        self.write("references/source-manifest.json", json.dumps({**manifest, "components": [{**entry, "skill": "components/el-missing/SKILL.md"}]}))
        self.assertIn("unknown component", "\n".join(validate(self.root)))

    def test_manifest_validates_versions_hashes_and_source_mapping(self):
        manifest = self.manifest()
        entry = manifest["components"][0]
        invalid = {**manifest, "element_plus_version": "2.15.0", "tag_commit": "wrong", "dev_commit": "invalid",
                   "components": [{**entry, "source_sha256": "invalid", "reference_sha256": "invalid", "source": "docs/en-US/component/other.md"}]}
        self.write("references/source-manifest.json", json.dumps(invalid))
        errors = "\n".join(validate(self.root))
        for field in ("element_plus_version", "tag_commit", "dev_commit", "source_sha256", "reference_sha256", "source"):
            self.assertIn(field, errors)

    def test_manifest_rejects_escape_and_does_not_read_external_reference(self):
        manifest = self.manifest()
        entry = manifest["components"][0]
        for field in ("skill", "reference", "source"):
            with self.subTest(field=field):
                invalid = {**manifest, "components": [{**entry, field: "../../etc/passwd"}]}
                self.write("references/source-manifest.json", json.dumps(invalid))
                self.assertIn("unsafe manifest path", "\n".join(validate(self.root)))
        api = self.root / entry["reference"]
        api.unlink()
        api.symlink_to("/etc/passwd")
        self.write("references/source-manifest.json", json.dumps(manifest))
        self.assertIn("outside repository", "\n".join(validate(self.root)))

    def test_manifest_rejects_invalid_json_and_shapes(self):
        self.write("references/source-manifest.json", "{")
        self.assertIn("invalid source manifest", "\n".join(validate(self.root)))
        for invalid in ([], {"components": {}}, {"components": [None]}):
            self.write("references/source-manifest.json", json.dumps(invalid))
            self.assertTrue(validate(self.root))

    def test_empty_missing_root_and_yaml_nonmapping(self):
        (self.root / "SKILL.md").unlink()
        self.assertIn("No SKILL.md", "\n".join(validate(self.root)))
        self.assertIn("not a directory", "\n".join(validate(self.root / "missing")))
        self.write("SKILL.md", "---\n- value\n---\n")
        self.assertIn("must be a mapping", "\n".join(validate(self.root)))

    def test_unreadable_markdown_and_external_markdown_symlink(self):
        self.write("invalid.md", "placeholder").write_bytes(b"\xff")
        self.assertIn("cannot read Markdown", "\n".join(validate(self.root)))
        (self.root / "external.md").symlink_to("/etc/passwd")
        self.assertIn("Markdown file outside repository", "\n".join(validate(self.root)))


if __name__ == "__main__":
    unittest.main()
