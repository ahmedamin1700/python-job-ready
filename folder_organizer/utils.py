import shutil
from pathlib import Path


def organize_folder(target_folder: Path, dry_run: bool = False):
    """
    Scans the target folder and moves files into subfolders based on extensions.
    """
    # 1. Define the rules
    EXTENSION_MAP = {
        "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"},
        "Documents": {".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".md"},
        "Archives": {".zip", ".rar", ".tar", ".gz", ".7z"},
        "Audio": {".mp3", ".wav", ".flac", ".aac"},
        "Video": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
        "Code": {".py", ".js", ".html", ".css", ".java", ".cpp"},
    }

    # 2. Iterate over items
    stats = {"moved": 0, "skipped": 0}

    for item in target_folder.iterdir():
        # Safety checks: Skip dirs and this script
        if item.is_dir() or item.name in ["main.py", "utils.py"]:
            continue

        # 3. Determine Category
        file_ext = item.suffix.lower()
        destination_name = "Others"  # Default

        for category, extensions in EXTENSION_MAP.items():
            if file_ext in extensions:
                destination_name = category
                break

        # 4. Define paths
        target_dir = target_folder / destination_name
        target_file = target_dir / item.name

        # 5. Action
        print(
            f"[{'DRY-RUN' if dry_run else 'MOVE'}] {item.name} -> {destination_name}/"
        )

        if not dry_run:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_file))
            stats["moved"] += 1

    return stats
