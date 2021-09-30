from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "9513b0b66a8546799bb12ddb3fb80755"


# username = "root"
# password = ""
# host = "localhost"
# database = "market"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/market"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# global variable for get value in all page
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


# Market_1 Model
class Market_1(db.Model):
    id = db.Column(db.Integer, primary_key=True)        # autoincrement=True
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id))
    
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



# Market_2 Model
class Market_2(db.Model):
    id = db.Column(db.Integer, primary_key=True)        # autoincrement=True
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id))
    
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


# Market_3 Model
class Market_3(db.Model):   
    id = db.Column(db.Integer, primary_key=True)        # autoincrement=True
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id))

    money_bet_1 = db.Column(db.Float())
    money_bet_2 = db.Column(db.Float())
    
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    
    bet_1 = db.Column(db.Integer())
    bet_2 = db.Column(db.Integer())

    def __repr__(self):
        return f"{self.rid.rid}"


# # Market_4 Model
# class Market_4(db.Model):
#     id = db.Column(db.Integer, primary_key=True)      # autoincrement=True
#     rid = db.Column(db.Integer(), db.ForeignKey(RID.id))

#     money_bet_1 = db.Column(db.Float())
#     money_bet_2 = db.Column(db.Float())
#     money_bet_3 = db.Column(db.Float())
    
#     price_1 = db.Column(db.Float())
#     price_2 = db.Column(db.Float())
#     price_3 = db.Column(db.Float())
    
#     bet_1 = db.Column(db.Integer())
#     bet_2 = db.Column(db.Integer())
#     bet_3 = db.Column(db.Integer())

#     def __repr__(self):
#         return f"{self.rid.rid}"


# # Market_5 Model
# class Market_5(db.Model):
#     id = db.Column(db.Integer, primary_key=True)      # autoincrement=True
#     rid = db.Column(db.Integer(), db.ForeignKey(RID.id))

#     money_bet_1 = db.Column(db.Float())
#     money_bet_2 = db.Column(db.Float())
#     money_bet_3 = db.Column(db.Float())
    
#     price_1 = db.Column(db.Float())
#     price_2 = db.Column(db.Float())
#     price_3 = db.Column(db.Float())
    
#     bet_1 = db.Column(db.Integer())
#     bet_2 = db.Column(db.Integer())
#     bet_3 = db.Column(db.Integer())

#     def __repr__(self):
#         return f"{self.rid.rid}"


# # Market_6 Model
# class Market_6(db.Model):
#     id = db.Column(db.Integer, primary_key=True)      # autoincrement=True
#     rid = db.Column(db.Integer(), db.ForeignKey(RID.id))

#     money_bet_1 = db.Column(db.Float())
#     money_bet_2 = db.Column(db.Float())
#     money_bet_3 = db.Column(db.Float())
    
#     price_1 = db.Column(db.Float())
#     price_2 = db.Column(db.Float())
#     price_3 = db.Column(db.Float())
    
#     bet_1 = db.Column(db.Integer())
#     bet_2 = db.Column(db.Integer())
#     bet_3 = db.Column(db.Integer())

#     def __repr__(self):
#         return f"{self.rid.rid}"


# # Market_7 Model
# class Market_7(db.Model):
#     id = db.Column(db.Integer, primary_key=True)      # autoincrement=True
#     rid = db.Column(db.Integer(), db.ForeignKey(RID.id))

#     money_bet_1 = db.Column(db.Float())
#     money_bet_2 = db.Column(db.Float())
#     money_bet_3 = db.Column(db.Float())
    
#     price_1 = db.Column(db.Float())
#     price_2 = db.Column(db.Float())
#     price_3 = db.Column(db.Float())
    
#     bet_1 = db.Column(db.Integer())
#     bet_2 = db.Column(db.Integer())
#     bet_3 = db.Column(db.Integer())

#     def __repr__(self):
#         return f"{self.rid.rid}"


# # Market_8 Model
# class Market_8(db.Model):
#     id = db.Column(db.Integer, primary_key=True)      # autoincrement=True
#     rid = db.Column(db.Integer(), db.ForeignKey(RID.id))

#     money_bet_1 = db.Column(db.Float())
#     money_bet_2 = db.Column(db.Float())
#     money_bet_3 = db.Column(db.Float())
    
#     price_1 = db.Column(db.Float())
#     price_2 = db.Column(db.Float())
#     price_3 = db.Column(db.Float())
    
#     bet_1 = db.Column(db.Integer())
#     bet_2 = db.Column(db.Integer())
#     bet_3 = db.Column(db.Integer())

#     def __repr__(self):
#         return f"{self.rid.rid}"


# # Market_9 Model
# class Market_9(db.Model):
#     id = db.Column(db.Integer, primary_key=True)      # autoincrement=True
#     rid = db.Column(db.Integer(), db.ForeignKey(RID.id))

#     money_bet_1 = db.Column(db.Float())
#     money_bet_2 = db.Column(db.Float())
#     money_bet_3 = db.Column(db.Float())
    
#     price_1 = db.Column(db.Float())
#     price_2 = db.Column(db.Float())
#     price_3 = db.Column(db.Float())
    
#     bet_1 = db.Column(db.Integer())
#     bet_2 = db.Column(db.Integer())
#     bet_3 = db.Column(db.Integer())

#     def __repr__(self):
#         return f"{self.rid.rid}"


# # Market_10 Model
# class Market_10(db.Model):
#     id = db.Column(db.Integer, primary_key=True)      # autoincrement=True 
#     rid = db.Column(db.Integer(), db.ForeignKey(RID.id))

#     money_bet_1 = db.Column(db.Float())
#     money_bet_2 = db.Column(db.Float())
#     money_bet_3 = db.Column(db.Float())
    
#     price_1 = db.Column(db.Float())
#     price_2 = db.Column(db.Float())
#     price_3 = db.Column(db.Float())
    
#     bet_1 = db.Column(db.Integer())
#     bet_2 = db.Column(db.Integer())
#     bet_3 = db.Column(db.Integer())

#     def __repr__(self):
#         return f"{self.rid.rid}"


db.create_all()

@app.route('/api')
def main():
    return 'Root of Market API'


# Default prices Of the Market
@app.route('/api/prices')
def prices():
    # this response is for the testing purpose

    # market = 1
    # option = 2
    # bet = 2

    # market = 1
    # option = 3
    # bet = 4

    Rid = 1
    # prices calculation after submit

    # update sum after every submit
    sum1 = 10 + 10 + 10 + 10 + 0.5 + 0.75

    price1 = 10/sum1
    price2 = (10+0.5)/sum1
    price3 = (10+0.75)/sum1
    price4 = 10/sum1

    market1_obj = Market_1(
                    rid = Rid,
                    money_bet_1 = 0,
                    money_bet_2 = 2*0.25,
                    money_bet_3 = 3*0.25,
                    money_bet_4 = 0,

                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
                    price_4 = price4,
                    
                    bet_1 = 0,
                    bet_2 = 2,
                    bet_3 = 3,
                    bet_4 = 0,
                    )

    db.session.add(market1_obj)  
    db.session.commit()

    if request.method == 'GET':
        m1 = Market_1.query.all()         # or you can add filter_by()
        m2 = Market_2.query.all()         # or you can add filter_by()
        m3 = Market_3.query.all()         # or you can add filter_by()
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
    
    return {
        'market1': market1, 
        'market2': market2, 
        'market3': market3
    }




# Start Survey
@app.route('/api/start_survey', methods=['POST'])
def start_survey():
    if request.method == 'POST':
        global Rid
        Rid = request.form['rid']
        time_started = datetime.now()
        
        RID_obj = RID(rid=Rid)
        db.session.add(RID_obj)  
        db.session.commit()

    resp = RID.query.filter_by(rid=Rid).first()
    body = []
    body.append({'rid': resp.rid, 'time_started': time_started})
    return {'body': body}




# End Survey
@app.route('/api/end_survey', methods=['GET'])
def end_survey():
    if request.method == 'GET':
        # Rid = request.form['rid']
        time_ended = datetime.now()

        # RID_obj = RID(rid=Rid)
        # db.session.add(RID_obj)
    resp = RID.query.filter_by(rid=Rid).first()

    if resp:
        resp.time_submitted = datetime.now()
        db.session.commit()
    else:
        return {'msg':'id not found'}

    body = []

    body.append({'rid': resp.rid, 'time_ended': resp.time_submitted})
    return {'body': body}



# run flask app
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)