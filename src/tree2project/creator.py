from pathlib import Path

def create_structure(paths, target_dir, dry_run=False):
    target_dir = Path(target_dir)


    created_dirs = []
    created_files = []
    skipped_files = []

    for relative_path, is_dir in paths:
        full_path = target_dir / relative_path

        if dry_run:
            continue

        if is_dir:
            full_path.mkdir(
                parents=True,
                exist_ok=True
            )
            created_dirs.append(str(full_path))
        else:
            full_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            if full_path.exists():
                skipped_files.append(str(full_path))
                continue

            full_path.touch()
            created_files.append(str(full_path))

    return {
        "created_dirs": created_dirs,
        "created_files": created_files,
        "skipped_files": skipped_files,
    }
    
