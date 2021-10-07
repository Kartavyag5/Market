from typing import NamedTuple
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import MAXYEAR, datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = "9513b0b66a8546799bb12ddb3fb80755"


#give the values of the following variables for connect MySQL db

# username = "root"
# password = "Kart$1798"
# host = "localhost"
# database = "market"

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Kart$1798@localhost/market"
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


# all market names:
    # 1. Kodiak Cakes Concept Test
    # 2. Jeopardy!
    # 3. BYU Football
    # 4. No Time To Die
    # 5.
    # 6.
    # 7.
    # 8.
    # 9.
    # 10.


#----------Market1 : Kodiak Cakes Concept Test-------------------------

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


#----------Market2 : Jeopardy!-------------------------

class Market_2(db.Model):
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


#----------Market3 : BYU Football -------------------------

class Market_3(db.Model):
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

    
#----------Market4 : No Time To Die -------------------------

class Market_4(db.Model):
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


# Market5 Model
class Market_5(db.Model):
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


# Market6 Model
class Market_6(db.Model):
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


# Market7 Model
class Market_7(db.Model):
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


# Market8 Model
class Market_8(db.Model):
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


# Market9 Model
class Market_9(db.Model):
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


# Market10 Model
class Market_10(db.Model):
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

db.create_all()

#this is data of sum of market all money

#------------Root API------------------
@app.route('/api')
@cross_origin()
def main():
    return 'Root of Market API'


#-------------Start Survey API-------------------------

@app.route('/api/start_survey', methods=['POST'])
@cross_origin()
def start_survey():

    market1_check = Market_1.query.all()
    
    if not market1_check:
        market1 = Market_1(
                    price_1=0.25,
                    price_2=0.25,
                    price_3=0.25,
                    price_4=0.25,
                    money_bet_1=10,
                    money_bet_2=10,
                    money_bet_3=10,
                    money_bet_4=10,
                    bet_1=0,
                    bet_2=0,
                    bet_3=0,
                    bet_4=0,
        )

        market2 = Market_2(
                    price_1=0.25,
                    price_2=0.25,
                    price_3=0.25,
                    price_4=0.25,
                    money_bet_1=10,
                    money_bet_2=10,
                    money_bet_3=10,
                    money_bet_4=10,
                    bet_1=0,
                    bet_2=0,
                    bet_3=0,
                    bet_4=0,
        )

        market3 = Market_3(
                    price_1=0.25,
                    price_2=0.25,
                    price_3=0.25,
                    price_4=0.25,
                    money_bet_1=10,
                    money_bet_2=10,
                    money_bet_3=10,
                    money_bet_4=10,
                    bet_1=0,
                    bet_2=0,
                    bet_3=0,
                    bet_4=0,
        )
        
        market4 = Market_4(
                    price_1=0.5,
                    price_2=0.5,
                    money_bet_1=10,
                    money_bet_2=10,
                    bet_1=0,
                    bet_2=0,
        )

        market5 = Market_5(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
                    money_bet_1=10,
                    money_bet_2=10,
                    money_bet_3=10,
                    bet_1=0,
                    bet_2=0,
                    bet_3=0,
        )

        market6 = Market_6(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
                    money_bet_1=10,
                    money_bet_2=10,
                    money_bet_3=10,
                    bet_1=0,
                    bet_2=0,
                    bet_3=0,
        )

        market7 = Market_7(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
                    money_bet_1=10,
                    money_bet_2=10,
                    money_bet_3=10,
                    bet_1=0,
                    bet_2=0,
                    bet_3=0,
        )

        market8 = Market_8(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
                    money_bet_1=10,
                    money_bet_2=10,
                    money_bet_3=10,
                    bet_1=0,
                    bet_2=0,
                    bet_3=0,
        )

        market9 = Market_9(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
                    money_bet_1=10,
                    money_bet_2=10,
                    money_bet_3=10,
                    bet_1=0,
                    bet_2=0,
                    bet_3=0,
        )

        market10 = Market_10(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
                    money_bet_1=10,
                    money_bet_2=10,
                    money_bet_3=10,
                    bet_1=0,
                    bet_2=0,
                    bet_3=0,
        )

        db.session.add(market1)  
        db.session.add(market2)  
        db.session.add(market3)
        db.session.add(market4)  
        db.session.add(market5)  
        db.session.add(market6)  
        db.session.add(market7)  
        db.session.add(market8)  
        db.session.add(market9)  
        db.session.add(market10)  
        db.session.commit()

    # when you give rid in post request, every time new rid obj created with datetime.now()
    # you have to give unique rid in request.
    if request.method=='POST':
        global Rid
        Rid = request.form['rid']
        time_started = datetime.now()
        Rid_check = RID.query.all()
        for i in Rid_check:
            if i.rid == Rid:
                return {'message':'rid is already used'}
        
        RID_obj = RID(rid=Rid)
        db.session.add(RID_obj)  
        db.session.commit()

    # this is for get the latest price of options in all markets
    m1 = db.session.query(Market_1).order_by(Market_1.id.desc()).first()
    m2 = db.session.query(Market_2).order_by(Market_2.id.desc()).first()
    m3 = db.session.query(Market_3).order_by(Market_3.id.desc()).first()
    m4 = db.session.query(Market_4).order_by(Market_4.id.desc()).first()
    m5 = db.session.query(Market_5).order_by(Market_5.id.desc()).first()
    m6 = db.session.query(Market_6).order_by(Market_6.id.desc()).first()
    m7 = db.session.query(Market_7).order_by(Market_7.id.desc()).first()
    m8 = db.session.query(Market_8).order_by(Market_8.id.desc()).first()
    m9 = db.session.query(Market_9).order_by(Market_9.id.desc()).first()
    m10 = db.session.query(Market_10).order_by(Market_10.id.desc()).first()
    market1 = []
    market2 = []
    market3 = []
    market4 = []
    market5 = []
    market6 = []
    market7 = []
    market8 = []
    market9 = []
    market10 = []

    market1.append({
            'id':1,
            'option1':{'id':11,'money_bet_1':0,'price_1': m1.price_1,'bet_1':0,},
            'option2':{'id':12,'money_bet_2':0,'price_2': m1.price_2,'bet_2':0,},
            'option3':{'id':13,'money_bet_3':0,'price_3': m1.price_3,'bet_3':0,},     
            'option4':{'id':14,'money_bet_4':0,'price_4': m1.price_4,'bet_4':0,},
        })
    
    market2.append({
            'id':2,
            'option1':{'id':21, 'money_bet_1':0, 'price_1':m2.price_1, 'bet_1':0,},
            'option2':{'id':22, 'money_bet_2':0, 'price_2':m2.price_2, 'bet_2':0,},
            'option3':{'id':23, 'money_bet_3':0, 'price_3':m2.price_3, 'bet_3':0,},
            'option4':{'id':24, 'money_bet_4':0, 'price_4':m2.price_4, 'bet_4':0,},
        })
    
    market3.append({
            'id':3,
            'option1':{'id':31, 'money_bet_1':0, 'price_1':m3.price_1, 'bet_1':0,},
            'option2':{'id':32, 'money_bet_2':0, 'price_2':m3.price_2, 'bet_2':0,},
            'option3':{'id':33, 'money_bet_3':0, 'price_3':m3.price_3, 'bet_3':0,},
            'option4':{'id':34, 'money_bet_4':0, 'price_4':m3.price_4, 'bet_4':0,},
        })
    
    market4.append({
            'id':4,
            'option1':{'id':41, 'money_bet_1':0, 'price_1':m4.price_1, 'bet_1':0,},
            'option2':{'id':42, 'money_bet_2':0, 'price_2':m4.price_2, 'bet_2':0,},
        })

    market5.append({
            'id':5,
            'option1':{'id':51, 'money_bet_1':0, 'price_1':m5.price_1, 'bet_1':0,},
            'option2':{'id':52, 'money_bet_2':0, 'price_2':m5.price_2, 'bet_2':0,},
            'option3':{'id':53, 'money_bet_3':0, 'price_3':m5.price_3, 'bet_3':0,},
        })

    market6.append({
            'id':6,
            'option1':{'id':61, 'money_bet_1':0, 'price_1':m6.price_1, 'bet_1':0,},
            'option2':{'id':62, 'money_bet_2':0, 'price_2':m6.price_2, 'bet_2':0,},
            'option3':{'id':63, 'money_bet_3':0, 'price_3':m6.price_3, 'bet_3':0,},
        })

    market7.append({
            'id':7,
            'option1':{'id':71, 'money_bet_1':0, 'price_1':m7.price_1, 'bet_1':0,},
            'option2':{'id':72, 'money_bet_2':0, 'price_2':m7.price_2, 'bet_2':0,},
            'option3':{'id':73, 'money_bet_3':0, 'price_3':m7.price_3, 'bet_3':0,},
        })

    market8.append({
            'id':8,
            'option1':{'id':81, 'money_bet_1':0, 'price_1':m8.price_1, 'bet_1':0,},
            'option2':{'id':82, 'money_bet_2':0, 'price_2':m8.price_2, 'bet_2':0,},
            'option3':{'id':83, 'money_bet_3':0, 'price_3':m8.price_3, 'bet_3':0,},
        })

    market9.append({
            'id':9,
            'option1':{'id':91, 'money_bet_1':0, 'price_1':m9.price_1, 'bet_1':0,},
            'option2':{'id':92, 'money_bet_2':0, 'price_2':m9.price_2, 'bet_2':0,},
            'option3':{'id':93, 'money_bet_3':0, 'price_3':m9.price_3, 'bet_3':0,},
        })

    market10.append({
            'id':10,
            'option1':{'id':101, 'money_bet_1':0, 'price_1':m10.price_1, 'bet_1':0,},
            'option2':{'id':102, 'money_bet_2':0, 'price_2':m10.price_2, 'bet_2':0,},
            'option3':{'id':103, 'money_bet_3':0, 'price_3':m10.price_3, 'bet_3':0,},
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
            'market4': market4,
            'market5': market5,
            'market6': market6,
            'market7': market7,
            'market8': market8,
            'market9': market9,
            'market10': market10,
            })
            
    return {'body': body, 'message':'new rid created',}


#------------End survey API--------------------

@app.route('/api/end_survey', methods=['GET','POST'])
@cross_origin()
def end_survey():

    if request.method=='POST':
        data = request.get_json()

    #get the rid Object for rid.id
    resp= RID.query.filter_by(rid=Rid).first()

    if resp:
        resp.time_submitted = datetime.now()
        db.session.commit()
    else:
        return {'msg':'id not found'}
    
    # front end response
    fe_respo = dict(data)
    

    # get the last obj of markets.
    market1_last_bet = Market_1.query.order_by(Market_1.id.desc()).first()
    market2_last_bet = Market_2.query.order_by(Market_2.id.desc()).first()
    market3_last_bet = Market_3.query.order_by(Market_3.id.desc()).first()
    market4_last_bet = Market_4.query.order_by(Market_4.id.desc()).first()
    market5_last_bet = Market_5.query.order_by(Market_5.id.desc()).first()
    market6_last_bet = Market_6.query.order_by(Market_6.id.desc()).first()
    market7_last_bet = Market_7.query.order_by(Market_7.id.desc()).first()
    market8_last_bet = Market_8.query.order_by(Market_8.id.desc()).first()
    market9_last_bet = Market_9.query.order_by(Market_9.id.desc()).first()
    market10_last_bet = Market_10.query.order_by(Market_10.id.desc()).first()

    # this for loop iterate over response and classify it with market obj

    for key,value in fe_respo.items():

        option_list = fe_respo[key]['options']

        for i in option_list:

            # -----------------Market_1------------------
            if i['id']==11:
                bet_val = i['bet']
                check_obj = Market_1.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1(
                                rid=resp.id,
                                money_bet_1 = market1_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit() 
                else:
                    check_obj.money_bet_1 = market1_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==12:
                bet_val = i['bet']
                check_obj = Market_1.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1(
                                rid=resp.id,
                                money_bet_2 = market1_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_2 = market1_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()

            if i['id']==13:
                bet_val = i['bet']
                check_obj = Market_1.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1(
                                rid=resp.id,
                                money_bet_3 = market1_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                 
                else:
                    check_obj.money_bet_3 = market1_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    db.session.commit()

            if i['id']==14:
                bet_val = i['bet']
                check_obj = Market_1.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1(
                                rid=resp.id,
                                money_bet_4 = market1_last_bet.price_4 * bet_val,
                                bet_4 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                    
                else:
                    check_obj.money_bet_4 = market1_last_bet.price_4 * bet_val
                    check_obj.bet_4 = bet_val
                    db.session.commit()

            # -----------------Market_2------------------
            if i['id']==21:
                bet_val = i['bet']
                check_obj = Market_2.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2(
                                rid=resp.id,
                                money_bet_1 = market2_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                    
                else:
                    check_obj.money_bet_1 = market2_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==22:
                bet_val = i['bet']
                check_obj = Market_2.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2(
                                rid=resp.id,
                                money_bet_2 = market2_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_2 = market2_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()

            if i['id']==23:
                bet_val = i['bet']
                check_obj = Market_2.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2(
                                rid=resp.id,
                                money_bet_3 = market2_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                  
                else:
                    check_obj.money_bet_3 = market2_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    db.session.commit()

            if i['id']==24:
                bet_val = i['bet']
                check_obj = Market_2.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2(
                                rid=resp.id,
                                money_bet_4 = market2_last_bet.price_4 * bet_val,
                                bet_4 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                  
                else:
                    check_obj.money_bet_4 = market2_last_bet.price_4 * bet_val
                    check_obj.bet_4 = bet_val
                    db.session.commit()

            # -----------------Market_3------------------
            if i['id']==31:
                bet_val = i['bet']
                check_obj = Market_3.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3(
                                rid=resp.id,
                                money_bet_1 = market3_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market3_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==32:
                bet_val = i['bet']
                check_obj = Market_3.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3(
                                rid=resp.id,
                                money_bet_2 = market3_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()     
                else:
                    check_obj.money_bet_2 = market3_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()

            if i['id']==33:
                bet_val = i['bet']
                check_obj = Market_3.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3(
                                rid=resp.id,
                                money_bet_3 = market3_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()     
                else:
                    check_obj.money_bet_3 = market3_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    db.session.commit()

            if i['id']==34:
                bet_val = i['bet']
                check_obj = Market_3.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3(
                                rid=resp.id,
                                money_bet_4 = market3_last_bet.price_4 * bet_val,
                                bet_4 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()     
                else:
                    check_obj.money_bet_4 = market3_last_bet.price_4 * bet_val
                    check_obj.bet_4 = bet_val
                    db.session.commit()
                    
            # -----------------Market_4-------------------
            if i['id']==41:
                bet_val = i['bet']
                check_obj = Market_4.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_4(
                                rid=resp.id,
                                money_bet_1 = market4_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market4_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==42:
                bet_val = i['bet']
                check_obj = Market_4.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_4(
                                rid=resp.id,
                                money_bet_2 = market4_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market4_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()


            # -----------------Market_5------------------
            if i['id']==51:
                bet_val = i['bet']
                check_obj = Market_5.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_5(
                                rid=resp.id,
                                money_bet_1 = market5_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market5_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==52:
                bet_val = i['bet']
                check_obj = Market_5.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_5(
                                rid=resp.id,
                                money_bet_2 = market5_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market5_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()

            if i['id']==53:
                bet_val = i['bet']
                check_obj = Market_5.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_5(
                                rid=resp.id,
                                money_bet_3 = market5_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market5_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    db.session.commit()

            # -----------------Market_6------------------
            if i['id']==61:
                bet_val = i['bet']
                check_obj = Market_6.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_6(
                                rid=resp.id,
                                money_bet_1 = market6_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market6_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==62:
                bet_val = i['bet']
                check_obj = Market_6.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_6(
                                rid=resp.id,
                                money_bet_2 = market6_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market6_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()

            if i['id']==63:
                bet_val = i['bet']
                check_obj = Market_6.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_6(
                                rid=resp.id,
                                money_bet_3 = market6_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market6_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    db.session.commit()

            # -----------------Market_7------------------
            if i['id']==71:   
                bet_val = i['bet']
                check_obj = Market_7.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_7(
                                rid=resp.id,
                                money_bet_1 = market7_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market7_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==72:
                bet_val = i['bet']
                check_obj = Market_7.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_7(
                                rid=resp.id,
                                money_bet_2 = market7_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market7_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()

            if i['id']==73:
                bet_val = i['bet']
                check_obj = Market_7.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_7(
                                rid=resp.id,
                                money_bet_3 = market7_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market7_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    db.session.commit()

            # -----------------Market_8------------------
            if i['id']==81:
                bet_val = i['bet']
                check_obj = Market_8.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_8(
                                rid=resp.id,
                                money_bet_1 = market8_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market8_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==82:
                bet_val = i['bet']
                check_obj = Market_8.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_8(
                                rid=resp.id,
                                money_bet_2 = market8_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market8_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()

            if i['id']==83:
                bet_val = i['bet']
                check_obj = Market_8.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_8(
                                rid=resp.id,
                                money_bet_3 = market8_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market8_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    db.session.commit()

            # -----------------Market_9------------------
            if i['id']==91:
                bet_val = i['bet']
                check_obj = Market_9.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_9(
                                rid=resp.id,
                                money_bet_1 = market9_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market9_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==92:
                bet_val = i['bet']
                check_obj = Market_9.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_9(
                                rid=resp.id,
                                money_bet_2 = market9_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market9_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()

            if i['id']==93:
                bet_val = i['bet']
                check_obj = Market_9.query.filter_by(rid=resp.id).first()
                if not check_obj:
                    market_obj = Market_9(
                                rid=resp.id,
                                money_bet_3 = market9_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market9_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    db.session.commit()

            # -----------------Market_10------------------
            if i['id']==101:
                bet_val = i['bet']
                check_obj = Market_10.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_10(
                                rid=resp.id,
                                money_bet_1 = market10_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market10_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    db.session.commit()

            if i['id']==102:
                bet_val = i['bet']
                check_obj = Market_10.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_10(
                                rid=resp.id,
                                money_bet_2 = market10_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market10_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    db.session.commit()

            if i['id']==103:
                bet_val = i['bet']
                check_obj = Market_10.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_10(
                                rid=resp.id,
                                money_bet_3 = market10_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market10_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    db.session.commit()  

                    
    # make all unselected options as 0 in db.
    market1_rid_obj = Market_1.query.filter_by(rid=resp.id).first()
    market2_rid_obj = Market_2.query.filter_by(rid=resp.id).first()
    market3_rid_obj = Market_3.query.filter_by(rid=resp.id).first()
    market4_rid_obj = Market_4.query.filter_by(rid=resp.id).first()
    market5_rid_obj = Market_5.query.filter_by(rid=resp.id).first()
    market6_rid_obj = Market_6.query.filter_by(rid=resp.id).first()
    market7_rid_obj = Market_7.query.filter_by(rid=resp.id).first()
    market8_rid_obj = Market_8.query.filter_by(rid=resp.id).first()
    market9_rid_obj = Market_9.query.filter_by(rid=resp.id).first()
    market10_rid_obj = Market_10.query.filter_by(rid=resp.id).first()

    # Market_1
    if not market1_rid_obj:
        rid_market1 = Market_1(
                rid=resp.id,
                price_1=0,
                price_2=0,
                price_3=0,
                price_4=0,
                money_bet_1=0,
                money_bet_2=0,
                money_bet_3=0,
                money_bet_4=0,
                bet_1=0,
                bet_2=0,
                bet_3=0,
                bet_4=0,
        )
        db.session.add(rid_market1)  

    if market1_rid_obj:
        if not market1_rid_obj.bet_1:
            market1_rid_obj.bet_1 = 0
            market1_rid_obj.money_bet_1 = 0
            market1_rid_obj.price_1 = 0

        if not market1_rid_obj.bet_2:
            market1_rid_obj.bet_2 = 0
            market1_rid_obj.money_bet_2 = 0
            market1_rid_obj.price_2 = 0
        
        if not market1_rid_obj.bet_3:
            market1_rid_obj.bet_3 = 0
            market1_rid_obj.money_bet_3 = 0
            market1_rid_obj.price_3 = 0

        if not market1_rid_obj.bet_4:
            market1_rid_obj.bet_4 = 0
            market1_rid_obj.money_bet_4 = 0
            market1_rid_obj.price_4 = 0

    # Market_2
    if not market2_rid_obj:
        rid_market2 = Market_2(
                rid=resp.id,
                price_1=0,
                price_2=0,
                price_3=0,
                price_4=0,
                money_bet_1=0,
                money_bet_2=0,
                money_bet_3=0,
                money_bet_4=0,
                bet_1=0,
                bet_2=0,
                bet_3=0,
                bet_4=0,
        )
        db.session.add(rid_market2)

    if market2_rid_obj:
        if not market2_rid_obj.bet_1:
            market2_rid_obj.bet_1 = 0
            market2_rid_obj.money_bet_1 = 0
            market2_rid_obj.price_1 = 0

        if not market2_rid_obj.bet_2:
            market2_rid_obj.bet_2 = 0
            market2_rid_obj.money_bet_2 = 0
            market2_rid_obj.price_2 = 0
        
        if not market2_rid_obj.bet_3:
            market2_rid_obj.bet_3 = 0
            market2_rid_obj.money_bet_3 = 0
            market2_rid_obj.price_3 = 0

        if not market2_rid_obj.bet_4:
            market2_rid_obj.bet_4 = 0
            market2_rid_obj.money_bet_4 = 0
            market2_rid_obj.price_4 = 0
    
    # Market_3
    if not market3_rid_obj:
        rid_market3 = Market_3(
                rid=resp.id,
                price_1=0,
                price_2=0,
                price_3=0,
                price_4=0,
                money_bet_1=0,
                money_bet_2=0,
                money_bet_3=0,
                money_bet_4=0,
                bet_1=0,
                bet_2=0,
                bet_3=0,
                bet_4=0,
        )
        db.session.add(rid_market3)

    if market3_rid_obj:
        if not market3_rid_obj.bet_1:
            market3_rid_obj.bet_1 = 0
            market3_rid_obj.money_bet_1 = 0
            market3_rid_obj.price_1 = 0

        if not market3_rid_obj.bet_2:
            market3_rid_obj.bet_2 = 0
            market3_rid_obj.money_bet_2 = 0
            market3_rid_obj.price_2 = 0

        if not market3_rid_obj.bet_3:
            market3_rid_obj.bet_3 = 0
            market3_rid_obj.money_bet_3 = 0
            market3_rid_obj.price_3 = 0

        if not market3_rid_obj.bet_4:
            market3_rid_obj.bet_4 = 0
            market3_rid_obj.money_bet_4 = 0
            market3_rid_obj.price_4 = 0
            
    # Market_4
    if not market4_rid_obj:
        rid_market4 = Market_4(
                rid=resp.id,
                price_1=0,
                price_2=0,
                money_bet_1=0,
                money_bet_2=0,
                bet_1=0,
                bet_2=0,
        )
        db.session.add(rid_market4)

    if market4_rid_obj:
        if not market4_rid_obj.bet_1:
            market4_rid_obj.bet_1 = 0
            market4_rid_obj.money_bet_1 = 0
            market4_rid_obj.price_1 = 0

        if not market4_rid_obj.bet_2:
            market4_rid_obj.bet_2 = 0
            market4_rid_obj.money_bet_2 = 0
            market4_rid_obj.price_2 = 0

    # Market_5
    if not market5_rid_obj:
        rid_market5 = Market_5(
                rid=resp.id,
                price_1=0,
                price_2=0,
                price_3=0,
                money_bet_1=0,
                money_bet_2=0,
                money_bet_3=0,
                bet_1=0,
                bet_2=0,
                bet_3=0,
        )
        db.session.add(rid_market5)

    if market5_rid_obj:
        if not market5_rid_obj.bet_1:
            market5_rid_obj.bet_1 = 0
            market5_rid_obj.money_bet_1 = 0
            market5_rid_obj.price_1 = 0

        if not market5_rid_obj.bet_2:
            market5_rid_obj.bet_2 = 0
            market5_rid_obj.money_bet_2 = 0
            market5_rid_obj.price_2 = 0
        
        if not market5_rid_obj.bet_3:
            market5_rid_obj.bet_3 = 0
            market5_rid_obj.money_bet_3 = 0
            market5_rid_obj.price_3 = 0

    # Market_6
    if not market6_rid_obj:
        rid_market6 = Market_6(
                rid=resp.id,
                price_1=0,
                price_2=0,
                price_3=0,
                money_bet_1=0,
                money_bet_2=0,
                money_bet_3=0,
                bet_1=0,
                bet_2=0,
                bet_3=0,
        )
        db.session.add(rid_market6)

    if market6_rid_obj:
        if not market6_rid_obj.bet_1:
            market6_rid_obj.bet_1 = 0
            market6_rid_obj.money_bet_1 = 0
            market6_rid_obj.price_1 = 0

        if not market6_rid_obj.bet_2:
            market6_rid_obj.bet_2 = 0
            market6_rid_obj.money_bet_2 = 0
            market6_rid_obj.price_2 = 0
        
        if not market6_rid_obj.bet_3:
            market6_rid_obj.bet_3 = 0
            market6_rid_obj.money_bet_3 = 0
            market6_rid_obj.price_3 = 0

    # Market_7
    if not market7_rid_obj:
        rid_market7 = Market_7(
                rid=resp.id,
                price_1=0,
                price_2=0,
                price_3=0,
                money_bet_1=0,
                money_bet_2=0,
                money_bet_3=0,
                bet_1=0,
                bet_2=0,
                bet_3=0,
        )
        db.session.add(rid_market7)

    if market7_rid_obj:
        if not market7_rid_obj.bet_1:
            market7_rid_obj.bet_1 = 0
            market7_rid_obj.money_bet_1 = 0
            market7_rid_obj.price_1 = 0

        if not market7_rid_obj.bet_2:
            market7_rid_obj.bet_2 = 0
            market7_rid_obj.money_bet_2 = 0
            market7_rid_obj.price_2 = 0
        
        if not market7_rid_obj.bet_3:
            market7_rid_obj.bet_3 = 0
            market7_rid_obj.money_bet_3 = 0
            market7_rid_obj.price_3 = 0

    # Market_8
    if not market8_rid_obj:
        rid_market8 = Market_8(
                rid=resp.id,
                price_1=0,
                price_2=0,
                price_3=0,
                money_bet_1=0,
                money_bet_2=0,
                money_bet_3=0,
                bet_1=0,
                bet_2=0,
                bet_3=0,
        )
        db.session.add(rid_market8)

    if market8_rid_obj:
        if not market8_rid_obj.bet_1:
            market8_rid_obj.bet_1 = 0
            market8_rid_obj.money_bet_1 = 0
            market8_rid_obj.price_1 = 0

        if not market8_rid_obj.bet_2:
            market8_rid_obj.bet_2 = 0
            market8_rid_obj.money_bet_2 = 0
            market8_rid_obj.price_2 = 0
        
        if not market8_rid_obj.bet_3:
            market8_rid_obj.bet_3 = 0
            market8_rid_obj.money_bet_3 = 0
            market8_rid_obj.price_3 = 0

    # Market_9
    if not market9_rid_obj:
        rid_market9 = Market_9(
                rid=resp.id,
                price_1=0,
                price_2=0,
                price_3=0,
                money_bet_1=0,
                money_bet_2=0,
                money_bet_3=0,
                bet_1=0,
                bet_2=0,
                bet_3=0,
        )
        db.session.add(rid_market9)

    if market9_rid_obj:
        if not market9_rid_obj.bet_1:
            market9_rid_obj.bet_1 = 0
            market9_rid_obj.money_bet_1 = 0
            market9_rid_obj.price_1 = 0

        if not market9_rid_obj.bet_2:
            market9_rid_obj.bet_2 = 0
            market9_rid_obj.money_bet_2 = 0
            market9_rid_obj.price_2 = 0
        
        if not market9_rid_obj.bet_3:
            market9_rid_obj.bet_3 = 0
            market9_rid_obj.money_bet_3 = 0
            market9_rid_obj.price_3 = 0

    # Market_10
    if not market10_rid_obj:
        rid_market10 = Market_10(
                rid=resp.id,
                price_1=0,
                price_2=0,
                price_3=0,
                money_bet_1=0,
                money_bet_2=0,
                money_bet_3=0,
                bet_1=0,
                bet_2=0,
                bet_3=0,
        )
        db.session.add(rid_market10)

    if market10_rid_obj:
        if not market10_rid_obj.bet_1:
            market10_rid_obj.bet_1 = 0
            market10_rid_obj.money_bet_1 = 0
            market10_rid_obj.price_1 = 0

        if not market10_rid_obj.bet_2:
            market10_rid_obj.bet_2 = 0
            market10_rid_obj.money_bet_2 = 0
            market10_rid_obj.price_2 = 0
        
        if not market10_rid_obj.bet_3:
            market10_rid_obj.bet_3 = 0
            market10_rid_obj.money_bet_3 = 0
            market10_rid_obj.price_3 = 0
    
    db.session.commit()
    body = []
    body.append({'rid':resp.rid, 'time_ended':resp.time_submitted, 'selected_options':fe_respo})
    return {'body': body}


#----------prices API-------------------

@app.route('/api/prices')
@cross_origin()
def prices():

    #this is for get id of user who start survey
    resp= RID.query.filter_by(rid=Rid).first()
    if not resp:
        return {'msg':'no user started survey'}

    #this is for apply the latest price
    user_bet = Market_1.query.order_by(Market_1.id.desc()).first()


    #---prices calculation after submit-------

#----------------------all money bet sums for market_1--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_1.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_1.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_1.money_bet_3)).scalar()
    sum_money_bet_4 = db.session.query(func.sum(Market_1.money_bet_4)).scalar()
    
    sum_Market1 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market1
    price2 = sum_money_bet_2/sum_Market1
    price3 = sum_money_bet_3/sum_Market1
    price4 = sum_money_bet_4/sum_Market1

    user_bet = Market_1.query.order_by(Market_1.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3
    user_bet.price_4 = price4

#----------------------all money bet sums for market_2--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_2.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_2.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_2.money_bet_3)).scalar()
    sum_money_bet_4 = db.session.query(func.sum(Market_2.money_bet_4)).scalar()
    
    sum_Market2 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market2
    price2 = sum_money_bet_2/sum_Market2
    price3 = sum_money_bet_3/sum_Market2
    price4 = sum_money_bet_4/sum_Market2

    user_bet = Market_2.query.order_by(Market_2.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3
    user_bet.price_4 = price4

#----------------------all money bet sums for market_3--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_3.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_3.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_3.money_bet_3)).scalar()
    sum_money_bet_4 = db.session.query(func.sum(Market_3.money_bet_4)).scalar()
    
    sum_Market3 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market3
    price2 = sum_money_bet_2/sum_Market3
    price3 = sum_money_bet_3/sum_Market3
    price4 = sum_money_bet_4/sum_Market3
    
    user_bet = Market_3.query.order_by(Market_3.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3
    user_bet.price_4 = price4

#----------------------all money bet sums for market_4--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_4.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_4.money_bet_2)).scalar()
    
    sum_Market4 = sum_money_bet_1 + sum_money_bet_2

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market4
    price2 = sum_money_bet_2/sum_Market4

    user_bet = Market_4.query.order_by(Market_4.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2

#----------------------all money bet sums for market_5--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_5.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_5.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_5.money_bet_3)).scalar()
    
    sum_Market5 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market5
    price2 = sum_money_bet_2/sum_Market5
    price3 = sum_money_bet_3/sum_Market5

    user_bet = Market_5.query.order_by(Market_5.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

#----------------------all money bet sums for market_6--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_6.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_6.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_6.money_bet_3)).scalar()
    
    sum_Market6 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market6
    price2 = sum_money_bet_2/sum_Market6
    price3 = sum_money_bet_3/sum_Market6

    user_bet = Market_6.query.order_by(Market_6.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

#----------------------all money bet sums for market_7--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_7.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_7.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_7.money_bet_3)).scalar()
    
    sum_Market7 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market7
    price2 = sum_money_bet_2/sum_Market7
    price3 = sum_money_bet_3/sum_Market7

    user_bet = Market_7.query.order_by(Market_7.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

#----------------------all money bet sums for market_8--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_8.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_8.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_8.money_bet_3)).scalar()
    
    sum_Market8 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market8
    price2 = sum_money_bet_2/sum_Market8
    price3 = sum_money_bet_3/sum_Market8

    user_bet = Market_8.query.order_by(Market_8.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

#----------------------all money bet sums for market_9--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_9.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_9.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_9.money_bet_3)).scalar()
    
    sum_Market9 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market9
    price2 = sum_money_bet_2/sum_Market9
    price3 = sum_money_bet_3/sum_Market9

    user_bet = Market_9.query.order_by(Market_9.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

#----------------------all money bet sums for market_10--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_10.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_10.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_10.money_bet_3)).scalar()
    
    sum_Market10 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    # this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market10
    price2 = sum_money_bet_2/sum_Market10
    price3 = sum_money_bet_3/sum_Market10

    user_bet = Market_10.query.order_by(Market_10.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3
    
    db.session.commit()
    
    # for get the all objects of all market
    m1 = Market_1.query.all()
    m2 = Market_2.query.all()
    m3 = Market_3.query.all()
    m4 = Market_4.query.all()
    m5 = Market_5.query.all()
    m6 = Market_6.query.all()
    m7 = Market_7.query.all()
    m8 = Market_8.query.all()
    m9 = Market_9.query.all()
    m10 = Market_10.query.all()
    market1 = []
    market2 = []
    market3 = []
    market4 = []
    market5 = []
    market6 = []
    market7 = []
    market8 = []
    market9 = []
    market10 = []

    for i in m1:
        market1.append({
            'id':1,
            'rid': i.rid,
            'option1':{'id':11, 'money_bet_1':i.money_bet_1, 'price_1':i.price_1, 'bet_1':i.bet_1,},
            'option2':{'id':12, 'money_bet_2':i.money_bet_2, 'price_2':i.price_2, 'bet_2':i.bet_2,},
            'option3':{'id':13, 'money_bet_3':i.money_bet_3, 'price_3':i.price_3, 'bet_3':i.bet_3,},
            'option4':{'id':14, 'money_bet_4':i.money_bet_4, 'price_4':i.price_4, 'bet_4':i.bet_4,},
        })
    
    for j in m2:
        market2.append({
            'id':2,
            'rid': j.rid,
            'option1':{'id':21, 'money_bet_1':j.money_bet_1, 'price_1':j.price_1, 'bet_1':j.bet_1,},
            'option2':{'id':22, 'money_bet_2':j.money_bet_2, 'price_2':j.price_2, 'bet_2':j.bet_2,},
            'option3':{'id':23, 'money_bet_3':j.money_bet_3, 'price_3':j.price_3, 'bet_3':j.bet_3,},
            'option4':{'id':24, 'money_bet_4':j.money_bet_4, 'price_4':j.price_4, 'bet_4':j.bet_4,},
        })

    for k in m3:
        market3.append({
            'id':3,
            'rid': k.rid,
            'option1':{'id':31, 'money_bet_1':k.money_bet_1, 'price_1':k.price_1, 'bet_1':k.bet_1,},
            'option2':{'id':32, 'money_bet_2':k.money_bet_2, 'price_2':k.price_2, 'bet_2':k.bet_2,},
            'option3':{'id':33, 'money_bet_3':k.money_bet_3, 'price_3':k.price_3, 'bet_3':k.bet_3,},
            'option4':{'id':34, 'money_bet_4':k.money_bet_4, 'price_4':k.price_4, 'bet_4':k.bet_4,},
        })
        
    for l in m4:
        market4.append({
            'id':4,
            'rid': l.rid,
            'option1':{'id':41, 'money_bet_1':l.money_bet_1, 'price_1':l.price_1, 'bet_1':l.bet_1,},
            'option2':{'id':42, 'money_bet_2':l.money_bet_2, 'price_2':l.price_2, 'bet_2':l.bet_2,},
        })

    for m in m5:
        market5.append({
            'id':5,
            'rid': m.rid,
            'option1':{'id':51, 'money_bet_1':m.money_bet_1, 'price_1':m.price_1, 'bet_1':m.bet_1,},
            'option2':{'id':52, 'money_bet_2':m.money_bet_2, 'price_2':m.price_2, 'bet_2':m.bet_2,},
            'option3':{'id':53, 'money_bet_3':m.money_bet_3, 'price_3':m.price_3, 'bet_3':m.bet_3,},
        })

    for n in m6:
        market6.append({
            'id':6,
            'rid': n.rid,
            'option1':{'id':61, 'money_bet_1':n.money_bet_1, 'price_1':n.price_1, 'bet_1':n.bet_1,},
            'option2':{'id':62, 'money_bet_2':n.money_bet_2, 'price_2':n.price_2, 'bet_2':n.bet_2,},
            'option3':{'id':63, 'money_bet_3':n.money_bet_3, 'price_3':n.price_3, 'bet_3':n.bet_3,},
        })
           
    for o in m7:
        market7.append({
            'id':7,
            'rid': o.rid,
            'option1':{'id':71, 'money_bet_1':o.money_bet_1, 'price_1':o.price_1, 'bet_1':o.bet_1,},
            'option2':{'id':72, 'money_bet_2':o.money_bet_2, 'price_2':o.price_2, 'bet_2':o.bet_2,},
            'option3':{'id':73, 'money_bet_3':o.money_bet_3, 'price_3':o.price_3, 'bet_3':o.bet_3,},
        })

    for p in m8:
        market8.append({
            'id':8,
            'rid': p.rid,
            'option1':{'id':81, 'money_bet_1':p.money_bet_1, 'price_1':p.price_1, 'bet_1':p.bet_1,},
            'option2':{'id':82, 'money_bet_2':p.money_bet_2, 'price_2':p.price_2, 'bet_2':p.bet_2,},
            'option3':{'id':83, 'money_bet_3':p.money_bet_3, 'price_3':p.price_3, 'bet_3':p.bet_3,},
        })

    for q in m9:
        market9.append({
            'id':9,
            'rid': q.rid,
            'option1':{'id':91, 'money_bet_1':q.money_bet_1, 'price_1':q.price_1, 'bet_1':q.bet_1,},
            'option2':{'id':92, 'money_bet_2':q.money_bet_2, 'price_2':q.price_2, 'bet_2':q.bet_2,},
            'option3':{'id':93, 'money_bet_3':q.money_bet_3, 'price_3':q.price_3, 'bet_3':q.bet_3,},
        })

    for r in m10:
        market10.append({
            'id':10,
            'rid': r.rid,
            'option1':{'id':101, 'money_bet_1':r.money_bet_1, 'price_1':r.price_1, 'bet_1':r.bet_1,},
            'option2':{'id':102, 'money_bet_2':r.money_bet_2, 'price_2':r.price_2, 'bet_2':r.bet_2,},
            'option3':{'id':103, 'money_bet_3':r.money_bet_3, 'price_3':r.price_3, 'bet_3':r.bet_3,},
        })
    
    return {
        'market1': market1, 
        'market2': market2, 
        'market3': market3,
        'market4': market4,
        'market5': market5,
        'market6': market6,
        'market7': market7,
        'market8': market8,
        'market9': market9,
        'market10': market10
    }


# ---------------------this API is only for testing purpose-----------------------------

#example response
# {
#     "market1":{
#             "id":1,
#             "options":[
#                 {"id":11,"bet":2},
#                 {"id":12,"bet":2},
#                 {"id":13,"bet":3}
#             ]
#     },

#     "market2":{
#             "id":2,
#             "options":[
#                 {"id":31,"bet":2},
#                 {"id":32,"bet":2}
#             ]
#     }
# }

#-----------run flask app------------------------

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
