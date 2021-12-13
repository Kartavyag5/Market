import os
from sqlalchemy.sql.expression import true
from dotenv import load_dotenv


load_dotenv()

class Config:
    CORS_HEADERS = 'Content-Type'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = 600
    SESSION_TYPE = 'sqlalchemy'
    
    
