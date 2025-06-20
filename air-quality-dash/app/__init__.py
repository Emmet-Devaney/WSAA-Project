import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.db import db

migrate = Migrate()

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "..", "static")
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///local.db"
    #app.config["SQLALCHEMY_DATABASE_URI"] = (
        #"sqlite:////home/EmmDev/air-quality-dash/instance/local.db"
    #)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    def aqi_band(value):
        try:
            v = int(value)
        except (TypeError, ValueError):
            return "unknown"
        if v <= 50:   return "good"
        if v <= 100:  return "moderate"
        if v <= 150:  return "usg"
        if v <= 200:  return "unhealthy"
        if v <= 300:  return "very-unhealthy"
        return "hazardous"

    app.jinja_env.globals["aqi_band"] = aqi_band

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    from .routes import bp
    app.register_blueprint(bp)

    # Background scheduler
    if not app.testing:
        from .scheduler import init_scheduler
        init_scheduler(app)

    # Import models so Flask-Migrate can detect them
    from app.models import city, aqi_snapshot

    return app



app = create_app()