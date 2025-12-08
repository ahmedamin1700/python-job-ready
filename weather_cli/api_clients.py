import os
from typing import Dict
from dotenv import load_dotenv

import requests
import time
import json
from pathlib import Path

CACHE_DURATION = 600
CACHE_FILE = Path(".weather-cache.json")

load_dotenv()


class WeatherClient:

    def __init__(self):
        self.cached = []
        self.lat = ""
        self.lon = ""
        self.temp = 0.0
        self.windspeed = 0.0
        try:
            self.api_key = os.getenv("WEATHER_API_KEY")
        except ValueError as e:
            print(f"Error: {e}")

    def get_weather(self, city: str) -> Dict:
        city_key = city.lower()
        cache = self._load_cache()
        if city_key in cache:
            cached_entry = cache[city_key]
            age = time.time() - cached_entry["timestamp"]

            if age < CACHE_DURATION:
                print(f"(Using Cache) Data is {int(age)}s old.")
                return cached_entry["data"]
            else:
                print("Cache expired. Fetching fresh data...")

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
            data = {"temp": self.temp, "windspeed": self.windspeed}
            self._save_cache(city, data)
        except requests.exceptions.HTTPError as e:
            print(f"An HTTP error occurred {e}")
        return {"temp": self.temp, "windspeed": self.windspeed}

    def _load_cache(self) -> dict:
        """Reads the cache file safely."""
        if not CACHE_FILE.exists():
            return {}

        try:
            with open(CACHE_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return {}

    def _save_cache(self, city: str, data: dict):
        """Updates the cache with new data for a specific city."""
        cache = self._load_cache()

        city_key = city.lower()

        cache[city_key] = {"timestamp": time.time(), "data": data}
        with open(CACHE_FILE, "w") as file:
            json.dump(cache, file, indent=4)


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
