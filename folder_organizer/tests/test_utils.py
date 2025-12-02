# tests/test_utils.py
import pytest
from pathlib import Path
from utils import organize_folder


def test_organize_files(tmp_path):
    """
    tmp_path is a built-in pytest fixture that creates a temporary directory.
    """
    # 1. Setup: Create dummy files in the temp folder
    (tmp_path / "photo.jpg").touch()
    (tmp_path / "document.pdf").touch()
    (tmp_path / "song.mp3").touch()

    # 2. Action: Run the organizer
    stats = organize_folder(tmp_path, dry_run=False)

    # 3. Assertion: Check if files moved to correct subfolders
    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert (tmp_path / "Documents" / "document.pdf").exists()
    assert (tmp_path / "Audio" / "song.mp3").exists()

    # Check if original files are gone from root
    assert not (tmp_path / "photo.jpg").exists()

    # Check stats
    assert stats["moved"] == 3


def test_dry_run_does_not_move(tmp_path):
    # 1. Setup
    (tmp_path / "test.txt").touch()

    # 2. Action: Run with dry_run=True
    organize_folder(tmp_path, dry_run=True)

    # 3. Assertion: File should still be in root
    assert (tmp_path / "test.txt").exists()
    assert not (tmp_path / "Documents" / "test.txt").exists()
