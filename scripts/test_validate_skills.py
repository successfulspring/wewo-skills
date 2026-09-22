"""Exercise package-validation failures using isolated, mutated repository copies.

These tests validate the authoring tool, not the behavior of a running skill.
Run from the plugin root: python -B -m unittest discover -s scripts -p test_*.py
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import validate_skills as validator


class PackageContractsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="wewo-validator-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = Path(__file__).resolve().parent.parent
        for directory in ("skills", ".codex-plugin", ".claude-plugin", ".agents"):
            shutil.copytree(source / directory, self.root / directory)

    def replace(self, relative, old, new):
        path = self.root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new), encoding="utf-8")

    def check(self, function):
        result = validator.Validation()
        function(self.root, result)
        return result.errors

    def append_runtime(self, skill, text):
        path = self.root / "skills" / skill / "references" / "invalid-contract.md"
        path.write_text(text, encoding="utf-8")

    def test_valid_layout_and_packaging(self):
        for function in (
            validator.validate_skill_structure,
            validator.validate_artifact_ownership,
            validator.validate_workspace_contracts,
            validator.validate_agent_names,
            validator.validate_shared_contracts,
            validator.validate_context_content_contracts,
            validator.validate_plugin_packaging,
            validator.validate_marketplace_packaging,
            validator.validate_no_cross_skill_routing,
            validator.validate_self_containment,
        ):
            with self.subTest(function=function.__name__):
                self.assertEqual([], self.check(function))

    def test_each_display_name_must_match_its_skill(self):
        for skill in validator.EXPECTED_SKILLS:
            with self.subTest(skill=skill):
                relative = f"skills/{skill}/agents/openai.yaml"
                wrong = "Wewo Context" if skill == "wewo-context" else "Wrong Name"
                self.replace(relative, f'"{skill}"', f'"{wrong}"')
                errors = self.check(validator.validate_agent_names)
                self.assertEqual(1, len(errors))
                self.assertIn("interface.display_name", errors[0])
                self.replace(relative, f'"{wrong}"', f'"{skill}"')

    def test_display_name_is_checked_inside_interface_only(self):
        relative = "skills/wewo-context/agents/openai.yaml"
        self.replace(relative, '  display_name: "wewo-context"\n', '')
        path = self.root / relative
        with path.open("a", encoding="utf-8") as stream:
            stream.write('\ndependencies:\n  display_name: "wewo-context"\n')
        self.assertTrue(self.check(validator.validate_agent_names))

    def test_duplicate_or_unsupported_display_name_is_rejected(self):
        relative = "skills/wewo-context/agents/openai.yaml"
        original = '  display_name: "wewo-context"'
        for extra in ('  display_name: "wewo-context"', '  display_name: [wewo-context]'):
            with self.subTest(extra=extra):
                changed = original + "\n" + extra
                self.replace(relative, original, changed)
                self.assertTrue(self.check(validator.validate_agent_names))
                self.replace(relative, changed, original)

    def test_display_name_allows_literal_yaml_quotes_and_comments(self):
        relative = "skills/wewo-context/agents/openai.yaml"
        original = '  display_name: "wewo-context"'
        for value in ("'wewo-context'", "wewo-context # canonical name"):
            with self.subTest(value=value):
                changed = "  display_name: " + value
                self.replace(relative, original, changed)
                self.assertEqual([], self.check(validator.validate_agent_names))
                self.replace(relative, changed, original)

    def test_context_requirement_mapping_cannot_be_removed(self):
        self.replace(
            "skills/wewo-context/SKILL.md", validator.CONTEXT_REQUIREMENT_CONTRACT, ""
        )
        errors = self.check(validator.validate_context_content_contracts)
        self.assertEqual(1, len(errors))
        self.assertIn("requirement-evidence", errors[0])

    def test_each_workspace_copy_rejects_local_fallback_drift(self):
        original = "Only a genuinely non-Git project defaults to `local`."
        changed = "Every project defaults to `local`."
        for skill in validator.EXPECTED_SKILLS:
            with self.subTest(skill=skill):
                relative = f"skills/{skill}/SKILL.md"
                self.replace(relative, original, changed)
                errors = self.check(validator.validate_shared_contracts)
                self.assertEqual(1, len(errors))
                self.assertIn("workspace contract differs", errors[0])
                self.replace(relative, changed, original)

    def test_each_skill_requires_untrusted_evidence_boundary(self):
        for skill in validator.EXPECTED_SKILLS:
            with self.subTest(skill=skill):
                relative = f"skills/{skill}/SKILL.md"
                self.replace(relative, validator.UNTRUSTED_EVIDENCE_CONTRACT, "omitted")
                errors = self.check(validator.validate_shared_contracts)
                self.assertEqual(1, len(errors))
                self.assertIn("untrusted-evidence", errors[0])
                self.replace(relative, "omitted", validator.UNTRUSTED_EVIDENCE_CONTRACT)

    def test_each_skill_rejects_reference_access_expansion(self):
        original = "Access those only\nwith explicit user authorization"
        changed = "Access those automatically\nwithout user authorization"
        for skill in validator.EXPECTED_SKILLS:
            with self.subTest(skill=skill):
                relative = f"skills/{skill}/SKILL.md"
                self.replace(relative, original, changed)
                errors = self.check(validator.validate_shared_contracts)
                self.assertEqual(1, len(errors))
                self.assertIn("source-access", errors[0])
                self.replace(relative, changed, original)

    def test_context_sensitive_information_rule_cannot_be_removed(self):
        self.replace(
            "skills/wewo-context/references/context-content.md",
            validator.CONTEXT_SENSITIVE_CONTRACT, "",
        )
        errors = self.check(validator.validate_context_content_contracts)
        self.assertEqual(1, len(errors))
        self.assertIn("sensitive-information", errors[0])

    def test_contract_marker_deletion_duplication_and_reordering_fail(self):
        relative = "skills/wewo-context/SKILL.md"
        start, end = "<!-- wewo:workspace:start -->", "<!-- wewo:workspace:end -->"
        path = self.root / relative
        original = path.read_text(encoding="utf-8")
        mutations = (
            original.replace(start, ""),
            original.replace(start, start + "\n" + start),
            end + "\n" + original.replace(end, ""),
        )
        for changed in mutations:
            with self.subTest(changed=changed[:80]):
                path.write_text(changed, encoding="utf-8")
                self.assertTrue(self.check(validator.validate_shared_contracts))
        path.write_text(original, encoding="utf-8")

    def test_contracts_allow_whitespace_reflow_and_skill_specific_prose(self):
        relative = "skills/wewo-context/SKILL.md"
        self.replace(
            relative, validator.WORKSPACE_CONTRACT,
            "\n\n  " + "   ".join(validator.WORKSPACE_CONTRACT.split()) + "\n",
        )
        with (self.root / relative).open("a", encoding="utf-8") as stream:
            stream.write("\nAn independently maintained skill-specific note.\n")
        self.assertEqual([], self.check(validator.validate_shared_contracts))

    def test_missing_seventh_skill_is_rejected(self):
        target = (self.root / "skills" / "wewo-context").resolve()
        target.relative_to(self.root.resolve())
        shutil.rmtree(target)
        self.assertTrue(self.check(validator.validate_skill_structure))

    def test_requirement_owner_still_needs_its_output(self):
        self.replace(
            "skills/wewo-build/SKILL.md",
            validator.REQUIREMENT_OUTPUT_PREFIX + "implementation-record.md",
            "implementation-record.md",
        )
        self.assertTrue(self.check(validator.validate_artifact_ownership))

    def test_context_outputs_are_not_requirement_artifacts(self):
        self.replace(
            "skills/wewo-context/SKILL.md",
            validator.CONTEXT_OUTPUT_PATHS[0],
            validator.REQUIREMENT_OUTPUT_PREFIX + "project-context.md",
        )
        self.assertTrue(self.check(validator.validate_artifact_ownership))
        self.assertTrue(self.check(validator.validate_workspace_contracts))

    def test_context_can_locate_requirement_evidence(self):
        path = self.root / "skills/wewo-context/SKILL.md"
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\nRead selected source at " + validator.REQUIREMENT_OUTPUT_PREFIX + "prd.md\n")
        self.assertEqual([], self.check(validator.validate_artifact_ownership))

    def test_all_skills_expose_both_context_locations(self):
        self.replace(
            "skills/wewo-test/SKILL.md", validator.CONTEXT_OUTPUT_PATHS[1], "omitted"
        )
        self.assertTrue(self.check(validator.validate_workspace_contracts))

    def test_legacy_branch_only_paths_in_references_are_rejected(self):
        self.append_runtime("wewo-erd", "docs/wewo/<branch-name>/<requirement-slug>/")
        self.assertTrue(self.check(validator.validate_workspace_contracts))

    def test_context_remains_normally_discoverable(self):
        path = self.root / "skills/wewo-context/agents/openai.yaml"
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\npolicy:\n  allow_implicit_invocation: false\n")
        self.assertTrue(self.check(validator.validate_workspace_contracts))

    def test_cross_skill_routing_includes_new_capability(self):
        self.append_runtime("wewo-prd", "Invoke wewo-context before continuing.")
        self.assertTrue(self.check(validator.validate_no_cross_skill_routing))

    def test_existing_capability_boundaries_still_reject_coupling(self):
        cases = (
            ("wewo-build", "Read test-cases.md.", validator.validate_build_invariants),
            ("wewo-test", "Read review.md.", validator.validate_test_invariants),
            ("wewo-testcases", "TDD Candidate", validator.validate_testcases_invariants),
            ("wewo-review", "Read test-execution.md.", validator.validate_review_invariants),
        )
        for skill, text, function in cases:
            with self.subTest(skill=skill):
                self.append_runtime(skill, text)
                self.assertTrue(self.check(function))

    def test_shared_runtime_dependency_still_rejected(self):
        self.append_runtime("wewo-context", "Read shared/context.md.")
        self.assertTrue(self.check(validator.validate_self_containment))

    def test_codex_marketplace_rejects_github_shorthand(self):
        path = self.root / ".agents/plugins/marketplace.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["plugins"][0]["source"] = {
            "source": "github", "repo": validator.GITHUB_PLUGIN_SOURCE_REPO
        }
        path.write_text(json.dumps(manifest), encoding="utf-8")
        self.assertTrue(self.check(validator.validate_marketplace_packaging))

    def test_gitlab_marketplace_pair_is_valid(self):
        for relative in (
            ".agents/plugins/marketplace.json",
            ".claude-plugin/marketplace.json",
        ):
            path = self.root / relative
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["plugins"][0]["source"]["url"] = (
                validator.GITLAB_PLUGIN_SOURCE_URL
            )
            path.write_text(json.dumps(manifest), encoding="utf-8")
        self.assertEqual([], self.check(validator.validate_marketplace_packaging))

    def test_mixed_distribution_sources_are_rejected(self):
        sources = {
            ".agents/plugins/marketplace.json": validator.GITHUB_PLUGIN_SOURCE_URL,
            ".claude-plugin/marketplace.json": validator.GITLAB_PLUGIN_SOURCE_URL,
        }
        for relative, source_url in sources.items():
            path = self.root / relative
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["plugins"][0]["source"]["url"] = source_url
            path.write_text(json.dumps(manifest), encoding="utf-8")
        errors = self.check(validator.validate_marketplace_packaging)
        self.assertEqual(1, len(errors))
        self.assertIn("same distribution repository", errors[0])

    def test_unapproved_distribution_source_is_rejected(self):
        path = self.root / ".agents/plugins/marketplace.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["plugins"][0]["source"]["url"] = (
            "https://example.com/wewo-skills.git"
        )
        path.write_text(json.dumps(manifest), encoding="utf-8")
        self.assertTrue(self.check(validator.validate_marketplace_packaging))

    def test_mismatched_plugin_versions_are_rejected(self):
        self.replace(".codex-plugin/plugin.json", '"0.3.0"', '"0.2.1"')
        self.assertTrue(self.check(validator.validate_plugin_packaging))


if __name__ == "__main__":
    unittest.main()
