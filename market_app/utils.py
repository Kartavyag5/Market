from .models import *
from .constant import *
from sqlalchemy import func

def initial_values_for_markets(db):
    market1_check = Market_1_Bets.query.all()
    
    if not market1_check:
        market1 = Market_1_Bets(
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

        market2 = Market_2_Bets(
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

        market3 = Market_3_Bets(
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
        
        market4 = Market_4_Bets(
                    price_1=0.5,
                    price_2=0.5,
                    money_bet_1=10,
                    money_bet_2=10,
                    bet_1=0,
                    bet_2=0,
        )

        market5 = Market_5_Bets(
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

        market6 = Market_6_Bets(
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

        market7 = Market_7_Bets(
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

        market8 = Market_8_Bets(
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

        market9 = Market_9_Bets(
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

        market10 = Market_10_Bets(
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

        """prices table initial values"""

        market1_price = Market_1_Prices(
                    price_1=0.25,
                    price_2=0.25,
                    price_3=0.25,
                    price_4=0.25,
        )

        market2_price = Market_2_Prices(
                    price_1=0.25,
                    price_2=0.25,
                    price_3=0.25,
                    price_4=0.25,
        )

        market3_price = Market_3_Prices(
                    price_1=0.25,
                    price_2=0.25,
                    price_3=0.25,
                    price_4=0.25,
        )

        market4_price = Market_4_Prices(
                    price_1=0.5,
                    price_2=0.5,
        )

        market5_price = Market_5_Prices(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
        )

        market6_price = Market_6_Prices(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
        )
        market7_price = Market_7_Prices(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
        )
        market8_price = Market_8_Prices(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
        )
        market9_price = Market_9_Prices(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
        )
        market10_price = Market_10_Prices(
                    price_1=0.33,
                    price_2=0.33,
                    price_3=0.33,
        )

        db.session.add(market1_price)
        db.session.add(market2_price)
        db.session.add(market3_price)
        db.session.add(market4_price)
        db.session.add(market5_price)
        db.session.add(market6_price)
        db.session.add(market7_price)
        db.session.add(market8_price)
        db.session.add(market9_price)
        db.session.add(market10_price)

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

def show_latest_prices(Rid,db,started_time):
    m1 = db.session.query(Market_1_Prices).order_by(Market_1_Prices.id.desc()).first()
    m2 = db.session.query(Market_2_Prices).order_by(Market_2_Prices.id.desc()).first()
    m3 = db.session.query(Market_3_Prices).order_by(Market_3_Prices.id.desc()).first()
    m4 = db.session.query(Market_4_Prices).order_by(Market_4_Prices.id.desc()).first()
    m5 = db.session.query(Market_5_Prices).order_by(Market_5_Prices.id.desc()).first()
    m6 = db.session.query(Market_6_Prices).order_by(Market_6_Prices.id.desc()).first()
    m7 = db.session.query(Market_7_Prices).order_by(Market_7_Prices.id.desc()).first()
    m8 = db.session.query(Market_8_Prices).order_by(Market_8_Prices.id.desc()).first()
    m9 = db.session.query(Market_9_Prices).order_by(Market_9_Prices.id.desc()).first()
    m10 = db.session.query(Market_10_Prices).order_by(Market_10_Prices.id.desc()).first()
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
            'time_started': started_time,
            })
            
    return {'body': body, 'message':'new rid created'}


def prices_seen_by_user(Rid,db,started_time):
    "these are latest prices in all markets"

    user_seen_prices = show_latest_prices(Rid,db,started_time)

    prices_list = {
                    'm1_price1': user_seen_prices['body'][0]['market1'][0]['option1']['price_1'],
                    'm1_price2': user_seen_prices['body'][0]['market1'][0]['option2']['price_2'],
                    'm1_price3': user_seen_prices['body'][0]['market1'][0]['option3']['price_3'],
                    'm1_price4': user_seen_prices['body'][0]['market1'][0]['option4']['price_4'],

                    'm2_price1': user_seen_prices['body'][0]['market2'][0]['option1']['price_1'],
                    'm2_price2': user_seen_prices['body'][0]['market2'][0]['option2']['price_2'],
                    'm2_price3': user_seen_prices['body'][0]['market2'][0]['option3']['price_3'],
                    'm2_price4': user_seen_prices['body'][0]['market2'][0]['option4']['price_4'],
                    
                    'm3_price1': user_seen_prices['body'][0]['market3'][0]['option1']['price_1'],
                    'm3_price2': user_seen_prices['body'][0]['market3'][0]['option2']['price_2'],
                    'm3_price3': user_seen_prices['body'][0]['market3'][0]['option3']['price_3'],
                    'm3_price4': user_seen_prices['body'][0]['market3'][0]['option4']['price_4'],
                    
                    'm4_price1': user_seen_prices['body'][0]['market4'][0]['option1']['price_1'],
                    'm4_price2': user_seen_prices['body'][0]['market4'][0]['option2']['price_2'],
                    
                    'm5_price1': user_seen_prices['body'][0]['market5'][0]['option1']['price_1'],
                    'm5_price2': user_seen_prices['body'][0]['market5'][0]['option2']['price_2'],
                    'm5_price3': user_seen_prices['body'][0]['market5'][0]['option3']['price_3'],
                    
                    'm6_price1': user_seen_prices['body'][0]['market6'][0]['option1']['price_1'],
                    'm6_price2': user_seen_prices['body'][0]['market6'][0]['option2']['price_2'],
                    'm6_price3': user_seen_prices['body'][0]['market6'][0]['option3']['price_3'],
                    
                    'm7_price1': user_seen_prices['body'][0]['market7'][0]['option1']['price_1'],
                    'm7_price2': user_seen_prices['body'][0]['market7'][0]['option2']['price_2'],
                    'm7_price3': user_seen_prices['body'][0]['market7'][0]['option3']['price_3'],
                    
                    'm8_price1': user_seen_prices['body'][0]['market8'][0]['option1']['price_1'],
                    'm8_price2': user_seen_prices['body'][0]['market8'][0]['option2']['price_2'],
                    'm8_price3': user_seen_prices['body'][0]['market8'][0]['option3']['price_3'],
                    
                    'm9_price1': user_seen_prices['body'][0]['market9'][0]['option1']['price_1'],
                    'm9_price2': user_seen_prices['body'][0]['market9'][0]['option2']['price_2'],
                    'm9_price3': user_seen_prices['body'][0]['market9'][0]['option3']['price_3'],
                    
                    'm10_price1': user_seen_prices['body'][0]['market10'][0]['option1']['price_1'],
                    'm10_price2': user_seen_prices['body'][0]['market10'][0]['option2']['price_2'],
                    'm10_price3': user_seen_prices['body'][0]['market10'][0]['option3']['price_3'],
    }

    return prices_list



def update_all_market_prices(Rid):
    """this is for get id of user who start survey"""
    resp= RID.query.filter_by(rid=Rid).first()
    if not resp:
        return {'message':ERROR_MESSAGE['start_survey']}

    """prices calculation after submit"""

    market1_rid_obj = Market_1_Bets.query.filter_by(rid_user=Rid).first()
    market2_rid_obj = Market_2_Bets.query.filter_by(rid_user=Rid).first()
    market3_rid_obj = Market_3_Bets.query.filter_by(rid_user=Rid).first()
    market4_rid_obj = Market_4_Bets.query.filter_by(rid_user=Rid).first()
    market5_rid_obj = Market_5_Bets.query.filter_by(rid_user=Rid).first()
    market6_rid_obj = Market_6_Bets.query.filter_by(rid_user=Rid).first()
    market7_rid_obj = Market_7_Bets.query.filter_by(rid_user=Rid).first()
    market8_rid_obj = Market_8_Bets.query.filter_by(rid_user=Rid).first()
    market9_rid_obj = Market_9_Bets.query.filter_by(rid_user=Rid).first()
    market10_rid_obj = Market_10_Bets.query.filter_by(rid_user=Rid).first()

    if market1_rid_obj:

        """all money bet sums for market_1"""
        sum_money_bet_1 = db.session.query(func.sum(Market_1_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_1_Bets.money_bet_2)).scalar()
        sum_money_bet_3 = db.session.query(func.sum(Market_1_Bets.money_bet_3)).scalar()
        sum_money_bet_4 = db.session.query(func.sum(Market_1_Bets.money_bet_4)).scalar()
        
        sum_Market1 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market1
        price2 = sum_money_bet_2/sum_Market1
        price3 = sum_money_bet_3/sum_Market1
        price4 = sum_money_bet_4/sum_Market1

        updated_prices_market_1 = Market_1_Prices(
                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
                    price_4 = price4
        )
        db.session.add(updated_prices_market_1)

    if market2_rid_obj:
        """all money bet sums for market_2"""

        sum_money_bet_1 = db.session.query(func.sum(Market_2_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_2_Bets.money_bet_2)).scalar()
        sum_money_bet_3 = db.session.query(func.sum(Market_2_Bets.money_bet_3)).scalar()
        sum_money_bet_4 = db.session.query(func.sum(Market_2_Bets.money_bet_4)).scalar()
        
        sum_Market2 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market2
        price2 = sum_money_bet_2/sum_Market2
        price3 = sum_money_bet_3/sum_Market2
        price4 = sum_money_bet_4/sum_Market2

        updated_prices_market_2 = Market_2_Prices(
                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
                    price_4 = price4
        )
        db.session.add(updated_prices_market_2)
    
    if market3_rid_obj:
        """all money bet sums for market_3"""

        sum_money_bet_1 = db.session.query(func.sum(Market_3_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_3_Bets.money_bet_2)).scalar()
        sum_money_bet_3 = db.session.query(func.sum(Market_3_Bets.money_bet_3)).scalar()
        sum_money_bet_4 = db.session.query(func.sum(Market_3_Bets.money_bet_4)).scalar()
        
        sum_Market3 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3 + sum_money_bet_4

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market3
        price2 = sum_money_bet_2/sum_Market3
        price3 = sum_money_bet_3/sum_Market3
        price4 = sum_money_bet_4/sum_Market3
        
        updated_prices_market_3 = Market_3_Prices(
                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
                    price_4 = price4
        )
        db.session.add(updated_prices_market_3)
    
    
    if market4_rid_obj:
        """all money bet sums for market_4"""

        sum_money_bet_1 = db.session.query(func.sum(Market_4_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_4_Bets.money_bet_2)).scalar()
        
        sum_Market4 = sum_money_bet_1 + sum_money_bet_2

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market4
        price2 = sum_money_bet_2/sum_Market4

        updated_prices_market_4 = Market_4_Prices(
                    price_1 = price1,
                    price_2 = price2,
        )
        db.session.add(updated_prices_market_4)
    
    if market5_rid_obj:
        """all money bet sums for market_5"""

        sum_money_bet_1 = db.session.query(func.sum(Market_5_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_5_Bets.money_bet_2)).scalar()
        sum_money_bet_3 = db.session.query(func.sum(Market_5_Bets.money_bet_3)).scalar()
        
        sum_Market5 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market5
        price2 = sum_money_bet_2/sum_Market5
        price3 = sum_money_bet_3/sum_Market5

        updated_prices_market_5 = Market_5_Prices(
                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
        )
        db.session.add(updated_prices_market_5)
    
    if market6_rid_obj:
        """all money bet sums for market_6"""

        sum_money_bet_1 = db.session.query(func.sum(Market_6_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_6_Bets.money_bet_2)).scalar()
        sum_money_bet_3 = db.session.query(func.sum(Market_6_Bets.money_bet_3)).scalar()
        
        sum_Market6 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market6
        price2 = sum_money_bet_2/sum_Market6
        price3 = sum_money_bet_3/sum_Market6

        updated_prices_market_6 = Market_6_Prices(
                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
        )
        db.session.add(updated_prices_market_6)
    
    if market7_rid_obj:
        """all money bet sums for market_7"""

        sum_money_bet_1 = db.session.query(func.sum(Market_7_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_7_Bets.money_bet_2)).scalar()
        sum_money_bet_3 = db.session.query(func.sum(Market_7_Bets.money_bet_3)).scalar()
        
        sum_Market7 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market7
        price2 = sum_money_bet_2/sum_Market7
        price3 = sum_money_bet_3/sum_Market7

        updated_prices_market_7 = Market_7_Prices(
                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
        )
        db.session.add(updated_prices_market_7)
    
    
    if market8_rid_obj:
        """all money bet sums for market_8"""

        sum_money_bet_1 = db.session.query(func.sum(Market_8_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_8_Bets.money_bet_2)).scalar()
        sum_money_bet_3 = db.session.query(func.sum(Market_8_Bets.money_bet_3)).scalar()
        
        sum_Market8 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market8
        price2 = sum_money_bet_2/sum_Market8
        price3 = sum_money_bet_3/sum_Market8

        updated_prices_market_8 = Market_8_Prices(
                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
        )
    
        db.session.add(updated_prices_market_8)

    if market9_rid_obj:
        """all money bet sums for market_9"""

        sum_money_bet_1 = db.session.query(func.sum(Market_9_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_9_Bets.money_bet_2)).scalar()
        sum_money_bet_3 = db.session.query(func.sum(Market_9_Bets.money_bet_3)).scalar()
        
        sum_Market9 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market9
        price2 = sum_money_bet_2/sum_Market9
        price3 = sum_money_bet_3/sum_Market9

        updated_prices_market_9 = Market_9_Prices(
                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
        )
        db.session.add(updated_prices_market_9)
    
    if market10_rid_obj:
        """all money bet sums for market_10"""

        sum_money_bet_1 = db.session.query(func.sum(Market_10_Bets.money_bet_1)).scalar()
        sum_money_bet_2 = db.session.query(func.sum(Market_10_Bets.money_bet_2)).scalar()
        sum_money_bet_3 = db.session.query(func.sum(Market_10_Bets.money_bet_3)).scalar()
        
        sum_Market10 = sum_money_bet_1 + sum_money_bet_2 + sum_money_bet_3

        """this is the updated prices for new user"""
        price1 = sum_money_bet_1/sum_Market10
        price2 = sum_money_bet_2/sum_Market10
        price3 = sum_money_bet_3/sum_Market10

        updated_prices_market_10 = Market_10_Prices(
                    price_1 = price1,
                    price_2 = price2,
                    price_3 = price3,
        )
        db.session.add(updated_prices_market_10)

    db.session.commit()

    return {"message":SUCCESS_MESSAGE['prices_update']}


def Rid_startTime_EndTime_Added_to_Market_bets(db):
    Rid_obj = db.session.query(RID).order_by(RID.id.desc()).first()

    """get the rid obj in market tables"""
    market1_rid_obj = Market_1_Bets.query.filter_by(rid=Rid_obj.id).first()
    market2_rid_obj = Market_2_Bets.query.filter_by(rid=Rid_obj.id).first()
    market3_rid_obj = Market_3_Bets.query.filter_by(rid=Rid_obj.id).first()
    market4_rid_obj = Market_4_Bets.query.filter_by(rid=Rid_obj.id).first()
    market5_rid_obj = Market_5_Bets.query.filter_by(rid=Rid_obj.id).first()
    market6_rid_obj = Market_6_Bets.query.filter_by(rid=Rid_obj.id).first()
    market7_rid_obj = Market_7_Bets.query.filter_by(rid=Rid_obj.id).first()
    market8_rid_obj = Market_8_Bets.query.filter_by(rid=Rid_obj.id).first()
    market9_rid_obj = Market_9_Bets.query.filter_by(rid=Rid_obj.id).first()
    market10_rid_obj = Market_10_Bets.query.filter_by(rid=Rid_obj.id).first()
    
    if market1_rid_obj:
        market1_rid_obj.rid_user = Rid_obj.rid
        market1_rid_obj.start_time = Rid_obj.time_started
        market1_rid_obj.end_time = Rid_obj.time_submitted
        
    if market2_rid_obj:
        market2_rid_obj.rid_user = Rid_obj.rid
        market2_rid_obj.start_time = Rid_obj.time_started
        market2_rid_obj.end_time = Rid_obj.time_submitted
        
    if market3_rid_obj:
        market3_rid_obj.rid_user = Rid_obj.rid
        market3_rid_obj.start_time = Rid_obj.time_started
        market3_rid_obj.end_time = Rid_obj.time_submitted
        
    if market4_rid_obj:
        market4_rid_obj.rid_user = Rid_obj.rid
        market4_rid_obj.start_time = Rid_obj.time_started
        market4_rid_obj.end_time = Rid_obj.time_submitted
        
    if market5_rid_obj:
        market5_rid_obj.rid_user = Rid_obj.rid
        market5_rid_obj.start_time = Rid_obj.time_started
        market5_rid_obj.end_time = Rid_obj.time_submitted
        
    if market6_rid_obj:
        market6_rid_obj.rid_user = Rid_obj.rid
        market6_rid_obj.start_time = Rid_obj.time_started
        market6_rid_obj.end_time = Rid_obj.time_submitted
        
    if market7_rid_obj:
        market7_rid_obj.rid_user = Rid_obj.rid
        market7_rid_obj.start_time = Rid_obj.time_started
        market7_rid_obj.end_time = Rid_obj.time_submitted
        
    if market8_rid_obj:
        market8_rid_obj.rid_user = Rid_obj.rid
        market8_rid_obj.start_time = Rid_obj.time_started
        market8_rid_obj.end_time = Rid_obj.time_submitted
        
    if market9_rid_obj:
        market9_rid_obj.rid_user = Rid_obj.rid
        market9_rid_obj.start_time = Rid_obj.time_started
        market9_rid_obj.end_time = Rid_obj.time_submitted
        
    if market10_rid_obj:
        market10_rid_obj.rid_user = Rid_obj.rid
        market10_rid_obj.start_time = Rid_obj.time_started
        market10_rid_obj.end_time = Rid_obj.time_submitted

    db.session.commit()

    return {"message":SUCCESS_MESSAGE['rid_time_added']}
        

