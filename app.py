from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = "market-secret"

db = SQLAlchemy(app)

#give the values of the following variables for connect MySQL db

# username = 
# password = 
# host = 
# database = 

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{username}:{password}@{host}/{database}"
