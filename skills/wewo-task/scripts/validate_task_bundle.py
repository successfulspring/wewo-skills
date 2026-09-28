"""Read-only structural validation; semantic coverage/confirmation need review."""

from __future__ import annotations

import argparse
import re
import stat
from pathlib import Path


TASK_ID = re.compile(r"TASK-(?:00[1-9]|0[1-9][0-9]|[1-9][0-9]{2,})\Z")
TASK_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def positive_count(value: str) -> int:
    if not re.fullmatch(r"[1-9][0-9]*", value):
        raise argparse.ArgumentTypeError("count must be an explicit positive integer")
    return int(value)


def reject_link(path: Path) -> None:
    # Windows junctions/reparse points need the same boundary as POSIX symlinks.
    info = path.lstat()
    if path.is_symlink() or getattr(info, "st_file_attributes", 0) & getattr(
        stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400
    ):
        raise ValueError(f"linked bundle path is not allowed: {path}")


def read_regular(path: Path) -> str:
    reject_link(path)
    if not path.is_file():
        raise ValueError(f"expected regular file: {path}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError(f"empty document: {path}")
    return text


def validate_bundle(requirement: Path, count: int) -> list[str]:
    """Inspect only this bundle; never follow arbitrary Markdown references."""
    errors: list[str] = []
    if type(count) is not int or count <= 0:
        return ["count must be an explicit positive integer"]
    try:
        requirement = requirement.absolute()
        # Check before resolve/read, so an escaped path is not accessed first.
        for part in reversed((requirement, *requirement.parents)):
            reject_link(part)
        if not requirement.is_dir():
            raise ValueError(f"expected requirement directory: {requirement}")
        for name in ("prd.md", "technical-design.md"):
            read_regular(requirement / name)
        overview = read_regular(requirement / "task-breakdown.md")
        tasks = requirement / "tasks"
        reject_link(tasks)
        if not tasks.is_dir():
            raise ValueError("tasks must be a directory")
        entries = list(tasks.iterdir())
        ids: set[str] = set()
        for entry in entries:
            reject_link(entry)
            if not entry.is_dir() or not TASK_ID.fullmatch(entry.name):
                errors.append(f"unexpected task directory entry: {entry.name}")
                continue
            ids.add(entry.name)
            try:
                body = read_regular(entry / "task.md")
                first = body.splitlines()[0]
                if not re.match(rf"^# {re.escape(entry.name)}(?:\s|$)", first):
                    errors.append(f"task heading does not match {entry.name}")
            except (OSError, UnicodeError, ValueError) as error:
                errors.append(str(error))
        if len(ids) != count:
            errors.append(f"expected exactly {count} task directories, found {len(ids)}")
        linked: set[str] = set()
        for target in TASK_LINK.findall(overview):
            if "task.md" not in target:
                continue
            match = re.fullmatch(r"tasks/(TASK-[0-9]+)/task\.md", target)
            if match and TASK_ID.fullmatch(match[1]):
                linked.add(match[1])
            elif target.startswith("tasks/"):
                errors.append(f"invalid task link: {target}")
            # Other links may cite authorized external prerequisites. Never
            # follow them or count them as members of this bundle.
        if linked != ids:
            errors.append("overview task links must match all and only the task directories")
    except (OSError, UnicodeError, ValueError) as error:
        errors.append(str(error))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--requirement-dir", type=Path, required=True)
    parser.add_argument("--count", type=positive_count, required=True)
    args = parser.parse_args()
    errors = validate_bundle(args.requirement_dir, args.count)
    if errors:
        print("Task bundle validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Task bundle structure passed: exactly {args.count} tasks. "
          "Confirmation, coverage and cohesion require separate review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
