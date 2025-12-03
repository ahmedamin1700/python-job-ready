import os
from dotenv import load_dotenv

load_dotenv()


def main():
    print(f"Key loaded: {os.getenv("WEATHER_API_KEY")}")


if __name__ == "__main__":
    main()
