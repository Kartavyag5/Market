from .models import *
from .constant import *
from sqlalchemy import func

def initial_values_for_markets(db):
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
        return {'message':'default values successfully added'}

    """show latest prices while start survey"""

def show_latest_prices(Rid,db):
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
    #resp= RID.query.filter_by(rid=Rid).first()
    body = []
    body.append({
            'rid':Rid, 
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
            
    return {'body': body, 'message':'new rid created'}


def update_all_market_prices(Rid):
    """this is for get id of user who start survey"""
    resp= RID.query.filter_by(rid=Rid).first()
    if not resp:
        return {'message':ERROR_MESSAGE['start_survey']}

    """this is for apply the latest price"""
    user_bet = Market_1.query.order_by(Market_1.id.desc()).first()


    """prices calculation after submit"""

    """all money bet sums for market_1"""
    sum_money_bet_1 = db.session.query(func.sum(Market_1.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_1.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_1.money_bet_3)).scalar()
    sum_money_bet_4 = db.session.query(func.sum(Market_1.money_bet_4)).scalar()
    
    sum_Market1 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market1
    price2 = sum_money_bet_2/sum_Market1
    price3 = sum_money_bet_3/sum_Market1
    price4 = sum_money_bet_4/sum_Market1

    user_bet = Market_1.query.order_by(Market_1.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3
    user_bet.price_4 = price4

    """all money bet sums for market_2"""

    sum_money_bet_1 = db.session.query(func.sum(Market_2.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_2.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_2.money_bet_3)).scalar()
    sum_money_bet_4 = db.session.query(func.sum(Market_2.money_bet_4)).scalar()
    
    sum_Market2 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market2
    price2 = sum_money_bet_2/sum_Market2
    price3 = sum_money_bet_3/sum_Market2
    price4 = sum_money_bet_4/sum_Market2

    user_bet = Market_2.query.order_by(Market_2.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3
    user_bet.price_4 = price4

    """all money bet sums for market_3"""

    sum_money_bet_1 = db.session.query(func.sum(Market_3.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_3.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_3.money_bet_3)).scalar()
    sum_money_bet_4 = db.session.query(func.sum(Market_3.money_bet_4)).scalar()
    
    sum_Market3 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market3
    price2 = sum_money_bet_2/sum_Market3
    price3 = sum_money_bet_3/sum_Market3
    price4 = sum_money_bet_4/sum_Market3
    
    user_bet = Market_3.query.order_by(Market_3.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3
    user_bet.price_4 = price4

    """all money bet sums for market_4"""

    sum_money_bet_1 = db.session.query(func.sum(Market_4.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_4.money_bet_2)).scalar()
    
    sum_Market4 = sum_money_bet_1 + sum_money_bet_2

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market4
    price2 = sum_money_bet_2/sum_Market4

    user_bet = Market_4.query.order_by(Market_4.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2

    """all money bet sums for market_5"""

    sum_money_bet_1 = db.session.query(func.sum(Market_5.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_5.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_5.money_bet_3)).scalar()
    
    sum_Market5 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market5
    price2 = sum_money_bet_2/sum_Market5
    price3 = sum_money_bet_3/sum_Market5

    user_bet = Market_5.query.order_by(Market_5.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

    """all money bet sums for market_6"""

    sum_money_bet_1 = db.session.query(func.sum(Market_6.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_6.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_6.money_bet_3)).scalar()
    
    sum_Market6 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market6
    price2 = sum_money_bet_2/sum_Market6
    price3 = sum_money_bet_3/sum_Market6

    user_bet = Market_6.query.order_by(Market_6.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

    """all money bet sums for market_7"""

    sum_money_bet_1 = db.session.query(func.sum(Market_7.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_7.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_7.money_bet_3)).scalar()
    
    sum_Market7 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market7
    price2 = sum_money_bet_2/sum_Market7
    price3 = sum_money_bet_3/sum_Market7

    user_bet = Market_7.query.order_by(Market_7.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

    """all money bet sums for market_8"""

    sum_money_bet_1 = db.session.query(func.sum(Market_8.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_8.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_8.money_bet_3)).scalar()
    
    sum_Market8 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market8
    price2 = sum_money_bet_2/sum_Market8
    price3 = sum_money_bet_3/sum_Market8

    user_bet = Market_8.query.order_by(Market_8.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

    """all money bet sums for market_9"""

    sum_money_bet_1 = db.session.query(func.sum(Market_9.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_9.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_9.money_bet_3)).scalar()
    
    sum_Market9 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market9
    price2 = sum_money_bet_2/sum_Market9
    price3 = sum_money_bet_3/sum_Market9

    user_bet = Market_9.query.order_by(Market_9.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3

    """all money bet sums for market_10"""

    sum_money_bet_1 = db.session.query(func.sum(Market_10.money_bet_1)).scalar()
    sum_money_bet_2 = db.session.query(func.sum(Market_10.money_bet_2)).scalar()
    sum_money_bet_3 = db.session.query(func.sum(Market_10.money_bet_3)).scalar()
    
    sum_Market10 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

    """this is the updated prices for new user"""
    price1 = sum_money_bet_1/sum_Market10
    price2 = sum_money_bet_2/sum_Market10
    price3 = sum_money_bet_3/sum_Market10

    user_bet = Market_10.query.order_by(Market_10.id.desc()).first()
    user_bet.price_1 = price1
    user_bet.price_2 = price2
    user_bet.price_3 = price3
    
    db.session.commit()

    return {"message":SUCCESS_MESSAGE['prices_update']}

