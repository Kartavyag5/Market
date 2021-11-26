from .models import *
from .constant import *

def store_FE_response_data(data,resp):

    fe_respo = dict(data)
    
    """ get the last obj of markets. """
    market1_last_bet = Market_1_Prices.query.order_by(Market_1_Prices.id.desc()).first()
    market2_last_bet = Market_2_Prices.query.order_by(Market_2_Prices.id.desc()).first()
    market3_last_bet = Market_3_Prices.query.order_by(Market_3_Prices.id.desc()).first()
    market4_last_bet = Market_4_Prices.query.order_by(Market_4_Prices.id.desc()).first()
    market5_last_bet = Market_5_Prices.query.order_by(Market_5_Prices.id.desc()).first()
    market6_last_bet = Market_6_Prices.query.order_by(Market_6_Prices.id.desc()).first()
    market7_last_bet = Market_7_Prices.query.order_by(Market_7_Prices.id.desc()).first()
    market8_last_bet = Market_8_Prices.query.order_by(Market_8_Prices.id.desc()).first()
    market9_last_bet = Market_9_Prices.query.order_by(Market_9_Prices.id.desc()).first()
    market10_last_bet = Market_10_Prices.query.order_by(Market_10_Prices.id.desc()).first()

    """ this for loop iterate over response and classify it with market obj """

    for key,value in fe_respo.items():

        option_list = fe_respo[key]['options']

        for i in option_list:

            """Market_1"""
            if i['id']==11:
                bet_val = i['bet']
                check_obj = Market_1_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1_Bets(
                                rid=resp.id,
                                money_bet_1 = market1_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,
                                price_1 = market1_last_bet.price_1,  
                                )
                    db.session.add(market_obj)  
                    db.session.commit() 
                else:
                    check_obj.money_bet_1 = market1_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market1_last_bet.price_1
                    db.session.commit()

            if i['id']==12:
                bet_val = i['bet']
                check_obj = Market_1_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1_Bets(
                                rid=resp.id,
                                money_bet_2 = market1_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market1_last_bet.price_2  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_2 = market1_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market1_last_bet.price_2
                    db.session.commit()

            if i['id']==13:
                bet_val = i['bet']
                check_obj = Market_1_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1_Bets(
                                rid=resp.id,
                                money_bet_3 = market1_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,
                                price_3 = market1_last_bet.price_3  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                 
                else:
                    check_obj.money_bet_3 = market1_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = market1_last_bet.price_3
                    db.session.commit()

            if i['id']==14:
                bet_val = i['bet']
                check_obj = Market_1_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_1_Bets(
                                rid=resp.id,
                                money_bet_4 = market1_last_bet.price_4 * bet_val,
                                bet_4 = bet_val,
                                price_4 = market1_last_bet.price_4  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                    
                else:
                    check_obj.money_bet_4 = market1_last_bet.price_4 * bet_val
                    check_obj.bet_4 = bet_val
                    check_obj.price_4 = market1_last_bet.price_4
                    db.session.commit()

            """Market_2"""
            if i['id']==21:
                bet_val = i['bet']
                check_obj = Market_2_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2_Bets(
                                rid=resp.id,
                                money_bet_1 = market2_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,
                                price_1 = market2_last_bet.price_1  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                    
                else:
                    check_obj.money_bet_1 = market2_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market2_last_bet.price_1  
                    db.session.commit()

            if i['id']==22:
                bet_val = i['bet']
                check_obj = Market_2_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2_Bets(
                                rid=resp.id,
                                money_bet_2 = market2_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market2_last_bet.price_2    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_2 = market2_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market2_last_bet.price_2  
                    db.session.commit()

            if i['id']==23:
                bet_val = i['bet']
                check_obj = Market_2_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2_Bets(
                                rid=resp.id,
                                money_bet_3 = market2_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,
                                price_3 = market2_last_bet.price_3    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                  
                else:
                    check_obj.money_bet_3 = market2_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = market2_last_bet.price_3  
                    db.session.commit()

            if i['id']==24:
                bet_val = i['bet']
                check_obj = Market_2_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_2_Bets(
                                rid=resp.id,
                                money_bet_4 = market2_last_bet.price_4 * bet_val,
                                bet_4 = bet_val,
                                price_4 = market2_last_bet.price_4    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()                  
                else:
                    check_obj.money_bet_4 = market2_last_bet.price_4 * bet_val
                    check_obj.bet_4 = bet_val
                    check_obj.price_4 = market2_last_bet.price_4  
                    db.session.commit()

            """Market_3"""
            if i['id']==31:
                bet_val = i['bet']
                check_obj = Market_3_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3_Bets(
                                rid=resp.id,
                                money_bet_1 = market3_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,
                                price_1 = market3_last_bet.price_1    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market3_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market3_last_bet.price_1
                    db.session.commit()

            if i['id']==32:
                bet_val = i['bet']
                check_obj = Market_3_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3_Bets(
                                rid=resp.id,
                                money_bet_2 = market3_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market3_last_bet.price_2  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()     
                else:
                    check_obj.money_bet_2 = market3_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market3_last_bet.price_2
                    db.session.commit()

            if i['id']==33:
                bet_val = i['bet']
                check_obj = Market_3_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3_Bets(
                                rid=resp.id,
                                money_bet_3 = market3_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,
                                price_3 = market3_last_bet.price_3  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()     
                else:
                    check_obj.money_bet_3 = market3_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = market3_last_bet.price_3
                    db.session.commit()

            if i['id']==34:
                bet_val = i['bet']
                check_obj = Market_3_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_3_Bets(
                                rid=resp.id,
                                money_bet_4 = market3_last_bet.price_4 * bet_val,
                                bet_4 = bet_val,
                                price_4 = market3_last_bet.price_4  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()     
                else:
                    check_obj.money_bet_4 = market3_last_bet.price_4 * bet_val
                    check_obj.bet_4 = bet_val
                    check_obj.price_4 = market3_last_bet.price_4
                    db.session.commit()
                    
            """Market_4"""
            if i['id']==41:
                bet_val = i['bet']
                check_obj = Market_4_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_4_Bets(
                                rid=resp.id,
                                money_bet_1 = market4_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,
                                price_1 = market4_last_bet.price_1    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market4_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market4_last_bet.price_1
                    db.session.commit()

            if i['id']==42:
                bet_val = i['bet']
                check_obj = Market_4_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_4_Bets(
                                rid=resp.id,
                                money_bet_2 = market4_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market4_last_bet.price_2  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market4_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market4_last_bet.price_2
                    db.session.commit()


            """Market_5"""
            if i['id']==51:
                bet_val = i['bet']
                check_obj = Market_5_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_5_Bets(
                                rid=resp.id,
                                money_bet_1 = market5_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,
                                price_1 = market5_last_bet.price_1  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market5_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market5_last_bet.price_1
                    db.session.commit()

            if i['id']==52:
                bet_val = i['bet']
                check_obj = Market_5_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_5_Bets(
                                rid=resp.id,
                                money_bet_2 = market5_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market5_last_bet.price_2  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market5_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market5_last_bet.price_2
                    db.session.commit()

            if i['id']==53:
                bet_val = i['bet']
                check_obj = Market_5_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_5_Bets(
                                rid=resp.id,
                                money_bet_3 = market5_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,
                                price_3 = market5_last_bet.price_3  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market5_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = market5_last_bet.price_3
                    db.session.commit()

            """Market_6"""
            if i['id']==61:
                bet_val = i['bet']
                check_obj = Market_6_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_6_Bets(
                                rid=resp.id,
                                money_bet_1 = market6_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,
                                price_1 = market6_last_bet.price_1  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market6_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market6_last_bet.price_1  
                    db.session.commit()

            if i['id']==62:
                bet_val = i['bet']
                check_obj = Market_6_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_6_Bets(
                                rid=resp.id,
                                money_bet_2 = market6_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market6_last_bet.price_2  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market6_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market6_last_bet.price_2  
                    db.session.commit()

            if i['id']==63:
                bet_val = i['bet']
                check_obj = Market_6_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_6_Bets(
                                rid=resp.id,
                                money_bet_3 = market6_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,
                                price_3 = market6_last_bet.price_3  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market6_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = market6_last_bet.price_3  
                    db.session.commit()

            """Market_7"""
            if i['id']==71:   
                bet_val = i['bet']
                check_obj = Market_7_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_7_Bets(
                                rid=resp.id,
                                money_bet_1 = market7_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,
                                price_1 = market7_last_bet.price_1    
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market7_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market7_last_bet.price_1
                    db.session.commit()

            if i['id']==72:
                bet_val = i['bet']
                check_obj = Market_7_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_7_Bets(
                                rid=resp.id,
                                money_bet_2 = market7_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market7_last_bet.price_2  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market7_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market7_last_bet.price_2  
                    db.session.commit()

            if i['id']==73:
                bet_val = i['bet']
                check_obj = Market_7_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_7_Bets(
                                rid=resp.id,
                                money_bet_3 = market7_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,
                                price_3 = market7_last_bet.price_3  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market7_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = market7_last_bet.price_3  
                    db.session.commit()

            """Market_8"""
            if i['id']==81:
                bet_val = i['bet']
                check_obj = Market_8_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_8_Bets(
                                rid=resp.id,
                                money_bet_1 = market8_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,
                                price_1 = market8_last_bet.price_1  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market8_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market8_last_bet.price_1  
                    db.session.commit()

            if i['id']==82:
                bet_val = i['bet']
                check_obj = Market_8_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_8_Bets(
                                rid=resp.id,
                                money_bet_2 = market8_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market8_last_bet.price_2  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market8_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market8_last_bet.price_2
                    db.session.commit()

            if i['id']==83:
                bet_val = i['bet']
                check_obj = Market_8_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_8_Bets(
                                rid=resp.id,
                                money_bet_3 = market8_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,
                                price_3 = market8_last_bet.price_3  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market8_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = market8_last_bet.price_3  
                    db.session.commit()

            """Market_9"""
            if i['id']==91:
                bet_val = i['bet']
                check_obj = Market_9_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_9_Bets(
                                rid=resp.id,
                                money_bet_1 = market9_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                price_1 = market9_last_bet.price_1
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market9_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market9_last_bet.price_1
                    db.session.commit()

            if i['id']==92:
                bet_val = i['bet']
                check_obj = Market_9_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_9_Bets(
                                rid=resp.id,
                                money_bet_2 = market9_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market9_last_bet.price_2  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market9_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market9_last_bet.price_2  
                    db.session.commit()

            if i['id']==93:
                bet_val = i['bet']
                check_obj = Market_9_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj:
                    market_obj = Market_9_Bets(
                                rid=resp.id,
                                money_bet_3 = market9_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,  
                                price_3 = market9_last_bet.price_3
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market9_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = market9_last_bet.price_3

                    db.session.commit()

            """Market_10"""
            if i['id']==101:
                bet_val = i['bet']
                check_obj = Market_10_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_10_Bets(
                                rid=resp.id,
                                money_bet_1 = market10_last_bet.price_1 * bet_val,
                                bet_1 = bet_val,  
                                price_1 = market10_last_bet.price_1 
                                )
                    db.session.add(market_obj)  
                    db.session.commit()
                else:
                    check_obj.money_bet_1 = market10_last_bet.price_1 * bet_val
                    check_obj.bet_1 = bet_val
                    check_obj.price_1 = market10_last_bet.price_1 
                    db.session.commit()

            if i['id']==102:
                bet_val = i['bet']
                check_obj = Market_10_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_10_Bets(
                                rid=resp.id,
                                money_bet_2 = market10_last_bet.price_2 * bet_val,
                                bet_2 = bet_val,
                                price_2 = market10_last_bet.price_2  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()   
                else:
                    check_obj.money_bet_2 = market10_last_bet.price_2 * bet_val
                    check_obj.bet_2 = bet_val
                    check_obj.price_2 = market10_last_bet.price_2
                    db.session.commit()

            if i['id']==103:
                bet_val = i['bet']
                check_obj = Market_10_Bets.query.filter_by(rid=resp.id).first()
                if not check_obj: 
                    market_obj = Market_10_Bets(
                                rid=resp.id,
                                money_bet_3 = market10_last_bet.price_3 * bet_val,
                                bet_3 = bet_val,
                                price_3 = market8_last_bet.price_3  
                                )
                    db.session.add(market_obj)  
                    db.session.commit()    
                else:
                    check_obj.money_bet_3 = market10_last_bet.price_3 * bet_val
                    check_obj.bet_3 = bet_val
                    check_obj.price_3 = market8_last_bet.price_3
                    db.session.commit()

    """ make all unselected options as 0 in db. """
    market1_rid_obj = Market_1_Bets.query.filter_by(rid=resp.id).first()
    market2_rid_obj = Market_2_Bets.query.filter_by(rid=resp.id).first()
    market3_rid_obj = Market_3_Bets.query.filter_by(rid=resp.id).first()
    market4_rid_obj = Market_4_Bets.query.filter_by(rid=resp.id).first()
    market5_rid_obj = Market_5_Bets.query.filter_by(rid=resp.id).first()
    market6_rid_obj = Market_6_Bets.query.filter_by(rid=resp.id).first()
    market7_rid_obj = Market_7_Bets.query.filter_by(rid=resp.id).first()
    market8_rid_obj = Market_8_Bets.query.filter_by(rid=resp.id).first()
    market9_rid_obj = Market_9_Bets.query.filter_by(rid=resp.id).first()
    market10_rid_obj = Market_10_Bets.query.filter_by(rid=resp.id).first()

    """Market_1"""
    if market1_rid_obj:
        if not market1_rid_obj.bet_1:
            market1_rid_obj.bet_1 = 0
            market1_rid_obj.money_bet_1 = 0
            market1_rid_obj.price_1 = market1_last_bet.price_1

        if not market1_rid_obj.bet_2:
            market1_rid_obj.bet_2 = 0
            market1_rid_obj.money_bet_2 = 0
            market1_rid_obj.price_2 = market1_last_bet.price_2
        
        if not market1_rid_obj.bet_3:
            market1_rid_obj.bet_3 = 0
            market1_rid_obj.money_bet_3 = 0
            market1_rid_obj.price_3 = market1_last_bet.price_3

        if not market1_rid_obj.bet_4:
            market1_rid_obj.bet_4 = 0
            market1_rid_obj.money_bet_4 = 0
            market1_rid_obj.price_4 = market1_last_bet.price_4

    """Market_2"""
    if market2_rid_obj:
        if not market2_rid_obj.bet_1:
            market2_rid_obj.bet_1 = 0
            market2_rid_obj.money_bet_1 = 0
            market2_rid_obj.price_1 = market2_last_bet.price_1

        if not market2_rid_obj.bet_2:
            market2_rid_obj.bet_2 = 0
            market2_rid_obj.money_bet_2 = 0
            market2_rid_obj.price_2 = market2_last_bet.price_2
        
        if not market2_rid_obj.bet_3:
            market2_rid_obj.bet_3 = 0
            market2_rid_obj.money_bet_3 = 0
            market2_rid_obj.price_3 = market2_last_bet.price_3

        if not market2_rid_obj.bet_4:
            market2_rid_obj.bet_4 = 0
            market2_rid_obj.money_bet_4 = 0
            market2_rid_obj.price_4 = market2_last_bet.price_4
    
    """Market_3"""
    if market3_rid_obj:
        if not market3_rid_obj.bet_1:
            market3_rid_obj.bet_1 = 0
            market3_rid_obj.money_bet_1 = 0
            market3_rid_obj.price_1 = market3_last_bet.price_1

        if not market3_rid_obj.bet_2:
            market3_rid_obj.bet_2 = 0
            market3_rid_obj.money_bet_2 = 0
            market3_rid_obj.price_2 = market3_last_bet.price_2

        if not market3_rid_obj.bet_3:
            market3_rid_obj.bet_3 = 0
            market3_rid_obj.money_bet_3 = 0
            market3_rid_obj.price_3 = market3_last_bet.price_3

        if not market3_rid_obj.bet_4:
            market3_rid_obj.bet_4 = 0
            market3_rid_obj.money_bet_4 = 0
            market3_rid_obj.price_4 = market3_last_bet.price_4
            
    """Market_4"""
    if market4_rid_obj:
        if not market4_rid_obj.bet_1:
            market4_rid_obj.bet_1 = 0
            market4_rid_obj.money_bet_1 = 0
            market4_rid_obj.price_1 = market4_last_bet.price_1

        if not market4_rid_obj.bet_2:
            market4_rid_obj.bet_2 = 0
            market4_rid_obj.money_bet_2 = 0
            market4_rid_obj.price_2 = market4_last_bet.price_2

    """Market_5"""
    if market5_rid_obj:
        if not market5_rid_obj.bet_1:
            market5_rid_obj.bet_1 = 0
            market5_rid_obj.money_bet_1 = 0
            market5_rid_obj.price_1 = market5_last_bet.price_1

        if not market5_rid_obj.bet_2:
            market5_rid_obj.bet_2 = 0
            market5_rid_obj.money_bet_2 = 0
            market5_rid_obj.price_2 = market5_last_bet.price_2
        
        if not market5_rid_obj.bet_3:
            market5_rid_obj.bet_3 = 0
            market5_rid_obj.money_bet_3 = 0
            market5_rid_obj.price_3 = market5_last_bet.price_3

    """Market_6"""
    if market6_rid_obj:
        if not market6_rid_obj.bet_1:
            market6_rid_obj.bet_1 = 0
            market6_rid_obj.money_bet_1 = 0
            market6_rid_obj.price_1 = market6_last_bet.price_1

        if not market6_rid_obj.bet_2:
            market6_rid_obj.bet_2 = 0
            market6_rid_obj.money_bet_2 = 0
            market6_rid_obj.price_2 = market6_last_bet.price_2
        
        if not market6_rid_obj.bet_3:
            market6_rid_obj.bet_3 = 0
            market6_rid_obj.money_bet_3 = 0
            market6_rid_obj.price_3 = market6_last_bet.price_3

    """Market_7"""
    if market7_rid_obj:
        if not market7_rid_obj.bet_1:
            market7_rid_obj.bet_1 = 0
            market7_rid_obj.money_bet_1 = 0
            market7_rid_obj.price_1 = market7_last_bet.price_1

        if not market7_rid_obj.bet_2:
            market7_rid_obj.bet_2 = 0
            market7_rid_obj.money_bet_2 = 0
            market7_rid_obj.price_2 = market7_last_bet.price_2
        
        if not market7_rid_obj.bet_3:
            market7_rid_obj.bet_3 = 0
            market7_rid_obj.money_bet_3 = 0
            market7_rid_obj.price_3 = market7_last_bet.price_3

    """Market_8"""
    if market8_rid_obj:
        if not market8_rid_obj.bet_1:
            market8_rid_obj.bet_1 = 0
            market8_rid_obj.money_bet_1 = 0
            market8_rid_obj.price_1 = market8_last_bet.price_1

        if not market8_rid_obj.bet_2:
            market8_rid_obj.bet_2 = 0
            market8_rid_obj.money_bet_2 = 0
            market8_rid_obj.price_2 = market8_last_bet.price_2
        
        if not market8_rid_obj.bet_3:
            market8_rid_obj.bet_3 = 0
            market8_rid_obj.money_bet_3 = 0
            market8_rid_obj.price_3 = market8_last_bet.price_3

    """Market_9"""
    if market9_rid_obj:
        if not market9_rid_obj.bet_1:
            market9_rid_obj.bet_1 = 0
            market9_rid_obj.money_bet_1 = 0
            market9_rid_obj.price_1 = market9_last_bet.price_1

        if not market9_rid_obj.bet_2:
            market9_rid_obj.bet_2 = 0
            market9_rid_obj.money_bet_2 = 0
            market9_rid_obj.price_2 = market9_last_bet.price_2
        
        if not market9_rid_obj.bet_3:
            market9_rid_obj.bet_3 = 0
            market9_rid_obj.money_bet_3 = 0
            market9_rid_obj.price_3 = market9_last_bet.price_3

    """Market_10"""
    if market10_rid_obj:
        if not market10_rid_obj.bet_1:
            market10_rid_obj.bet_1 = 0
            market10_rid_obj.money_bet_1 = 0
            market10_rid_obj.price_1 = market10_last_bet.price_1

        if not market10_rid_obj.bet_2:
            market10_rid_obj.bet_2 = 0
            market10_rid_obj.money_bet_2 = 0
            market10_rid_obj.price_2 = market10_last_bet.price_2
        
        if not market10_rid_obj.bet_3:
            market10_rid_obj.bet_3 = 0
            market10_rid_obj.money_bet_3 = 0
            market10_rid_obj.price_3 = market10_last_bet.price_3
    
    db.session.commit()
    body = []
    body.append({'rid':resp.rid, 'time_ended':resp.time_submitted, 'selected_options':fe_respo})
    return {'body': body, 'message': SUCCESS_MESSAGE['survey_ended']}
