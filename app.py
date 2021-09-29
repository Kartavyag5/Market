from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "9513b0b66a8546799bb12ddb3fb80755"


#give the values of the following variables for connect MySQL db

# username = "root"
# password = "Kart$1798"
# host = "localhost"
# database = "market"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Kart$1798@localhost/market"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

#global variable for get value in all page
Rid = 'no id'

# RID Model
class RID(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    rid = db.Column(db.String(200), unique=True)
    time_started = db.Column(db.DateTime, default=datetime.now)
    time_submitted = db.Column(db.DateTime, nullable=True, default=None)
    
    def __repr__(self):
        return f"{self.rid}"

    def __repr__(self):
        return f"{self.time_started}:{self.time_submitted}"


# Market1 Model
class Market_1(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id),nullable=True)
    money_bet_1 = db.Column(db.Float())
    money_bet_2 = db.Column(db.Float())
    money_bet_3 = db.Column(db.Float())
    money_bet_4 = db.Column(db.Float())
    
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    price_4 = db.Column(db.Float())
    
    bet_1 = db.Column(db.Integer())
    bet_2 = db.Column(db.Integer())
    bet_3 = db.Column(db.Integer())
    bet_4 = db.Column(db.Integer())

    def __repr__(self):
        return f"{self.rid.rid}"



# Market2 Model
class Market_2(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id),nullable=True)
    money_bet_1 = db.Column(db.Float())
    money_bet_2 = db.Column(db.Float())
    money_bet_3 = db.Column(db.Float())
    
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    
    bet_1 = db.Column(db.Integer())
    bet_2 = db.Column(db.Integer())
    bet_3 = db.Column(db.Integer())
    
    def __repr__(self):
        return f"{self.rid.rid}"


# Market3 Model
class Market_3(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id),nullable=True)
    money_bet_1 = db.Column(db.Float())
    money_bet_2 = db.Column(db.Float())
    
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    
    bet_1 = db.Column(db.Integer())
    bet_2 = db.Column(db.Integer())

    def __repr__(self):
        return f"{self.rid.rid}"


db.create_all()

@app.route('/api')
def main():
    return 'Root of Market API'

@app.route('/api/prices')
def prices():
# assume the data that comes from front end:
# {
#   "data": {
#     "market_1": {
#       "option_1": {
#         "price": 4.75,
#         "bet": 2
#       }
#     },
#     "market_2": {
#       "option_1": {
#         "price": 3.75,
#         "bet": 2
#       }
#     }
#   }
# }


    if request.method == 'GET':
        m1 = Market_1.query.all()
        m2 = Market_2.query.all()
        m3 = Market_3.query.all()
        market1 = []
        market2 = []
        market3 = []

        for i in m1:
            market1.append({
                'rid': i.rid,
                'money_bet_1': i.money_bet_1,
                'money_bet_2': i.money_bet_2,
                'money_bet_3': i.money_bet_3,
                'money_bet_4': i.money_bet_4,
                
                'price_1': i.price_1,
                'price_2': i.price_2,
                'price_3': i.price_3,
                'price_4': i.price_4,
                
                'bet_1': i.bet_1,
                'bet_2': i.bet_2,
                'bet_3': i.bet_3,
                'bet_4': i.bet_4,
            })
        
        for j in m2:
            market2.append({
                'rid': j.rid,
                'money_bet_1': j.money_bet_1,
                'money_bet_2': j.money_bet_2,
                'money_bet_3': j.money_bet_3,
                
                'price_1': j.price_1,
                'price_2': j.price_2,
                'price_3': j.price_3,
                
                'bet_1': j.bet_1,
                'bet_2': j.bet_2,
                'bet_3': j.bet_3,
            })
        
        for k in m3:
            market3.append({
                'rid': k.rid,
                'money_bet_1': k.money_bet_1,
                'money_bet_2': k.money_bet_2,
                
                'price_1': k.price_1,
                'price_2': k.price_2,
                
                'bet_1': k.bet_1,
                'bet_2': k.bet_2,
                
            })
           
    return {'market1': market1, 'market2': market2, 'market3': market3} 


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
    body = []
    body.append({'rid':resp.rid, 'time_started':time_started})
    return {'body': body}

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
    return {'body': body}


# run flask app
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
