from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import pymysql
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "9513b0b66a8546799bb12ddb3fb80755"


#give the values of the following variables for connect MySQL db

# username = "root"
# password = "Creole@123"
# host = "localhost"
# database = "market"

# app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:'Creole@123'@localhost/market"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


# models
class RID(db.Model):
    rid = db.Column(db.String(255), unique=True, nullable=False)
    time_started = db.Column(db.DateTime, default=datetime.datetime.now)
    time_submitted = db.Column(db.DateTime, default=datetime.datetime.now)
    
    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.time_started}:{self.time_submitted}"

class Question(db.Model):
    q1 = db.Column(db.Integer, nullable=False)
    q2 = db.Column(db.Integer, nullable=False)
    q3 = db.Column(db.Integer, nullable=False)
    q4 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.q1}:{self.q2}:{self.q3}:{self.q4}"


db.create_all()

# run flask app
if __name__ == '__main__':
    app.run(debug=True)
