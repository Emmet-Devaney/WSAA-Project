# WSAA PROJECT - Air Quality Dash

A flask-based web application that lets you check a real-time Air-Quality Index (AQI) for any city or WAQI station ID and discover nearby monitoring stations.  
The AQI : **[World Air Quality Index API](https://aqicn.org/api/)**, the app stores snapshots in SQLite, colour-codes results by EPA health bands, and refreshes data on a background schedule (3 hours).

> **Live App:** <https://emmdev.pythonanywhere.com/> (This site will be disabled on Sunday 17 August 2025)

---

## Table of Contents
1. [Features](#features)  
2. [Route](#route)  
3. [Local Server](#local-server)  
4. [Project Structure](#structure)  
5. [References](#references)

---

## Features
| Category | Details |
|----------|---------|
| **City / Station-ID search** | Single search box accepts either “*Dublin*” or a numeric station UID “*2266*”. Backend detects digits and calls `/feed/@<id>/`. |
| **Station Finder** | `/station-search` route lets you keyword-search the WAQI catalogue and lists matching stations with colour-coded AQI badges. |
| **Colour-banded UI** | EPA AQI ranges (Good → Hazardous) drive the badge colour on station lists *and* the highlighted result card on the home page. |
| **Background scheduler** | APScheduler job polls WAQI every 3 h and stores readings in **`AQISnapshot`** for future trend charts. Disabled automatically on PythonAnywhere. |
| **REST mini-API** | `/api/aqi/<query>` returns the same JSON the UI consumes. `/api/search?q=keyword` proxies WAQI’s station search. |
| **SQLite + Flask-Migrate** | Schema versioned by Alembic; `City` and `AQISnapshot` tables created with `flask db upgrade`. |
| **Deployment ready** | Works locally and on the free tier of PythonAnywhere; `.env` and absolute DB path handling built-in. |
| **Styling** | Vanilla CSS (no Bootstrap) keeps the footprint tiny; flex layout and media queries ensure mobile friendliness. |

---

## Route

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET / POST | Search city **or** station ID → returns highlighted AQI card. |
| `/station-search` | GET / POST | Form to search WAQI stations by keyword; shows colour-coded list. |
| `/api/search` | GET | `?q=<keyword>` – JSON list of matching stations. |

---

## Local Server

### Prerequisites
* Python
* WAQI API token (free – sign up at <https://aqicn.org/data-platform/token/>)

### Setup

```bash
# clone repository
git clone https://github.com/Emmet-Devaney/WSAA-Project.git  
cd air-quality-dash

#create & activate virtual environment
python -m venv venv
venv\Scripts\activate

#install required imports on venv
pip install -r requirements.txt

# Create writable instance folder and .env
mkdir instance
echo WAQI_API_TOKEN=your_token_here > .env

# Initialise the DB
$Env:FLASK_APP = "run.py"    # set once per shell when local
flask db init                # first time only
flask db migrate -m "init"
flask db upgrade

# Run it
export FLASK_APP=run.py
flask run
```

Open http://127.0.0.1:5000 in your browser.


## Structure

```bash
air-quality-dash/
│
├── app/
│   ├── __init__.py          # Flask factory, blueprints, scheduler
│   ├── waqi.py              # WAQI API helpers (city OR @id search)
│   ├── scheduler.py         # APScheduler job
│   ├── db.py                # SQLAlchemy instance
│   ├── models/              
│   │   ├── city.py          # SQLAlchemy model for each location tracked (`id`, `name`, `country`, optional WAQI UID).  
│   │   └── aqi_snapshot.py  # Historical readings table; hourly AQI + pollutant, FK → `City`.  
│   └── routes/
│       ├── __init__.py      # core blueprint (index + station-search + API)
│
├── templates/               
│   ├── index.html
│   └── station_search.html
│
├── static/css/style.css     # styling
├── instance/                # local.db lives here
├── .env                     # WAQI_API_TOKEN
├── .gitignore                
├── requirements.txt         # necessary imports
├── run.py                   # entry point
└── README.md

```

# References

| Topic                                       | Link                                                                                                             |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| WAQI API                                    | [https://aqicn.org/api/](https://aqicn.org/api/)                                                                 |
| EPA AQI health bands                        | [https://www.airnow.gov/aqi/aqi-basics/](https://www.airnow.gov/aqi/aqi-basics/)                                 |
| Flask Blueprints                            | [https://flask.palletsprojects.com/en/3.0.x/blueprints/](https://flask.palletsprojects.com/en/3.0.x/blueprints/) |
| Flask-Migrate / Alembic                     | [https://flask-migrate.readthedocs.io/en/latest/](https://flask-migrate.readthedocs.io/en/latest/)               |
| APScheduler – BackgroundScheduler           | [https://apscheduler.readthedocs.io/en/3.x/index.html](https://apscheduler.readthedocs.io/en/3.x/index.html)     |


## File & Directory Reference

| Path | Purpose | Key Docs / Guides |
|------|---------|-------------------|
| **templates/index.html** | Jinja-powered home page: search form & highlighted result card | • Jinja2 Template Basics → <https://jinja.palletsprojects.com/en/3.1.x/templates/> |
| **app/scheduler.py** | APScheduler job that polls WAQI every 3 h and writes snapshots | • APScheduler BackgroundScheduler → <https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/background.html> |
| **app/db.py** | Creates the singleton `SQLAlchemy()` object used across the app | • Flask-SQLAlchemy Quickstart → <https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/> |
| **app/models/city.py** | `City` table: id, name, country, optional WAQI uid | • SQLAlchemy ORM Mapping → <https://docs.sqlalchemy.org/en/20/orm/mapping_api.html> |
| **app/models/aqi_snapshot.py** | `AQISnapshot` table: FK to `cities`, AQI, pollutant, timestamp | • SQLAlchemy Relationships → <https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html> |
| **app/routes/__init__.py** | Core **Blueprint**: `/` search, `/station-search`, `/api/*` | • Flask Blueprints → <https://flask.palletsprojects.com/en/3.0.x/blueprints/> |
| **migrations/** | Alembic scripts generated by Flask-Migrate (`flask db migrate`) | • Flask-Migrate + Alembic Workflow → <https://flask-migrate.readthedocs.io/en/latest/> |
| **instance/** | Runtime-only folder (ignored by Git) holding `local.db` & `.env` | • Flask “Instance” folder pattern → <https://flask.palletsprojects.com/en/3.0.x/config/#instance-folders> |
| **static/css/style.css** | Minimal responsive CSS & EPA AQI colour bands | • MDN CSS Flexbox Guide → <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox> |
| **run.py** | App entry point: `from app import create_app; app = create_app()` | • Flask Application Factory pattern → <https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/> |




### Other References
| Topic | Reference | Usage Example |
|-------|-----------|------------|
| Virtual Environments | [Python Docs – Venv](https://docs.python.org/3/library/venv.html) | `venv/`, `.gitignore` |
| API Testing | [Postman Docs – Requests](https://learning.postman.com/docs/sending-requests/requests/) | Manual API testing |
| Markdown Layout | [Github Docs - Organizing information with tables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables)  | README.md |
