import argparse
import sys
from pathlib import Path

# Import the function we just wrote
from utils import organize_folder


def main():
    parser = argparse.ArgumentParser(description="Organize files in a folder.")
    parser.add_argument("path", type=str, help="Path to the folder to organize")
    parser.add_argument(
        "--dry-run", action="store_true", help="Simulate without moving files"
    )

    args = parser.parse_args()
    folder_path = Path(args.path)

    if not folder_path.exists():
        print(f"Error: Path '{folder_path}' not found.")
        sys.exit(1)

    print(f"--- Organizing: {folder_path.resolve()} ---")

    # Call the logic
    organize_folder(folder_path, dry_run=args.dry_run)

    print("--- Done! ---")


if __name__ == "__main__":
    main()
