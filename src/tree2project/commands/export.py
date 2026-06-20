from pathlib import Path

from rich.console import Console

from tree2project.exporter import export_structure

console = Console()


def run(args):
    root = Path(args.directory)

    if not root.exists():
        console.print(
            f"[red]Directory not found:[/red] {root}"
        )
        return 1

    structure = export_structure(root)

    if args.output:
        with open(
            args.output,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(structure)

        console.print(
            f"[green]Saved:[/green] {args.output}"
        )
    else:
        console.print(structure)

    return 0