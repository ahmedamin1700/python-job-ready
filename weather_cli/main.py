import os
from dotenv import load_dotenv
from api_clients import CurrencyClient, WeatherClient

load_dotenv()


def main():
    weather = WeatherClient()
    data = weather.get_weather("Cairo")

    currency = CurrencyClient()
    amount = currency.convert(100.0, "USD", "EGP")

    print(amount)


if __name__ == "__main__":
    main()
