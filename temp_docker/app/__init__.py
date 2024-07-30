from flask import Flask
from pymongo import MongoClient
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo_client = MongoClient(app.config['MONGODB_URI'])
    app.db = mongo_client.get_default_database()

    from app.routes.person import person_bp
    app.register_blueprint(person_bp, url_prefix='/person')

    return app