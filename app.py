from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import MAXYEAR, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "9513b0b66a8546799bb12ddb3fb80755"


#give the values of the following variables for connect MySQL db

# username = "root"
# password = "Kart$1798"
# host = "localhost"
# database = "market"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Kart$1798@localhost/market"
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

#this is data of sum of market all money

#------------Root API------------------
@app.route('/api')
def main():
    return 'Root of Market API'


#-------------Start Survey API-------------------------

@app.route('/api/start_survey', methods=['POST'])
def start_survey():
    # when you give rid in post request, every time new rid obj created with datetime.now()
    # you have to give unique rid in request.
    if request.method=='POST':
        global Rid
        Rid = request.form['rid']
        time_started = datetime.now()
        Rid_check = RID.query.all()
        for i in Rid_check:
            if i.rid == Rid:
                return {'msg':'rid is already used'}
        
        RID_obj = RID(rid=Rid)
        db.session.add(RID_obj)  
        db.session.commit()

    # this is for get the latest price of options in all markets
    m1 = db.session.query(Market_1).order_by(Market_1.id.desc()).first()
    m2 = db.session.query(Market_2).order_by(Market_2.id.desc()).first()
    m3 = db.session.query(Market_3).order_by(Market_3.id.desc()).first()
    market1 = []
    market2 = []
    market3 = []

    
    market1.append({
            'id':1,
            'option1':{
                        'id':11,
                        'money_bet_1':0,
                        'price_1': m1.price_1,
                        'bet_1':0,
                    },

            'option2':{
                        'id':12,
                        'money_bet_2':0,
                        'price_2': m1.price_2,
                        'bet_2':0,
                    },

            'option3':{
                        'id':13,
                        'money_bet_3':0,
                        'price_3': m1.price_3,
                        'bet_3':0,
                    },
                    
            'option4':{
                        'id':14,
                        'money_bet_4':0,
                        'price_4': m1.price_4,
                        'bet_4':0,
                    },
        })
    
    
    market2.append({
            'id':2,
            'option1':{'id':21,'money_bet_1':0,'price_1': m2.price_1,'bet_1':0,},
            'option2':{'id':22,'money_bet_2':0,'price_2': m2.price_2,'bet_2':0,},
            'option3':{'id':23,'money_bet_3':0,'price_3': m2.price_3,'bet_3':0,},
        })
    
    
    market3.append({
            'id':3,
            'option1':{'id':31,'money_bet_1':0,'price_1': m3.price_1,'bet_1':0,},
            'option2':{'id':32,'money_bet_2':0,'price_2': m3.price_2,'bet_2':0,},
        })

    # this query will return the last created rid object
    resp= RID.query.filter_by(rid=Rid).first()
    body = []
    body.append({
            'rid':resp.rid, 
            'time_started':time_started, 
            'market1': market1, 
            'market2': market2, 
            'market3': market3,
            })
            
    return {'body': body}


#------------End survey API--------------------

@app.route('/api/end_survey', methods=['GET'])
def end_survey():
    if request.method == 'POST':
        time_ended = datetime.now()


    resp= RID.query.filter_by(rid=Rid).first()

    if resp:
        resp.time_submitted = datetime.now()
        db.session.commit()
    else:
        return {'msg':'id not found'}

    body = []

    body.append({'rid':resp.rid, 'time_ended':resp.time_submitted})
    return {'body': body}


#----------prices API-------------------

@app.route('/api/prices')
def prices():
    
    # this response is for the testing purpose

    # market = 1
    # option = 2
    # bet = 2

    # market = 1
    # option = 3
    # bet = 3
    #Rid = 1

    #this is for get id of user who start survey
    resp= RID.query.filter_by(rid=Rid).first()
    if not resp:
        return {'msg':'no user started survey'}

    #this is for apply the latest price
    user_bet = Market_1.query.order_by(Market_1.id.desc()).first()

    market1_obj = Market_1(
                    rid=resp.id,
                    money_bet_1= 0,
                    money_bet_2= 2*user_bet.price_2,
                    money_bet_3= 3*user_bet.price_3,
                    money_bet_4= 0,
                    # price_1= price1,
                    # price_2= price2,
                    # price_3= price3,
                    # price_4= price4,
                    bet_1 = 0,
                    bet_2 = 2,
                    bet_3 = 3,
                    bet_4 = 0,
                    )

    db.session.add(market1_obj)  
    db.session.commit()

    #---prices calculation after submit-------

    # all money bet sums for market_1
    sum_money_bet_1 = db.session.query(func.sum(Market_1.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_1.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_1.money_bet_3)).scalar()
    sum_money_bet_4 = db.session.query(func.sum(Market_1.money_bet_4)).scalar()
    
    sum_Market1 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

    #this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market1
    price2 = sum_money_bet_2/sum_Market1
    price3 = sum_money_bet_3/sum_Market1
    price4 = sum_money_bet_4/sum_Market1

    user_bet = Market_1.query.order_by(Market_1.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3
    user_bet.price_4 = price4

    db.session.commit()
    
    # for get the all objects of all market
    m1 = Market_1.query.all()
    m2 = Market_2.query.all()
    m3 = Market_3.query.all()
    market1 = []
    market2 = []
    market3 = []

    for i in m1:
        market1.append({
            'id':1,
            'rid': i.rid,
            'option1':{'id':11,'money_bet_1': i.money_bet_1,'price_1': i.price_1,'bet_1': i.bet_1,},
            'option2':{'id':12,'money_bet_2': i.money_bet_2,'price_2': i.price_2,'bet_2': i.bet_2,},
            'option3':{'id':13,'money_bet_3': i.money_bet_3,'price_3': i.price_3,'bet_3': i.bet_3,},
            'option4':{'id':14,'money_bet_4': i.money_bet_4,'price_4': i.price_4,'bet_4': i.bet_4,},
        })
    
    for j in m2:

        market2.append({
            'id':2,
            'rid': j.rid,
            'option1':{'id':21,'money_bet_1': j.money_bet_1,'price_1': j.price_1,'bet_1': j.bet_1,},
            'option2':{'id':22,'money_bet_2': j.money_bet_2,'price_2': j.price_2,'bet_2': j.bet_2,},
            'option3':{'id':23,'money_bet_3': j.money_bet_3,'price_3': j.price_3,'bet_3': j.bet_3,},
        })

        
    for k in m3:

        market3.append({
            'id':3,
            'rid': k.rid,
            'option1':{'id':31,'money_bet_1': k.money_bet_1,'price_1': k.price_1,'bet_1': k.bet_1,},
            'option2':{'id':32,'money_bet_2': k.money_bet_2,'price_2': k.price_2,'bet_2': k.bet_2,},
        })

           
    return {'market1': market1, 'market2': market2, 'market3': market3}


#-----------run flask app------------------------
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)