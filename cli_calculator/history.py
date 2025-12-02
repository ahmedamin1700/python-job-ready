import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List


HISTORY_FILE = Path("history.json")


def load_history() -> List[Dict[str, Any]]:
    """Reads the JSON file and returns the list of records."""
    if not HISTORY_FILE.exists():
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_record(operation: str, a: float, b: float, result: float):
    """Adds a new record to history."""
    history = load_history()

    record = {
        "timestamp": datetime.now().isoformat(),
        "operation": operation,
        "a": a,
        "b": b,
        "result": result,
    }

    history.append(record)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def clear_history():
    """Wipes the history file."""
    if HISTORY_FILE.exists():
        HISTORY_FILE.unlink()
