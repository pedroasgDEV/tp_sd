from flask import Flask
from app.routes.person import person_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(person_bp, url_prefix='/api/person')

    return app