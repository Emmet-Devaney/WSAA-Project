import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("WAQI_API_TOKEN")

BASE_URL = "https://api.waqi.info/feed"

#print(" Token loaded:", "yes" if TOKEN else "NOPE") - for debug

def fetch_city_aqi(city: str):
    url = f"{BASE_URL}/{city}/?token={TOKEN}"
    # print(f"Querying: {url}") - for debug

    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()

        if data["status"] != "ok":
            print(f"No data for '{city}'. Reason: {data.get('data')}")
            return

        aqi = data["data"].get("aqi", "N/A")

        dompol = data["data"].get("dominentpol", "N/A")

        time = data["data"].get("time", {}).get("s", "Unknown")

        print(f"\nCity: {city}")
        print(f"AQI: {aqi}")
        print(f"Dominant pollutant: {dompol}")
        print(f"Updated: {time}")
        print("—" * 40)

    except Exception as e:
        print("Error fetching AQI:", e)


if __name__ == "__main__":
    while True:
        city = input("Enter city name (or 'q' to quit): ").strip()
        if city.lower() == "q":
            break
        fetch_city_aqi(city)
