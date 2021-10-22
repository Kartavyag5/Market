from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from .config import Config

load_dotenv()
#db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    cors = CORS(app)
    #db.init_app(app)
    # db.create_all()
    # app.add_url_rule('/api/start_survey', view_func=utils.initial_values_for_markets)
    #app.add_url_rule('/api/end_survey', view_func=utils.other)
    return app

# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True