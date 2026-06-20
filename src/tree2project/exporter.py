
from pathlib import Path


def export_structure(root_path):
    root = Path(root_path)

    if not root.exists():
        raise FileNotFoundError(root)

    lines = [f"{root.name}/"]

    def walk(directory, prefix=""):
        items = sorted(
            directory.iterdir(),
            key=lambda p: (p.is_file(), p.name.lower())
        )

        for idx, item in enumerate(items):
            last = idx == len(items) - 1

            connector = "└── " if last else "├── "

            if item.is_dir():
                lines.append(
                    f"{prefix}{connector}{item.name}/"
                )

                extension = "    " if last else "│   "

                walk(
                    item,
                    prefix + extension
                )
            else:
                lines.append(
                    f"{prefix}{connector}{item.name}"
                )

    walk(root)

    return "\n".join(lines)
