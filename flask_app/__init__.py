from flask import Flask
import os
from flask_cors import CORS
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_app.app1 import app1



load_dotenv()
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(app1)
    db.init_app(app)
    cors = CORS(app)
    return app

# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True