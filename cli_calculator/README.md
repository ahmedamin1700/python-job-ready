# CLI Calculator with History

A Python CLI tool that performs basic arithmetic and persists calculation history to a JSON file.

## Features
- **Math**: Add, Subtract, Multiply, Divide.
- **Safety**: Handles division by zero gracefully.
- **Persistence**: Saves every calculation to `history.json` automatically.
- **Audit**: View or clear history via CLI commands.

## Usage

```bash
# Math
python -m cli_calculator.main add 10 5
python -m cli_calculator.main div 10 2

# History
python -m cli_calculator.main history
python -m cli_calculator.main clear
🧪 Testing
```

```Bash
uv run python -m pytest
```