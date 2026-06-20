from tree2project.parser import (
    parse_structure
)


def test_parse():
    data = [
        "project/\n",
        "├── README.md\n",
        "└── src/\n",
        "    └── main.py\n",
    ]

    result = parse_structure(data)

    assert len(result) == 4