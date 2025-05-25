from apscheduler.schedulers.background import BackgroundScheduler
from app.models.city import City
from app.models.aqi_snapshot import AqiSnapshot
from app.waqi import fetch_aqi
from app.db import db


def _refresh_all():
    for city in City.query.all():
        data = fetch_aqi(city.name)
        if "error" not in data:
            snap = AqiSnapshot(
                city=city,
                aqi=data["aqi"],
                pollutant=data["pollutant"]
            )
            db.session.add(snap)
    db.session.commit()


def init_scheduler(app):
    sched = BackgroundScheduler(timezone="UTC")
    sched.add_job(_refresh_all, "interval", hours=3)
    sched.start()
    app.logger.info("APScheduler started")