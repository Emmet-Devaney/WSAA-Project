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
