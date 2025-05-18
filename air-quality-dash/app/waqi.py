import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("WAQI_API_TOKEN")

def fetch_aqi(city_name):
    url = f"https://api.waqi.info/feed/{city_name}/?token={TOKEN}"
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
