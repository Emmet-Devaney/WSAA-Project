import os
import requests
from dotenv import load_dotenv

# Load WAQI token from .env (local) or environment (production)
load_dotenv()
TOKEN = os.getenv("WAQI_API_TOKEN")
BASE_URL = "https://api.waqi.info"


def fetch_aqi(query):

    # Decide which WAQI endpoint to hit
    endpoint = (
        f"{BASE_URL}/feed/@{query}/"         # station ID
        if str(query).lstrip("-").isdigit()
        else f"{BASE_URL}/feed/{query}/"     # city name
    )
    url = f"{endpoint}?token={TOKEN}"

    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()

        if data["status"] != "ok":
            return {"error": "No AQI data found for this query."}

        iaqi     = data["data"]["iaqi"]
        main_pol = data["data"].get("dominentpol", "n/a").upper()

        return {
            "city":      data["data"]["city"]["name"],
            "aqi":       data["data"]["aqi"],
            "pollutant": main_pol,
            "time":      data["data"]["time"]["s"],
        }

    except Exception as e:
        # Network error, timeout, JSON error, etc.
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
