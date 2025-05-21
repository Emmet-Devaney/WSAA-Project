from app.db import db

class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(2), nullable=False)
    location_id = db.Column(db.Integer, nullable=True)  # optional WAQI station ID

    snapshots = db.relationship("AqiSnapshot", backref="city", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "location_id": self.location_id,
        }
