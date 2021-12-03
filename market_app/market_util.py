from .models import *
from .constant import *

def store_FE_response_data(data,resp):

    fe_respo = dict(data)

    """ this for loop iterate over response and classify it with market obj """

    for key,value in fe_respo.items():

        option_list = fe_respo[key]['options']

        for i in option_list:

            """Market_1"""
            if i['id']==11:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_1_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,
                                price_1 = price,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit() 
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price
                    db.session.commit()

            if i['id']==12:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_1_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price
                    db.session.commit()

            if i['id']==13:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_1_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1_Bets(
                                rid=resp.id,
                                money_bet_3 = price * bet_val,
                                bet_3 = bet_val,
                                price_3 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                 
                else:
                    check_obj.money_bet_3 = price * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = price
                    db.session.commit()

            if i['id']==14:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_1_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1_Bets(
                                rid=resp.id,
                                money_bet_4 = price * bet_val,
                                bet_4 = bet_val,
                                price_4 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                    
                else:
                    check_obj.money_bet_4 = price * bet_val
                    check_obj.bet_4 = bet_val
                    check_obj.price_4 = price
                    db.session.commit()

            """Market_2"""
            if i['id']==21:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_2_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,
                                price_1 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                    
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price  
                    db.session.commit()

            if i['id']==22:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_2_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price  
                    db.session.commit()

            if i['id']==23:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_2_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2_Bets(
                                rid=resp.id,
                                money_bet_3 = price * bet_val,
                                bet_3 = bet_val,
                                price_3 = price    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                  
                else:
                    check_obj.money_bet_3 = price * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = price  
                    db.session.commit()

            if i['id']==24:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_2_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2_Bets(
                                rid=resp.id,
                                money_bet_4 = price * bet_val,
                                bet_4 = bet_val,
                                price_4 = price    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                  
                else:
                    check_obj.money_bet_4 = price * bet_val
                    check_obj.bet_4 = bet_val
                    check_obj.price_4 = price  
                    db.session.commit()

            """Market_3"""
            if i['id']==31:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_3_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,
                                price_1 = price    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price
                    db.session.commit()

            if i['id']==32:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_3_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()     
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price
                    db.session.commit()

            if i['id']==33:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_3_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3_Bets(
                                rid=resp.id,
                                money_bet_3 = price * bet_val,
                                bet_3 = bet_val,
                                price_3 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()     
                else:
                    check_obj.money_bet_3 = price * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = price
                    db.session.commit()

            if i['id']==34:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_3_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3_Bets(
                                rid=resp.id,
                                money_bet_4 = price * bet_val,
                                bet_4 = bet_val,
                                price_4 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()     
                else:
                    check_obj.money_bet_4 = price * bet_val
                    check_obj.bet_4 = bet_val
                    check_obj.price_4 = price
                    db.session.commit()
                    
            """Market_4"""
            if i['id']==41:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_4_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_4_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,
                                price_1 = price    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price
                    db.session.commit()

            if i['id']==42:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_4_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_4_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price
                    db.session.commit()


            """Market_5"""
            if i['id']==51:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_5_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_5_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,
                                price_1 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price
                    db.session.commit()

            if i['id']==52:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_5_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_5_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price
                    db.session.commit()

            if i['id']==53:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_5_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_5_Bets(
                                rid=resp.id,
                                money_bet_3 = price * bet_val,
                                bet_3 = bet_val,
                                price_3 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = price * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = price
                    db.session.commit()

            """Market_6"""
            if i['id']==61:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_6_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_6_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,
                                price_1 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price  
                    db.session.commit()

            if i['id']==62:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_6_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_6_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price  
                    db.session.commit()

            if i['id']==63:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_6_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_6_Bets(
                                rid=resp.id,
                                money_bet_3 = price * bet_val,
                                bet_3 = bet_val,
                                price_3 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = price * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = price  
                    db.session.commit()

            """Market_7"""
            if i['id']==71:   
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_7_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_7_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,
                                price_1 = price    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price
                    db.session.commit()

            if i['id']==72:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_7_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_7_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price  
                    db.session.commit()

            if i['id']==73:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_7_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_7_Bets(
                                rid=resp.id,
                                money_bet_3 = price * bet_val,
                                bet_3 = bet_val,
                                price_3 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = price * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = price  
                    db.session.commit()

            """Market_8"""
            if i['id']==81:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_8_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_8_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,
                                price_1 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price  
                    db.session.commit()

            if i['id']==82:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_8_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_8_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price
                    db.session.commit()

            if i['id']==83:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_8_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_8_Bets(
                                rid=resp.id,
                                money_bet_3 = price * bet_val,
                                bet_3 = bet_val,
                                price_3 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = price * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = price  
                    db.session.commit()

            """Market_9"""
            if i['id']==91:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_9_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_9_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,  
                                price_1 = price
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price
                    db.session.commit()

            if i['id']==92:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_9_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_9_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price  
                    db.session.commit()

            if i['id']==93:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_9_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj:
                    market_obj = Market_9_Bets(
                                rid=resp.id,
                                money_bet_3 = price * bet_val,
                                bet_3 = bet_val,  
                                price_3 = price
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = price * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = price

                    db.session.commit()

            """Market_10"""
            if i['id']==101:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_10_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_10_Bets(
                                rid=resp.id,
                                money_bet_1 = price * bet_val,
                                bet_1 = bet_val,  
                                price_1 = price 
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = price * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = price 
                    db.session.commit()

            if i['id']==102:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_10_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_10_Bets(
                                rid=resp.id,
                                money_bet_2 = price * bet_val,
                                bet_2 = bet_val,
                                price_2 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = price * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = price
                    db.session.commit()

            if i['id']==103:
                bet_val = i['bet']
                price = i['price']
                check_obj = Market_10_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_10_Bets(
                                rid=resp.id,
                                money_bet_3 = price * bet_val,
                                bet_3 = bet_val,
                                price_3 = price  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = price * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = price
                    db.session.commit()

    body = []
    body.append({'rid':resp.rid, 'time_ended':resp.time_submitted, 'selected_options':fe_respo})
    return {'body': body, 'message': SUCCESS_MESSAGE['survey_ended']}
