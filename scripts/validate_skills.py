"""Validate the portable wewo-skills repository and synchronized mirrors (V2).

Check groups:

A. Reliable static invariants
- required repository files;
- exactly the expected six skills;
- SKILL.md structure and frontmatter;
- distinct skill descriptions;
- valid local Markdown references;
- no legacy numbered workflow filenames in canonical runtime trees;
- no cross-skill runtime routing to another named wewo-* capability;
- runtime self-containment (no shared/ or specs/ dependency);
- Build invariants (no Testplan artifacts / adjustment contracts);
- Testplan invariants (no removed TDD / automation / execution-stage markers);
- Test invariants (no Build/Review process artifacts as standard inputs);
- artifact ownership output contracts;
- canonical/mirror equality.

B. Useful contract heuristics
- Testplan execution-tool boundary marker present;
- Review input-exclusion heuristic (forbidden artifact names only inside the
  approved negative statement).

C. Runtime behavior explicitly NOT statically provable
- whether a test ever uses a fixed wait;
- whether production code is ever modified;
- whether Required Evidence Level is ever downgraded.

Those are runtime acceptance concerns and are not asserted here.
"""

from __future__ import annotations

import hashlib
import os
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse


EXPECTED_SKILLS = (
    "wewo-prd",
    "wewo-erd",
    "wewo-testplan",
    "wewo-build",
    "wewo-review",
    "wewo-test",
)
MIRROR_PATHS = (Path(".agents/skills"), Path(".claude/skills"))
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
METADATA_PATH_PATTERN = re.compile(
    r'(?m)^\s*(?:icon_small|icon_large):\s*["\']([^"\']+)["\']\s*$'
)
SLASH_COMMAND_PATTERN = re.compile(r"(?m)^\s*/[a-z][a-z0-9-]*(?:\s|$)")
HOST_COMMAND_PATTERN = re.compile(
    r"\b(?:powershell|cmd\.exe|osascript|apt-get|homebrew|brew install)\b",
    re.IGNORECASE,
)
HOST_CAPABILITY_PATTERN = re.compile(
    r"\b(?:subagents?|browser control|mcp tools?|proprietary metadata)\b",
    re.IGNORECASE,
)
DEPENDENCY_PATTERN = re.compile(
    r"\b(?:must|required?|requires?|depend(?:s|ency)?)\b", re.IGNORECASE
)
ROOT_OUTPUT_PATTERN = re.compile(
    r"\b(?:write|save|store|output|create|generate)\b.{0,100}"
    r"\b(?:repository|project)\s+root\b",
    re.IGNORECASE,
)
STABLE_FILENAMES = (
    "prd.md",
    "technical-design.md",
    "test-plan.md",
    "test-cases.md",
    "implementation-plan.md",
    "implementation-record.md",
    "test-execution.md",
    "manual-test-checklist.md",
    "code-review.md",
    "security-review.md",
)
LEGACY_FILENAMES = (
    "01-prd.md",
    "02-technical-design.md",
    "03-test-plan.md",
    "04-test-cases.md",
    "05-implementation-plan.md",
    "06-implementation-record.md",
    "07-code-review.md",
    "08-security-review.md",
    "09-test-execution.md",
    "10-manual-test-checklist.md",
)
OUTPUT_VERB_PATTERN = re.compile(
    r"\b(?:write|save|store|output|create|generate)\b", re.IGNORECASE
)
WORD_PATTERN = re.compile(r"[a-z][a-z0-9-]+")
STOPWORDS = {
    "and",
    "ask",
    "asks",
    "before",
    "change",
    "for",
    "in",
    "of",
    "or",
    "single",
    "the",
    "to",
    "use",
    "user",
    "when",
}

# V2 architecture contracts.
SKILL_NAMES = set(EXPECTED_SKILLS)
OTHER_SKILL_NAME_PATTERN = re.compile(r"wewo-(?:prd|erd|testplan|build|test|review)")
OWNED_ARTIFACTS = {
    "wewo-prd": ("prd.md",),
    "wewo-erd": ("technical-design.md",),
    "wewo-testplan": ("test-plan.md", "test-cases.md"),
    "wewo-build": ("implementation-plan.md", "implementation-record.md"),
    "wewo-test": ("test-execution.md", "manual-test-checklist.md"),
    "wewo-review": ("code-review.md", "security-review.md"),
}
BUILD_FORBIDDEN_MARKERS = (
    "test-plan.md",
    "test-cases.md",
    "test-case-adjustments",
)
TESTPLAN_FORBIDDEN_MARKERS = (
    "TDD Candidate",
    "TDD Collaboration",
    "TDD Case List",
    "Automation Candidate",
    "E2E Automation Candidate",
    "Suggested Automation Method",
    "Recommended Execution Stage",
)
TESTPLAN_TOOL_BOUNDARY_MARKER = (
    "does not inspect, select, configure, or reason about concrete test tools, "
    "test runners, browser installations, or execution infrastructure"
)
TEST_FORBIDDEN_PROCESS_ARTIFACTS = (
    "implementation-plan.md",
    "implementation-record.md",
    "code-review.md",
    "security-review.md",
)
REVIEW_FORBIDDEN_INPUTS = (
    "test-plan.md",
    "test-cases.md",
    "implementation-plan.md",
    "implementation-record.md",
    "test-execution.md",
)
SELF_CONTAINMENT_FORBIDDEN = ("shared/", "specs/")


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.checks: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def checked(self, message: str) -> None:
        self.checks.append(message)


def parse_frontmatter(path: Path, validation: Validation) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        validation.error(f"{path}: missing opening YAML frontmatter delimiter")
        return {}, text

    try:
        closing_index = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration:
        validation.error(f"{path}: missing closing YAML frontmatter delimiter")
        return {}, text

    values: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:closing_index], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):\s*(.+)", line)
        if not match:
            validation.error(f"{path}:{line_number}: unsupported YAML syntax")
            continue
        key, value = match.groups()
        if key in values:
            validation.error(f"{path}:{line_number}: duplicate frontmatter key {key}")
            continue
        value = value.strip()
        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {'"', "'"}
        ):
            value = value[1:-1]
        if not value:
            validation.error(f"{path}:{line_number}: empty frontmatter value")
        values[key] = value

    if set(values) != {"name", "description"}:
        validation.error(
            f"{path}: frontmatter must contain only name and description"
        )

    body = "\n".join(lines[closing_index + 1 :])
    return values, body


def validate_skill_structure(
    repo_root: Path, validation: Validation
) -> dict[str, str]:
    canonical = repo_root / "skills"
    if not canonical.is_dir():
        validation.error(f"Missing canonical skills directory: {canonical}")
        return {}

    actual_skills = sorted(
        path.name for path in canonical.iterdir() if path.is_dir()
    )
    if actual_skills != sorted(EXPECTED_SKILLS):
        validation.error(
            "Canonical skill directories differ from the expected six: "
            f"{actual_skills}"
        )

    descriptions: dict[str, str] = {}
    for skill_name in EXPECTED_SKILLS:
        skill_dir = canonical / skill_name
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            validation.error(f"Missing SKILL.md: {skill_file}")
            continue

        metadata, body = parse_frontmatter(skill_file, validation)
        declared_name = metadata.get("name", "")
        description = metadata.get("description", "")

        if not NAME_PATTERN.fullmatch(declared_name):
            validation.error(f"{skill_file}: invalid skill name {declared_name!r}")
        if declared_name != skill_name:
            validation.error(
                f"{skill_file}: name {declared_name!r} does not match directory"
            )
        if len(description.split()) < 12:
            validation.error(f"{skill_file}: description is not sufficiently scoped")
        descriptions[skill_name] = description

        validate_portability(skill_file, body, validation)

    validation.checked("Canonical skill structure and frontmatter")
    return descriptions


def validate_distinct_descriptions(
    descriptions: dict[str, str], validation: Validation
) -> None:
    normalized: dict[str, set[str]] = {}
    for name, description in descriptions.items():
        normalized[name] = {
            word
            for word in WORD_PATTERN.findall(description.lower())
            if word not in STOPWORDS
        }

    if len({description.casefold() for description in descriptions.values()}) != len(
        descriptions
    ):
        validation.error("Skill descriptions must not be duplicates")

    token_counts = Counter(token for tokens in normalized.values() for token in tokens)
    for name, tokens in normalized.items():
        if not any(token_counts[token] == 1 for token in tokens):
            validation.error(f"{name}: description has no unique scope language")

    names = list(normalized)
    for index, left_name in enumerate(names):
        for right_name in names[index + 1 :]:
            left = normalized[left_name]
            right = normalized[right_name]
            union = left | right
            similarity = len(left & right) / len(union) if union else 1.0
            if similarity >= 0.70:
                validation.error(
                    f"{left_name} and {right_name} descriptions overlap too much "
                    f"({similarity:.0%})"
                )

    validation.checked("Distinct scope for all six skill descriptions")


def validate_portability(
    skill_file: Path, body: str, validation: Validation
) -> None:
    if SLASH_COMMAND_PATTERN.search(body):
        validation.error(f"{skill_file}: core workflow contains a slash command")
    if HOST_COMMAND_PATTERN.search(body):
        validation.error(f"{skill_file}: core workflow contains a host-specific command")

    for line_number, line in enumerate(body.splitlines(), start=1):
        if HOST_CAPABILITY_PATTERN.search(line) and DEPENDENCY_PATTERN.search(line):
            validation.error(
                f"{skill_file}: body line {line_number} requires a host capability"
            )

    if ROOT_OUTPUT_PATTERN.search(body):
        validation.error(
            f"{skill_file}: workflow is configured to write to a repository root"
        )

    for line_number, line in enumerate(body.splitlines(), start=1):
        if (
            any(filename in line for filename in STABLE_FILENAMES)
            and OUTPUT_VERB_PATTERN.search(line)
            and "docs/wewo/" not in line
        ):
            validation.error(
                f"{skill_file}: body line {line_number} configures a workflow "
                "filename without the requirement workspace"
            )


def candidate_reference(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    target = unquote(target).split("#", 1)[0]
    if not target or target.startswith("#"):
        return None
    parsed = urlparse(target)
    if parsed.scheme or target.startswith("//"):
        return None
    if "<" in target or ">" in target or "..." in target:
        return None
    return target


def validate_local_references(repo_root: Path, validation: Validation) -> None:
    markdown_files = [
        path
        for path in repo_root.rglob("*.md")
        if ".agents" not in path.parts and ".claude" not in path.parts
    ]

    for markdown_file in markdown_files:
        text = markdown_file.read_text(encoding="utf-8")
        raw_targets = [
            match.group(1) for match in MARKDOWN_LINK_PATTERN.finditer(text)
        ]

        for raw_target in raw_targets:
            target = candidate_reference(raw_target)
            if target is None:
                continue
            target_path = Path(target)
            candidates = (
                [target_path]
                if target_path.is_absolute()
                else [markdown_file.parent / target_path, repo_root / target_path]
            )
            if not any(candidate.exists() for candidate in candidates):
                validation.error(
                    f"{markdown_file}: referenced local path does not exist: {target}"
                )

    for skill_name in EXPECTED_SKILLS:
        skill_dir = repo_root / "skills" / skill_name
        metadata_file = skill_dir / "agents/openai.yaml"
        if not metadata_file.is_file():
            continue
        metadata = metadata_file.read_text(encoding="utf-8")
        for match in METADATA_PATH_PATTERN.finditer(metadata):
            target = candidate_reference(match.group(1))
            if target is not None and not (skill_dir / target).exists():
                validation.error(
                    f"{metadata_file}: referenced local path does not exist: {target}"
                )

    validation.checked("Local file references")


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_snapshot(root: Path, validation: Validation) -> dict[str, tuple[str, str]]:
    snapshot: dict[str, tuple[str, str]] = {}
    if not root.is_dir():
        validation.error(f"Missing synchronized skills directory: {root}")
        return snapshot

    for current_root, directory_names, file_names in os.walk(
        root, followlinks=False
    ):
        current = Path(current_root)
        for name in directory_names:
            path = current / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                validation.error(f"Symbolic links are not portable: {path}")
            snapshot[relative] = ("directory", "")
        for name in file_names:
            path = current / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                validation.error(f"Symbolic links are not portable: {path}")
            snapshot[relative] = ("file", file_digest(path))
    return snapshot


def validate_mirrors(repo_root: Path, validation: Validation) -> None:
    canonical_snapshot = tree_snapshot(repo_root / "skills", validation)
    for relative_mirror in MIRROR_PATHS:
        mirror = repo_root / relative_mirror
        mirror_snapshot = tree_snapshot(mirror, validation)
        if mirror_snapshot != canonical_snapshot:
            missing = sorted(canonical_snapshot.keys() - mirror_snapshot.keys())
            extra = sorted(mirror_snapshot.keys() - canonical_snapshot.keys())
            changed = sorted(
                path
                for path in canonical_snapshot.keys() & mirror_snapshot.keys()
                if canonical_snapshot[path] != mirror_snapshot[path]
            )
            validation.error(
                f"{mirror} does not match canonical skills "
                f"(missing={missing}, extra={extra}, changed={changed})"
            )

    validation.checked("Codex and Claude Code mirrors match canonical skills")


def validate_required_repository_files(
    repo_root: Path, validation: Validation
) -> None:
    required = [
        repo_root / "README.md",
        repo_root / "shared/global-conventions.md",
        repo_root / "scripts/sync_skills.py",
        repo_root / "scripts/validate_skills.py",
    ]
    for path in required:
        if not path.is_file():
            validation.error(f"Missing required repository file: {path}")

    validation.checked("Required repository files")


def _iter_text_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file():
            yield path


def validate_no_legacy_filenames(repo_root: Path, validation: Validation) -> None:
    for path in _iter_text_files(repo_root / "skills"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name in LEGACY_FILENAMES:
            if name in text:
                validation.error(
                    f"{path}: legacy numbered workflow filename present: {name}"
                )
    validation.checked("No legacy numbered workflow filenames in canonical skills")


def validate_no_cross_skill_routing(
    repo_root: Path, validation: Validation
) -> None:
    for skill_dir in (repo_root / "skills").iterdir():
        if not skill_dir.is_dir() or skill_dir.name not in SKILL_NAMES:
            continue
        own = skill_dir.name
        for path in _iter_text_files(skill_dir):
            text = path.read_text(encoding="utf-8", errors="ignore")
            for match in OTHER_SKILL_NAME_PATTERN.finditer(text):
                found = match.group(0)
                if found == own:
                    continue
                validation.error(
                    f"{path}: reference to another capability {found}"
                )
    validation.checked("No cross-skill runtime routing in canonical skills")


def validate_self_containment(repo_root: Path, validation: Validation) -> None:
    for path in _iter_text_files(repo_root / "skills"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in SELF_CONTAINMENT_FORBIDDEN:
            if marker in text:
                validation.error(
                    f"{path}: runtime skill depends on maintainer path {marker}"
                )
    validation.checked("Runtime skills are self-contained")


def validate_artifact_ownership(repo_root: Path, validation: Validation) -> None:
    output_prefix = "docs/wewo/<requirement-category>/<requirement-slug>/"
    for skill_name, artifacts in OWNED_ARTIFACTS.items():
        skill_file = repo_root / "skills" / skill_name / "SKILL.md"
        if not skill_file.is_file():
            continue
        body = skill_file.read_text(encoding="utf-8")
        for artifact in artifacts:
            if f"{output_prefix}{artifact}" not in body:
                validation.error(
                    f"{skill_file}: missing required output contract for {artifact}"
                )
    validation.checked("Artifact ownership output contracts")


def validate_build_invariants(repo_root: Path, validation: Validation) -> None:
    for path in _iter_text_files(repo_root / "skills" / "wewo-build"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in BUILD_FORBIDDEN_MARKERS:
            if marker in text:
                validation.error(
                    f"{path}: build declares Testplan artifact or adjustment "
                    f"contract marker: {marker}"
                )
    validation.checked("Build invariants (no Testplan coupling)")


def validate_testplan_invariants(repo_root: Path, validation: Validation) -> None:
    for path in _iter_text_files(repo_root / "skills" / "wewo-testplan"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in TESTPLAN_FORBIDDEN_MARKERS:
            if marker in text:
                validation.error(
                    f"{path}: testplan contains removed contract marker: {marker}"
                )
    validation.checked("Testplan invariants (no TDD/automation/execution-stage)")


def validate_testplan_tool_boundary(
    repo_root: Path, validation: Validation
) -> None:
    skill_file = repo_root / "skills" / "wewo-testplan" / "SKILL.md"
    if skill_file.is_file():
        body = skill_file.read_text(encoding="utf-8")
        normalized = re.sub(r"\s+", " ", body)
        if TESTPLAN_TOOL_BOUNDARY_MARKER not in normalized:
            validation.error(
                f"{skill_file}: missing testplan execution-tool boundary marker"
            )
    validation.checked("Testplan execution-tool boundary contract (heuristic)")


def validate_test_invariants(repo_root: Path, validation: Validation) -> None:
    for path in _iter_text_files(repo_root / "skills" / "wewo-test"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in TEST_FORBIDDEN_PROCESS_ARTIFACTS:
            if marker in text:
                validation.error(
                    f"{path}: test depends on process artifact: {marker}"
                )
    validation.checked("Test invariants (no Build/Review process artifacts)")


def validate_review_invariants(repo_root: Path, validation: Validation) -> None:
    for path in _iter_text_files(repo_root / "skills" / "wewo-review"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        paragraphs = re.split(r"\n\s*\n", text)
        for marker in REVIEW_FORBIDDEN_INPUTS:
            for paragraph in paragraphs:
                if marker in paragraph and (
                    "does not include" not in paragraph
                    and "not include" not in paragraph
                ):
                    validation.error(
                        f"{path}: review declares {marker} as a standard input"
                    )
                    break
    validation.checked("Review invariants (no Testplan/Build-process inputs)")


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    validation = Validation()

    validate_required_repository_files(repo_root, validation)
    descriptions = validate_skill_structure(repo_root, validation)
    validate_distinct_descriptions(descriptions, validation)
    validate_local_references(repo_root, validation)

    validate_no_legacy_filenames(repo_root, validation)
    validate_no_cross_skill_routing(repo_root, validation)
    validate_self_containment(repo_root, validation)
    validate_artifact_ownership(repo_root, validation)
    validate_build_invariants(repo_root, validation)
    validate_testplan_invariants(repo_root, validation)
    validate_testplan_tool_boundary(repo_root, validation)
    validate_test_invariants(repo_root, validation)
    validate_review_invariants(repo_root, validation)

    validate_mirrors(repo_root, validation)

    if validation.errors:
        print(f"Validation failed with {len(validation.errors)} error(s):")
        for error in validation.errors:
            print(f"  - {error}")
        return 1

    print(f"Validation passed ({len(validation.checks)} check groups):")
    for check in validation.checks:
        print(f"  - {check}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
