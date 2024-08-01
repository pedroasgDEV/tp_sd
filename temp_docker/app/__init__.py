from flask import Flask
from app.utils.database.connection import MongoDB

def create_app():
    app = Flask(__name__)

    # Configurar a conexão com o MongoDB
    mongo = MongoDB()
    mongo.connectDB()
    db = mongo.get_database()

    # Tornar a conexão com o MongoDB disponível para o aplicativo
    app.config['db'] = db

    app.register_blueprint(person_bp, url_prefix='/api/person')

    return app