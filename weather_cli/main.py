import argparse
import sys
from api_clients import WeatherClient, CurrencyClient


def main():
    parser = argparse.ArgumentParser(description="Weather & Currency Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- WEATHER COMMAND ---
    weather_parser = subparsers.add_parser("weather", help="Get current weather")
    weather_parser.add_argument("city", type=str, help="City name")

    # --- CURRENCY COMMAND ---
    currency_parser = subparsers.add_parser("convert", help="Convert currency")
    currency_parser.add_argument("amount", type=float, help="Amount to convert")
    currency_parser.add_argument("base", type=str, help="From Currency (e.g., USD)")
    currency_parser.add_argument("target", type=str, help="To Currency (e.g., EUR)")

    args = parser.parse_args()

    # --- HANDLE WEATHER ---
    if args.command == "weather":
        try:
            client = WeatherClient()
            data = client.get_weather(args.city)

            if "error" in data:
                print(f"Error: {data['error']}")
            else:
                # Extract nice fields from the JSON
                temp = data["temp"]
                wind = data["windspeed"]
                print(f"🌍 Weather in {args.city.title()}:")
                print(f"   🌡️  Temp: {temp}°C")
                print(f"   ☁️  Wind Speed: {wind}")

        except Exception as e:
            print(f"Critical Error: {e}")

    # --- HANDLE CURRENCY ---
    elif args.command == "convert":
        try:
            client = CurrencyClient()
            result = client.convert(args.amount, args.base.upper(), args.target.upper())

            if result is None:
                print("Error: Conversion failed. Check your currency codes.")
            else:
                print(
                    f"💰 {args.amount} {args.base.upper()} = {result:.2f} {args.target.upper()}"
                )

        except Exception as e:
            print(f"Critical Error: {e}")


if __name__ == "__main__":
    main()
