from datetime import datetime
from app.db import db

class AqiSnapshot(db.Model):
    __tablename__ = "aqi_snapshots"

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"), nullable=False)
    pm25 = db.Column(db.Float, nullable=True)
    pm10 = db.Column(db.Float, nullable=True)
    aqi = db.Column(db.Integer, nullable=True)
    pollutant = db.Column(db.String(10), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "pm25": self.pm25,
            "pm10": self.pm10,
            "aqi": self.aqi,
            "pollutant": self.pollutant,
        }
