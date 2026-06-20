from pathlib import Path
import re

def parse_structure(lines):
    paths = []
    stack = []


    for raw in lines:
        line = raw.rstrip("\n")

        if not line.strip():
            continue

        stripped = line.strip()

        if re.fullmatch(r"[│\s]+", stripped):
            continue

        if not any(token in line for token in ("├──", "└──")):
            name = stripped.rstrip("/")

            if stripped.endswith("/"):
                stack = [name]
                paths.append((Path(name), True))
            else:
                paths.append((Path(name), False))

            continue

        prefix = (
            line.split("├──")[0]
            if "├──" in line
            else line.split("└──")[0]
        )

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
                stack = stack[: depth + 1]
                stack.append(name)

    return paths

