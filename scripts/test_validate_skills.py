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
            validator.validate_task_contracts,
            validator.validate_change_contracts,
            validator.validate_workspace_contracts,
            validator.validate_agent_names,
            validator.validate_shared_contracts,
            validator.validate_context_content_contracts,
            validator.validate_clarification_history_contracts,
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

    def test_each_clarification_phase_requires_exact_requirement_log_path(self):
        for skill in validator.CLARIFICATION_GUIDES:
            with self.subTest(skill=skill):
                relative = f"skills/{skill}/SKILL.md"
                self.replace(relative, validator.CLARIFICATION_HISTORY_PATH,
                             "docs/wewo/clarification-history.md")
                errors = self.check(validator.validate_clarification_history_contracts)
                self.assertEqual(1, len(errors))
                self.assertIn("missing clarification contract", errors[0])
                self.replace(relative, "docs/wewo/clarification-history.md",
                             validator.CLARIFICATION_HISTORY_PATH)

    def test_clarification_phase_cannot_claim_other_phase_entries(self):
        for skill, (phase, _guide) in validator.CLARIFICATION_GUIDES.items():
            with self.subTest(skill=skill):
                relative = f"skills/{skill}/SKILL.md"
                original = f"`{phase}` entries; preserve all other entries and manual content."
                changed = "all entries; replace other entries and manual content."
                self.replace(relative, original, changed)
                self.assertTrue(self.check(validator.validate_clarification_history_contracts))
                self.replace(relative, changed, original)

    def test_clarification_protocol_requires_local_guide_and_link(self):
        for skill, (_phase, guide) in validator.CLARIFICATION_GUIDES.items():
            with self.subTest(skill=skill):
                relative = f"skills/{skill}/SKILL.md"
                self.replace(relative, f"]({guide})", "](missing.md)")
                self.assertTrue(self.check(validator.validate_clarification_history_contracts))
                self.replace(relative, "](missing.md)", f"]({guide})")
                path = self.root / "skills" / skill / guide
                original = path.read_bytes()
                path.unlink()
                self.assertTrue(self.check(validator.validate_clarification_history_contracts))
                path.write_bytes(original)

    def test_clarification_protocol_copies_cannot_diverge(self):
        relative = "skills/wewo-erd/references/design-dialogue.md"
        self.replace(relative, "Do not retroactively change what was recommended or said.",
                     "Replace prior recommendations with the latest preference.")
        errors = self.check(validator.validate_clarification_history_contracts)
        self.assertEqual(1, len(errors))
        self.assertIn("clarification-history contract differs", errors[0])

    def test_clarification_original_and_interpretation_boundary_is_required(self):
        for skill, (_phase, guide) in validator.CLARIFICATION_GUIDES.items():
            self.replace(f"skills/{skill}/{guide}", "Interpretation (not verbatim):",
                         "Original answer:")
        errors = self.check(validator.validate_clarification_history_contracts)
        self.assertEqual(2, len(errors))
        self.assertTrue(all("Interpretation (not verbatim)" in error for error in errors))

    def test_clarification_final_gate_and_sensitive_conflict_rules_are_required(self):
        for anchor in (
            "The final document still requires the original explicit final-confirmation\ngate.",
            "Do not silently persist it, silently sanitize it, or call altered\ntext a complete original.",
        ):
            with self.subTest(anchor=anchor):
                for skill, (_phase, guide) in validator.CLARIFICATION_GUIDES.items():
                    self.replace(f"skills/{skill}/{guide}", anchor, "Missing boundary.")
                errors = self.check(validator.validate_clarification_history_contracts)
                self.assertEqual(2, len(errors))
                for skill, (_phase, guide) in validator.CLARIFICATION_GUIDES.items():
                    self.replace(f"skills/{skill}/{guide}", "Missing boundary.", anchor)

    def test_clarification_protocol_markers_must_be_unique_and_ordered(self):
        path = self.root / "skills/wewo-prd/references/clarification-guide.md"
        original = path.read_text(encoding="utf-8")
        start = "<!-- wewo:clarification-history:start -->"
        end = "<!-- wewo:clarification-history:end -->"
        for changed in (
            original.replace(start, ""), original.replace(end, ""),
            original.replace(start, start + start),
            end + original.replace(end, ""),
        ):
            with self.subTest(marker=changed[:80]):
                path.write_text(changed, encoding="utf-8")
                self.assertTrue(self.check(validator.validate_clarification_history_contracts))
        path.write_text(original, encoding="utf-8")

    def test_clarification_legacy_no_write_rule_is_rejected(self):
        path = self.root / "skills/wewo-erd/SKILL.md"
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\nWrite nothing until explicit final confirmation.\n")
        errors = self.check(validator.validate_clarification_history_contracts)
        self.assertEqual(1, len(errors))
        self.assertIn("obsolete exclusive-output or no-write rule", errors[0])

    def test_clarification_allows_reflow_and_stage_specific_guidance(self):
        path = self.root / "skills/wewo-erd/references/design-dialogue.md"
        text = path.read_text(encoding="utf-8")
        start = "<!-- wewo:clarification-history:start -->"
        end = "<!-- wewo:clarification-history:end -->"
        block = text.split(start, 1)[1].split(end, 1)[0]
        text = text.replace(block, "\n" + " ".join(block.split()) + "\n")
        path.write_text(text + "\nAdditional engineering dialogue guidance.\n", encoding="utf-8")
        self.assertEqual([], self.check(validator.validate_clarification_history_contracts))

    def test_requirement_owner_still_needs_its_output(self):
        self.replace(
            "skills/wewo-build/SKILL.md",
            validator.REQUIREMENT_OUTPUT_PREFIX + "implementation-record.md",
            "implementation-record.md",
        )
        self.assertTrue(self.check(validator.validate_artifact_ownership))

    def test_eighth_skill_is_required(self):
        target = (self.root / "skills/wewo-task").resolve()
        target.relative_to(self.root.resolve())
        shutil.rmtree(target)
        self.assertTrue(self.check(validator.validate_skill_structure))

    def test_both_output_modes_are_required(self):
        for skill, artifacts in validator.TASK_OWNED_ARTIFACTS.items():
            for artifact in artifacts:
                with self.subTest(skill=skill, artifact=artifact):
                    relative = f"skills/{skill}/SKILL.md"
                    original = validator.TASK_OUTPUT_PREFIX + artifact
                    self.replace(relative, original, "missing-task-path")
                    self.assertTrue(self.check(validator.validate_artifact_ownership))
                    self.replace(relative, "missing-task-path", original)

    def test_root_only_documents_cannot_move_under_tasks(self):
        for artifact in ("test-cases.md", "prd.md", "technical-design.md",
                         "clarification-history.md", "task-breakdown.md"):
            with self.subTest(artifact=artifact):
                self.append_runtime("wewo-task", validator.TASK_OUTPUT_PREFIX + artifact)
                self.assertTrue(self.check(validator.validate_artifact_ownership))

    def test_task_templates_cannot_add_assignment_fields(self):
        relative = "skills/wewo-task/assets/task-template.md"
        path = self.root / relative
        original = path.read_text(encoding="utf-8")
        for field in ("- Owner: Alice", "- Status: Ready", "| Assignee | Scope |"):
            with self.subTest(field=field):
                path.write_text(original + "\n" + field, encoding="utf-8")
                self.assertTrue(self.check(validator.validate_task_contracts))
        path.write_text(original, encoding="utf-8")

    def test_task_boundaries_cannot_disappear(self):
        cases = (
            ("wewo-task/SKILL.md", "exactly N task definitions"),
            ("wewo-build/references/task-scope.md", "not an approved implementation plan"),
            ("wewo-testcases/references/document-contract.md", "Execution scope"),
            ("wewo-test/references/project-and-matrix.md", "Do not infer missing task labels"),
            ("wewo-review/references/diff-scope-and-context.md", "If reliable isolation is unavailable"),
            ("wewo-context/references/evidence-and-lifecycle.md", "whole-requirement completion claim"),
        )
        for relative, phrase in cases:
            with self.subTest(relative=relative):
                self.replace("skills/" + relative, phrase, "omitted")
                self.assertTrue(self.check(validator.validate_task_contracts))
                self.replace("skills/" + relative, "omitted", phrase)

    def test_task_is_included_in_runtime_independence_checks(self):
        self.append_runtime("wewo-build", "Invoke wewo-task first.")
        self.assertTrue(self.check(validator.validate_no_cross_skill_routing))

    def test_ninth_skill_is_required(self):
        target = (self.root / "skills/wewo-change").resolve()
        target.relative_to(self.root.resolve())
        shutil.rmtree(target)
        self.assertTrue(self.check(validator.validate_skill_structure))
        self.assertTrue(self.check(validator.validate_change_contracts))

    def test_change_requires_explicit_policy_in_correct_section(self):
        path = self.root / "skills/wewo-change/agents/openai.yaml"
        original = path.read_text(encoding="utf-8")
        for changed in (
            original.replace("allow_implicit_invocation: false", "allow_implicit_invocation: true"),
            original.replace("policy:\n  allow_implicit_invocation: false", ""),
            original.replace("policy:", "dependencies:"),
            original + "\npolicy:\n  allow_implicit_invocation: false\n",
            original + "  allow_implicit_invocation: true\n",
        ):
            with self.subTest(metadata=changed):
                path.write_text(changed, encoding="utf-8")
                errors = self.check(validator.validate_change_contracts)
                self.assertTrue(any("explicit-only" in error for error in errors))
        path.write_text(original, encoding="utf-8")
        self.assertEqual([], self.check(validator.validate_change_contracts))

    def test_change_output_cannot_move_outside_selected_task(self):
        relative = "skills/wewo-change/SKILL.md"
        correct = validator.TASK_OUTPUT_PREFIX + "change-requests/CR-<number>.md"
        wrong = validator.REQUIREMENT_OUTPUT_PREFIX + "change-requests/CR-<number>.md"
        self.replace(relative, correct, wrong)
        self.assertTrue(self.check(validator.validate_artifact_ownership))
        self.assertTrue(self.check(validator.validate_change_contracts))
        self.replace(relative, wrong, correct)
        # Keeping the valid path must not allow an additional root CR path.
        self.append_runtime("wewo-change", "Write " + wrong)
        self.assertTrue(self.check(validator.validate_change_contracts))

    def test_change_cannot_lose_authority_or_history_boundaries(self):
        relative = "skills/wewo-change/SKILL.md"
        for old, new in (
            ("Never write `clarification-history.md`", "Also write `clarification-history.md`"),
            ("Every new CR is **Pending decision**", "Every new CR is **Approved**"),
            ("update only the specified existing CR", "create a new CR for every supplement"),
            ("updating a\nCR does not approve PRD/design or authorize implementation",
             "updating a CR approves implementation"),
        ):
            with self.subTest(boundary=old):
                self.replace(relative, old, new)
                self.assertTrue(self.check(validator.validate_change_contracts))
                self.replace(relative, new, old)

    def test_change_numbering_and_write_guards_cannot_be_removed(self):
        relative = "skills/wewo-change/references/request-record.md"
        for old, new in (
            ("highest existing numeric CR suffix plus one", "first unused suffix"),
            ("Different\nTASKs have independent sequences", "All TASKs share a global sequence"),
            ("New files require exclusive creation", "New files may overwrite existing files"),
            ("against the inspected preimage", "without inspecting existing content"),
        ):
            with self.subTest(boundary=old):
                self.replace(relative, old, new)
                self.assertTrue(self.check(validator.validate_change_contracts))
                self.replace(relative, new, old)

    def test_change_template_requires_scoped_identity_without_assignment(self):
        path = self.root / "skills/wewo-change/assets/change-request-template.md"
        original = path.read_text(encoding="utf-8")
        for changed in (
            original.replace("# <TASK-ID>/<CR-ID>", "# <CR-ID>"),
            original.replace("If only the derived task split or definitions are wrong",
                             "Always update PRD/ERD first"),
            original + "\n- Owner: Alice\n",
            original + "\n| Assignee | Proposal |\n",
            original + "\n- Approval status: Approved\n",
        ):
            with self.subTest(template=changed[-100:]):
                path.write_text(changed, encoding="utf-8")
                self.assertTrue(self.check(validator.validate_change_contracts))
        path.write_text(original, encoding="utf-8")

    def test_build_task_continue_cannot_bypass_confirmed_baseline(self):
        relative = "skills/wewo-build/references/task-scope.md"
        self.replace(relative, "cannot\noverride those documents", "may override those documents")
        self.assertTrue(self.check(validator.validate_change_contracts))

    def test_task_only_correction_remains_available_without_prd_erd_rewrite(self):
        for relative, old in (
            ("skills/wewo-change/SKILL.md",
             "do not change PRD/design merely to authorize that correction"),
            ("skills/wewo-build/references/task-scope.md",
             "if only derived TASK boundaries or definitions were wrong"),
        ):
            with self.subTest(relative=relative):
                self.replace(relative, old, "require a PRD/ERD rewrite for every task correction")
                self.assertTrue(self.check(validator.validate_change_contracts))
                self.replace(relative,
                             "require a PRD/ERD rewrite for every task correction", old)

    def test_change_does_not_introduce_automatic_skill_routing(self):
        for skill, instruction in (
            ("wewo-build", "Invoke wewo-change automatically on conflict."),
            ("wewo-change", "Invoke wewo-erd now to approve the application."),
        ):
            with self.subTest(skill=skill):
                self.append_runtime(skill, instruction)
                self.assertTrue(self.check(validator.validate_no_cross_skill_routing))

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
        self.replace(".codex-plugin/plugin.json", '"0.4.0"', '"0.3.0"')
        self.assertTrue(self.check(validator.validate_plugin_packaging))


if __name__ == "__main__":
    unittest.main()
