from flask import Flask, request, jsonify
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
    rid = db.Column(db.Integer, primary_key=True, unique=True)
    time_started = db.Column(db.DateTime, default=datetime.now)
    time_submitted = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"{self.rid}"

    def __repr__(self):
        return f"{self.time_started}:{self.time_submitted}"

# class Question(db.Model):
#     q1 = db.Column(db.Integer, nullable=False)
#     q2 = db.Column(db.Integer, nullable=False)
#     q3 = db.Column(db.Integer, nullable=False)
#     q4 = db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         return f"{self.q1}:{self.q2}:{self.q3}:{self.q4}"

@app.route('/api')
def main():
    return 'Root of Market API'

@app.route('/api/start_survey', methods=['GET', 'POST'])
def start_survey():
    if request.method=='POST':
        Rid = request.form['rid']
        Time_started = request.form['time_started']
        RID_obj = RID(rid=Rid,)
        print(RID_obj)
        db.session.add(RID_obj)  
        db.session.commit()
        
        resp = jsonify({'RID':Rid, 'Time_started':Time_started})
        return resp


# run flask app
if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
