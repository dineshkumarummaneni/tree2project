from pathlib import Path

from rich.console import Console

from tree2project.parser import parse_structure
from tree2project.validator import (
    validate_structure
)

console = Console()


def run(args):
    structure_file = Path(args.structure_file)

    with open(
        structure_file,
        "r",
        encoding="utf-8"
    ) as f:
        lines = f.readlines()

    paths = parse_structure(lines)

    result = validate_structure(
        paths,
        args.target
    )

    if result["valid"]:
        console.print(
            "[green]Structure valid[/green]"
        )
        return 0

    console.print(
        "[red]Missing paths:[/red]"
    )

    for item in result["missing"]:
        console.print(item)

    return 1