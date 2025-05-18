from flask import Blueprint, request, render_template

bp = Blueprint("core", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        result = f"You entered: {city}"  # Temporary response
    return render_template("index.html", result=result)
