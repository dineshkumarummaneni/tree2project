from pathlib import Path

from tree2project.exporter import (
    export_structure
)


def test_export(tmp_path):
    root = tmp_path / "sample"

    root.mkdir()

    (root / "README.md").touch()

    output = export_structure(root)

    assert "README.md" in output