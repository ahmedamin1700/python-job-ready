import os
from typing import Dict
from dotenv import load_dotenv

import requests


class WeatherClient:

    def __init__(self):
        self.lat = ""
        self.lon = ""
        self.temp = 0.0
        self.windspeed = 0.0
        try:
            self.api_key = os.getenv("WEATHER_API_KEY")
        except ValueError as e:
            print(f"Error: {e}")

    def get_weather(self, city: str) -> Dict:
        link = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid={self.api_key}"
        response = requests.get(link)
        try:
            response.raise_for_status()
            content = response.json()[0]
            self.lon = content["lon"]
            self.lat = content["lat"]
        except requests.exceptions.HTTPError as e:
            print(f"An HTTP error occurred {e}")

        link = f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.lon}&current_weather=true"
        response = requests.get(link)
        try:
            response.raise_for_status()
            content = response.json()
            self.temp = content["current_weather"]["temperature"]
            self.windspeed = content["current_weather"]["windspeed"]
        except requests.exceptions.HTTPError as e:
            print(f"An HTTP error occurred {e}")
        return {"temp": self.temp, "windspeed": self.windspeed}


class CurrencyClient:
    def __init__(self):
        self.rate = 0.0
        try:
            self.api_key = os.getenv("CURRENCY_API_KEY")
        except ValueError as e:
            print(f"Error: {e}")

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        link = f"https://v6.exchangerate-api.com/v6/{self.api_key}/pair/{from_currency}/{to_currency}"
        response = requests.get(link)
        try:
            response.raise_for_status()
            content = response.json()
            self.rate = content["conversion_rate"]
        except requests.exceptions.HTTPError as e:
            print(f"An HTTP error occurred {e}")
        return amount * self.rate
