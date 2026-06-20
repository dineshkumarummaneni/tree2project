import argparse

from tree2project.commands.create import (
    run as create_run
)
from tree2project.commands.export import (
    run as export_run
)
from tree2project.commands.validate import (
    run as validate_run
)


def main():
    parser = argparse.ArgumentParser(
        prog="tree2project"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    create_parser = subparsers.add_parser(
        "create",
        help="Create structure"
    )

    create_parser.add_argument(
        "structure_file"
    )

    create_parser.add_argument(
        "--target"
    )

    create_parser.add_argument(
        "--dry-run",
        action="store_true"
    )

    export_parser = subparsers.add_parser(
        "export",
        help="Export structure"
    )

    export_parser.add_argument(
        "directory"
    )

    export_parser.add_argument(
        "--output"
    )

    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate structure"
    )

    validate_parser.add_argument(
        "structure_file"
    )

    validate_parser.add_argument(
        "--target",
        required=True
    )

    args = parser.parse_args()

    if args.command == "create":
        raise SystemExit(
            create_run(args)
        )

    elif args.command == "export":
        raise SystemExit(
            export_run(args)
        )

    elif args.command == "validate":
        raise SystemExit(
            validate_run(args)
        )

    parser.print_help()


if __name__ == "__main__":
    main()