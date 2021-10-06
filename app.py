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
@app.route('/api/do_not_call')
@cross_origin()
def main():

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

    market3 = Market_3(
                price_1=0.5,
                price_2=0.5,
                money_bet_1=10,
                money_bet_2=10,
                bet_1=0,
                bet_2=0,
    )

    db.session.add(market1)  
    db.session.add(market2)  
    db.session.add(market3)  
    db.session.commit()

    return 'Root of Market API'


#-------------Start Survey API-------------------------

@app.route('/api/start_survey', methods=['POST'])
@cross_origin()
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
            'option1':{'id':21, 'money_bet_1':0, 'price_1':m2.price_1, 'bet_1':0,},
            'option2':{'id':22, 'money_bet_2':0, 'price_2':m2.price_2, 'bet_2':0,},
            'option3':{'id':23, 'money_bet_3':0, 'price_3':m2.price_3, 'bet_3':0,},
        })
    
    
    market3.append({
            'id':3,
            'option1':{'id':31, 'money_bet_1':0, 'price_1':m3.price_1, 'bet_1':0,},
            'option2':{'id':32, 'money_bet_2':0, 'price_2':m3.price_2, 'bet_2':0,},
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
            'message':'new rid created'
            })
            
    return {'body': body}


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

    # this for loop iterate over response and classify it with market obj

    for key,value in fe_respo.items():

        option_list = fe_respo[key]['options']

        for i in option_list:

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



    # make all unselected options as 0 in db.
    market1_rid_obj = Market_1.query.filter_by(rid=resp.id).first()
    market2_rid_obj = Market_2.query.filter_by(rid=resp.id).first()
    market3_rid_obj = Market_3.query.filter_by(rid=resp.id).first()

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

    if market3_rid_obj:
        if not market3_rid_obj.bet_1:
            market3_rid_obj.bet_1 = 0
            market3_rid_obj.money_bet_1 = 0
            market3_rid_obj.price_1 = 0

        if not market3_rid_obj.bet_2:
            market3_rid_obj.bet_2 = 0
            market3_rid_obj.money_bet_2 = 0
            market3_rid_obj.price_2 = 0
    
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


 #------------------ all money bet sums for market_1------------------------------

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


 #----------------------all money bet sums for market_2--------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_2.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_2.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_2.money_bet_3)).scalar()
    
    sum_Market2 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    #this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market2
    price2 = sum_money_bet_2/sum_Market2
    price3 = sum_money_bet_3/sum_Market2

    user_bet = Market_2.query.order_by(Market_2.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3


 # -----------------all money bet sums for market_3-------------------------------

    sum_money_bet_1 = db.session.query(func.sum(Market_3.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_3.money_bet_2)).scalar()
    
    
    sum_Market3 = sum_money_bet_1 + sum_money_bet_2

    #this is the updated prices for new user
    price1 = sum_money_bet_1/sum_Market3
    price2 = sum_money_bet_2/sum_Market3
    
    user_bet = Market_3.query.order_by(Market_3.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    
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
        })

        
    for k in m3:

        market3.append({
            'id':3,
            'rid': k.rid,
            'option1':{'id':31, 'money_bet_1':k.money_bet_1, 'price_1':k.price_1, 'bet_1':k.bet_1,},
            'option2':{'id':32, 'money_bet_2':k.money_bet_2, 'price_2':k.price_2, 'bet_2':k.bet_2,},
        })

           
    return {'market1': market1, 'market2': market2, 'market3': market3}


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