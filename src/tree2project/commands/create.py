from pathlib import Path

from rich.console import Console
from rich.table import Table

from tree2project.parser import parse_structure
from tree2project.creator import create_structure

console = Console()


def run(args):
    structure_file = Path(args.structure_file)

    if not structure_file.exists():
        console.print(
            f"[red]File not found:[/red] {structure_file}"
        )
        return 1

    with open(
        structure_file,
        "r",
        encoding="utf-8"
    ) as f:
        lines = f.readlines()

    paths = parse_structure(lines)

    target = (
        Path(args.target).expanduser().resolve()
        if args.target
        else Path(
            console.input(
                "Target directory: "
            )
        ).expanduser().resolve()
    )

    table = Table(title="Structure Preview")

    table.add_column("Type")
    table.add_column("Path")

    for path, is_dir in paths:
        table.add_row(
            "DIR" if is_dir else "FILE",
            str(target / path)
        )

    console.print(table)

    if args.dry_run:
        console.print(
            "[yellow]Dry run complete.[/yellow]"
        )
        return 0

    confirm = console.input(
        "Create structure? [y/N]: "
    )

    if confirm.lower() != "y":
        console.print(
            "[yellow]Cancelled[/yellow]"
        )
        return 0

    result = create_structure(
        paths,
        target
    )

    console.print(
        f"[green]Directories:[/green] "
        f"{len(result['created_dirs'])}"
    )

    console.print(
        f"[green]Files:[/green] "
        f"{len(result['created_files'])}"
    )

    console.print(
        f"[yellow]Skipped:[/yellow] "
        f"{len(result['skipped_files'])}"
    )

    return 0
