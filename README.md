# Air Quality Dash

The aim here is to build a Flask-based web application that allows users to query real-time air quality information for any city using the World Air Quality Index (WAQI) API (https://aqicn.org/api/), and view the AQI, main pollutant, and timestamp in a clear, interactive interface.

-----------------------


## The App so Far:
- Flask app
- Basic index route and form
- Runs without error on `flask run`
- Currently running on a local database

## How to run

```bash
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

$Env:FLASK_APP = "run.py"
flask run

```


# AQI Lookup

Users can now enter a city name to see:

- Air Quality Index (AQI)
- Dominant pollutant
- Measurement timestamp


## Environment Setup

Create a `.env` file:

```env
WAQI_API_TOKEN=your_token_here

```

### Add CLI Search and README**

> Files added:  
`cli_lookup.py`, `README.md`

# CLI Lookup Tool
A terminal-based tool `cli_lookup.py` is included to let users search for air quality stations using WAQI's search feature.

I may add this to the webpage

### Usage
```bash
python cli_lookup.py
```


