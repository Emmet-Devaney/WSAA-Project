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


---

### Polish the Webpage

> Files added:  
`static/style.css`


# More Aesthetic Design

- Added basic CSS in `static/style.css` for cleaner visuals.
- Added project metadata files for clarity.

## Changes
- `style.css` adds padding, fonts, and better layout




## Web Station Search

The app now includes a second route `/station-search` that allows users to look up nearby stations directly in the browser.

## New Route
- `/station-search`: Enter a keyword, view matching stations and AQI

## New Files
- `templates/station_search.html`



# Background Jobs & Database Models

- **New Models Added**  
  Introduced SQLAlchemy models for persistent AQI data:
  - `city.py` – defines a `City` model representing locations.
  - `aqi_snapshot.py` – defines `AQISnapshot`, storing hourly AQI readings tied to a city.

- **Database Integration (Flask-Migrate)**  
  Flask-Migrate is set up to track and apply schema changes using Alembic.  
  To apply migrations:

  ```bash
  flask db init        
  flask db migrate -m "initial schema"
  flask db upgrade
  ```

- **Background Scheduler**  

scheduler.py uses APScheduler to fetch AQI data for saved cities at intervals of an and stores snapshots to the database.