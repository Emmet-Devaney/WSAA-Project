
from flask import Flask
import os

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates")) # exact location needs to be specified
    )

    from .routes import bp as core_bp
    app.register_blueprint(core_bp)

    return app