from flask import Blueprint, request, render_template, jsonify
from app.waqi import fetch_aqi, search_stations

bp = Blueprint("core", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            result = fetch_aqi(city)
    return render_template("index.html", result=result)

@bp.get("/search")
def search():
    q = request.args.get("q", "").strip()
    return jsonify(search_stations(q)), 200

@bp.route("/station-search", methods=["GET", "POST"])
def station_search():
    stations = []
    if request.method == "POST":
        query = request.form.get("query", "").strip()
        if query:
            stations = search_stations(query)
    return render_template("station_search.html", results=stations)
