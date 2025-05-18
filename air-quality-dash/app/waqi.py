import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("WAQI_API_TOKEN")
BASE_URL = "https://api.waqi.info"

def fetch_aqi(city_name):
    url = f"{BASE_URL}/feed/{city_name}/?token={TOKEN}"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()

        if data["status"] != "ok":
            return {"error": "No AQI data found for this city."}

        return {
            "city": city_name,
            "aqi": data["data"].get("aqi"),
            "pollutant": data["data"].get("dominentpol"),
            "time": data["data"].get("time", {}).get("s")
        }
    except Exception as e:
        return {"error": str(e)}

def search_stations(query):
    url = f"{BASE_URL}/search/?keyword={query}&token={TOKEN}"
    try:
        resp = requests.get(url, timeout=10)
        results = resp.json().get("data", [])
        return [
            {
                "id": r.get("uid"),
                "name": r.get("station", {}).get("name"),
                "aqi": r.get("aqi")
            }
            for r in results
        ]
    except Exception as e:
        return [{"error": str(e)}]
