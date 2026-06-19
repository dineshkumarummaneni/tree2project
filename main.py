

from pathlib import Path
import argparse
import re
import sys


def clean_line(line: str) -> str:
    """Remove tree drawing characters."""
    line = line.rstrip()

    line = re.sub(r"^[│ ]*├── ", "", line)
    line = re.sub(r"^[│ ]*└── ", "", line)

    return line.strip()


def get_depth(line: str) -> int:
    """
    Calculate nesting depth from tree structure.
    Assumes each indentation level uses:
        │   or four spaces.
    """
    depth = 0
    idx = 0

    while idx < len(line):
        if line[idx:idx + 4] == "│   ":
            depth += 1
            idx += 4
        elif line[idx:idx + 4] == "    ":
            depth += 1
            idx += 4
        else:
            break

    return depth



def parse_structure(lines):
    """
    Parse a tree structure like:

    project/
    ├── README.md
    ├── src/
    │   ├── main.py
    │   └── utils/
    │       └── helper.py
    └── tests/

    Returns:
        [
            (Path("project"), True),
            (Path("project/README.md"), False),
            ...
        ]
    """

    paths = []
    stack = []

    for raw in lines:
        line = raw.rstrip("\n")

        if not line.strip():
            continue

        # Ignore pure tree guide lines
        stripped = line.strip()
        if re.fullmatch(r"[│\s]+", stripped):
            continue

        # Root directory
        if not any(token in line for token in ("├──", "└──")):
            name = stripped.rstrip("/")

            if stripped.endswith("/"):
                stack = [name]
                paths.append((Path(name), True))
            else:
                paths.append((Path(name), False))

            continue

        # Determine depth
        prefix = line.split("├──")[
            0
        ] if "├──" in line else line.split("└──")[0]

        depth = len(prefix) // 4

        name = re.sub(
            r"^[ │]*(├──|└──)\s*",
            "",
            line,
        ).strip()

        is_dir = name.endswith("/")

        name = name.rstrip("/")

        while len(stack) > depth + 1:
            stack.pop()

        parent = Path(*stack) if stack else Path()

        current = parent / name

        paths.append((current, is_dir))

        if is_dir:
            if len(stack) == depth + 1:
                stack.append(name)
            else:
                if len(stack) > depth + 1:
                    stack = stack[: depth + 1]
                stack.append(name)

    return paths



def preview(paths, target_dir):
    print("\nStructure Preview")
    print("=" * 60)

    for path, is_dir in paths:
        full_path = target_dir / path
        prefix = "[DIR ]" if is_dir else "[FILE]"
        print(f"{prefix} {full_path}")

    print("=" * 60)


def create_structure(paths, target_dir, dry_run=False):
    created_dirs = 0
    created_files = 0
    skipped_files = 0

    for path, is_dir in paths:
        full_path = target_dir / path

        if dry_run:
            continue

        if is_dir:
            full_path.mkdir(parents=True, exist_ok=True)
            created_dirs += 1
        else:
            full_path.parent.mkdir(parents=True, exist_ok=True)

            if full_path.exists():
                skipped_files += 1
                print(f"SKIP : {full_path}")
                continue

            full_path.touch()
            created_files += 1
            print(f"FILE : {full_path}")

    return {
        "created_dirs": created_dirs,
        "created_files": created_files,
        "skipped_files": skipped_files,
    }


def ask_for_target_directory():
    while True:
        target = input(
            "\nEnter target directory where structure should be created:\n> "
        ).strip()

        if not target:
            print("Directory path cannot be empty.")
            continue

        target_path = Path(target).expanduser().resolve()

        if not target_path.exists():
            create = input(
                f"\nDirectory does not exist:\n{target_path}\nCreate it? [y/N]: "
            ).strip().lower()

            if create == "y":
                target_path.mkdir(parents=True, exist_ok=True)
                return target_path

            continue

        if not target_path.is_dir():
            print("Specified path is not a directory.")
            continue

        return target_path


def load_structure_file(structure_file):
    with open(structure_file, "r", encoding="utf-8") as f:
        return f.readlines()


def main():
    parser = argparse.ArgumentParser(
        description="Create folder/file structure from a tree file."
    )

    parser.add_argument(
        "structure_file",
        nargs="?",
        help="Path to structure file"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview only. Do not create anything."
    )

    args = parser.parse_args()

    structure_file = args.structure_file

    if not structure_file:
        structure_file = input(
            "Enter structure file path:\n> "
        ).strip()

    structure_file = Path(structure_file).expanduser().resolve()

    if not structure_file.exists():
        print(f"Structure file not found:\n{structure_file}")
        sys.exit(1)

    lines = load_structure_file(structure_file)
    paths = parse_structure(lines)

    if not paths:
        print("No valid structure found.")
        sys.exit(1)

    target_dir = ask_for_target_directory()

    preview(paths, target_dir)

    if args.dry_run:
        print("\nDry-run complete. No changes made.")
        sys.exit(0)

    confirm = input(
        "\nCreate this structure? [y/N]: "
    ).strip().lower()

    if confirm != "y":
        print("Operation cancelled.")
        sys.exit(0)

    result = create_structure(
        paths=paths,
        target_dir=target_dir,
        dry_run=False,
    )

    print("\nSummary")
    print("=" * 60)
    print(f"Directories created : {result['created_dirs']}")
    print(f"Files created       : {result['created_files']}")
    print(f"Files skipped       : {result['skipped_files']}")
    print("=" * 60)

    print("\nStructure creation completed successfully.")


if __name__ == "__main__":
    main()

