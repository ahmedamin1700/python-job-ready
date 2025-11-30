# folder_organizer/main.py
import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Organize files in a folder.")

    # Arguments
    parser.add_argument("path", type=str, help="Path to the folder to organize")
    parser.add_argument(
        "--dry-run", action="store_true", help="Simulate without moving files"
    )

    args = parser.parse_args()

    folder_path = Path(args.path)

    # Basic Validation
    if not folder_path.exists():
        print(f"Error: Path '{folder_path}' not found.")
        sys.exit(1)

    print(f"Scanning: {folder_path.resolve()}")
    if args.dry_run:
        print("--- DRY RUN MODE ---")


if __name__ == "__main__":
    main()
