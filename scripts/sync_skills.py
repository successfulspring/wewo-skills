"""Synchronize canonical skills to the Codex and Claude Code directories."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import uuid
from pathlib import Path


MIRROR_PATHS = (Path(".agents/skills"), Path(".claude/skills"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy canonical skills/ into the local agent skill mirrors."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Repository root; defaults to the parent of this script directory.",
    )
    return parser.parse_args()


def reject_symbolic_links(source: Path) -> None:
    for current_root, directory_names, file_names in os.walk(
        source, followlinks=False
    ):
        current = Path(current_root)
        for name in [*directory_names, *file_names]:
            candidate = current / name
            if candidate.is_symlink():
                raise RuntimeError(
                    f"Canonical skills must not contain symbolic links: {candidate}"
                )


def assert_safe_mirror(repo_root: Path, mirror: Path) -> None:
    resolved_root = repo_root.resolve()
    resolved_mirror = mirror.resolve(strict=False)
    if resolved_mirror == resolved_root or resolved_root not in resolved_mirror.parents:
        raise RuntimeError(f"Refusing to replace unsafe mirror path: {mirror}")
    if mirror.relative_to(repo_root) not in MIRROR_PATHS:
        raise RuntimeError(f"Unexpected mirror path: {mirror}")


def replace_tree(source: Path, destination: Path) -> None:
    """Replace a mirror using staged copy and rollback on rename failure."""

    destination.parent.mkdir(parents=True, exist_ok=True)
    token = uuid.uuid4().hex
    staging = destination.parent / f".{destination.name}.sync-{token}"
    backup = destination.parent / f".{destination.name}.backup-{token}"

    shutil.copytree(source, staging, copy_function=shutil.copy2)
    moved_existing = False
    try:
        if destination.exists():
            destination.rename(backup)
            moved_existing = True
        staging.rename(destination)
    except Exception:
        if destination.exists() and not moved_existing:
            shutil.rmtree(destination)
        if moved_existing and backup.exists() and not destination.exists():
            backup.rename(destination)
        raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)

    if backup.exists():
        shutil.rmtree(backup)


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    canonical = repo_root / "skills"

    if not canonical.is_dir():
        print(f"ERROR: canonical skills directory does not exist: {canonical}")
        return 1

    reject_symbolic_links(canonical)

    for relative_mirror in MIRROR_PATHS:
        destination = repo_root / relative_mirror
        assert_safe_mirror(repo_root, destination)
        replace_tree(canonical, destination)
        print(f"Synchronized {canonical} -> {destination}")

    print("Synchronization complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
