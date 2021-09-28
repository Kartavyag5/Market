from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "9513b0b66a8546799bb12ddb3fb80755"


username = "root"
password = ""
host = "localhost"
database = "market"

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/market"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# global variable for get value in all page
Rid = 'no id'




# RID Model
class RID(db.Model):
    rid = db.Column(db.String(200), primary_key=True, unique=True)
    time_started = db.Column(db.DateTime, default=datetime.now)
    time_submitted = db.Column(db.DateTime,nullable=True, default=None)
    
    def __repr__(self):
        return f"{self.rid}"

    def __repr__(self):
        return f"{self.time_started}:{self.time_submitted}"




# Market Model
class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    rid = db.Column(db.String(200), unique=True, primary_key=True)
    market_name = db.Column(db.String(255), nullable=False, unique=True)
    money_bet = db.Column(db.Float(), default=10)
    prices = db.Column(db.Float())
    bets = db.Column(db.Integer())

    def __repr__(self):
        return f"{self.market_name}"

db.create_all()

@app.route('/api')
def main():
    return 'Root of Market API'


# Default prices Of the Market
@app.route('/api/prices')
def prices():
    if request.method == 'GET':
        market = Market.query.all()
        all_market = []

        for i in market:
            option = Market.query.filter_by(market=i.id)
            count = option.count()
            for j in option:
                j.prices = 1/count
                db.session.commit()
                all_market.append({
                    'id': i.id, 
                    'rid': j.rid,
                    'market': j.market_name,
                    'money_bet': j.money_bet,
                    'prices': j.prices,
                    'bets': j.bets,
                })
            
    return {'all-markets':all_market}   



# Start Survey
@app.route('/api/start_survey', methods=['POST'])
def start_survey():
    # when you give rid in post request, every time new rid obj created with datetime.now()
    # you have to give unique rid in request.
    if request.method=='POST':
        global Rid
        Rid = request.form['rid']
        time_started = datetime.now()
        
        RID_obj = RID(rid=Rid)
        db.session.add(RID_obj)  
        db.session.commit()

    # this query will return the last created rid object
    resp= RID.query.filter_by(rid=Rid).first()
    body=[]
    body.append({'rid':resp.rid, 'time_started':time_started,})
    return {'body': body}




# End Survey
@app.route('/api/end_survey', methods=['GET'])
def end_survey():
    if request.method == 'GET':
        # Rid = request.form['rid']
        time_ended = datetime.now()

        # RID_obj = RID(rid=Rid)
        # db.session.add(RID_obj)
    resp= RID.query.filter_by(rid=Rid).first()

    if resp:
        resp.time_submitted = datetime.now()
        db.session.commit()
    else:
        return {'msg':'id not found'}

    body = []

    body.append({'rid':resp.rid, 'time_ended':resp.time_submitted})
    return {'body':body}




# run flask app
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
