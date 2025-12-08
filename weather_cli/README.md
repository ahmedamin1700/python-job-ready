# 🌦️ Weather & Currency CLI

Fetches live weather and currency rates using OpenWeatherMap and ExchangeRate APIs. Features caching and secure API key management.

## 🛠️ Setup

1. **Install Dependencies**:
```bash
uv sync
```
Setup Secrets:
Create a .env file in the root directory:

```Ini
OPENWEATHER_API_KEY=your_key_here
CURRENCY_API_KEY=your_key_here
```
💻 Usage

```Bash
uv run weather_cli/main.py weather Cairo
uv run weather_cli/main.py convert 100 USD EUR
```