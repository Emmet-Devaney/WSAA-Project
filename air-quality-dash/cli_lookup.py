from app.waqi import search_stations

def run_cli():
    query = input(" Enter city name to search: ").strip()
    if not query:
        print("No input given.")
        return

    results = search_stations(query)
    if not results:
        print("No matches found.")
        return

    print(f"\nTop matches for '{query}':")
    for r in results:
        if "error" in r:
            print(" Error:", r["error"])
        else:
            print(f" {r['name']} | AQI: {r['aqi']} | ID: {r['id']}")

if __name__ == "__main__":
    run_cli()
