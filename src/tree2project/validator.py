from pathlib import Path


def validate_structure(paths, target_dir):
    target_dir = Path(target_dir)

    missing = []

    for relative_path, is_dir in paths:
        full_path = target_dir / relative_path

        if not full_path.exists():
            missing.append(str(full_path))
            continue

        if is_dir and not full_path.is_dir():
            missing.append(str(full_path))

        if not is_dir and not full_path.is_file():
            missing.append(str(full_path))

    return {
        "valid": len(missing) == 0,
        "missing": missing,
    }
