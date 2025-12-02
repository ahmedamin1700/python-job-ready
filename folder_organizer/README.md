# Folder Organizer CLI

A robust Python CLI tool that automatically declutters folders by organizing files into categories (Images, Documents, Audio, etc.) based on their extensions.

**Built as part of the Python Job-Ready Roadmap.**

## Features
- **Smart Categorization**: Sorts files into `Images`, `Documents`, `Archives`, `Audio`, `Video`, and `Code`.
- **Dry Run Mode**: Preview changes before actually moving files.
- **Safe**: Skips system files (`main.py`) and directories.

## Installation

Prerequisites: Python 3.10+ and [uv](https://github.com/astral-sh/uv).

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/python-job-ready.git
cd python-job-ready

# Install dependencies
uv sync
```
## Usage

```Bash
# Basic usage (Moves files immediately)
uv run folder_organizer/main.py /path/to/your/messy/folder

# Dry Run (Safe mode - just lists what would happen)
uv run folder_organizer/main.py /path/to/your/messy/folder --dry-run
```

## Running Tests
This project uses pytest to ensure reliability.

```Bash
uv run pytest
```

## Project Structure

```txt
folder_organizer/
├── main.py        # Entry point (CLI Argument Parsing)
├── utils.py       # Core logic (File scanning & moving)
└── tests/         # Unit tests
```
---