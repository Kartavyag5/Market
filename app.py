from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "9513b0b66a8546799bb12ddb3fb80755"


#give the values of the following variables for connect MySQL db

username = "root"
password = ""
host = "localhost"
database = "market"

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/market'
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


# models
class RID(db.Model):
    rid = db.Column(db.String(200), primary_key=True, unique=True)
    time_started = db.Column(db.DateTime, default=datetime.now)
    time_submitted = db.Column(db.DateTime,nullable=True, default=None)
    
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

@app.route('/api/start_survey', methods=['POST'])
def start_survey():
    # when you give rid in post request, every time new rid obj created with datetime.now()
    # you have to give unique rid in request.
    if request.method=='POST':
        Rid = request.form['rid']
        time_started = datetime.now()
        
        RID_obj = RID(rid=Rid)
        db.session.add(RID_obj)  
        db.session.commit()

    # this query will return the last created rid object
    resp= RID.query.filter_by(rid=Rid).first()
    body=[]
    
    body.append({'rid':resp.rid, 'time_started':time_started})
    return {'body': body}

@app.route('/api/end_survey', methods=['POST'])
def end_survey():
    if request.method == 'POST':
        Rid = request.form['rid']
        time_ended = datetime.now()

        RID_obj = RID(rid=Rid, time_submitted=time_ended)
        db.session.add(RID_obj)
        db.session.commit()

    resp= RID.query.filter_by(rid=Rid).first()
    body = []

    body.append({'rid':resp.rid, 'time_ended':time_ended})
    return {'body':body}


db.create_all()

# run flask app
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
