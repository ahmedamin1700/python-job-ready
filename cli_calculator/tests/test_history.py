import json
import history


def test_save_and_load_history(tmp_path):
    """
    tmp_path creates a temporary folder that deletes itself after the test.
    """
    # 1. TRICK: Point the history module to a fake file in the temp folder
    fake_file = tmp_path / "test_history.json"
    history.HISTORY_FILE = fake_file

    # 2. Action: Save a record
    history.save_record("add", 2.0, 3.0, 5.0)

    # 3. Assertion: Check if it loaded back correctly
    records = history.load_history()
    assert len(records) == 1
    assert records[0]["operation"] == "add"
    assert records[0]["result"] == 5.0


def test_clear_history(tmp_path):
    # 1. Setup
    fake_file = tmp_path / "test_history.json"
    history.HISTORY_FILE = fake_file

    # Create a dummy file manually
    fake_file.write_text("[]")
    assert fake_file.exists()

    # 2. Action
    history.clear_history()

    # 3. Assertion
    assert not fake_file.exists()
