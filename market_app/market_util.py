from .models import *
from .constant import *

def store_FE_response_data(data,resp):

    fe_respo = dict(data)
    
    """ get the last obj of markets. """
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

    """ this for loop iterate over response and classify it with market obj """

    for key,value in fe_respo.items():

        option_list = fe_respo[key]['options']

        for i in option_list:

            """Market_1"""
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

            """Market_2"""
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

            """Market_3"""
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
                    
            """Market_4"""
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


            """Market_5"""
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

            """Market_6"""
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

            """Market_7"""
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

            """Market_8"""
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

            """Market_9"""
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

            """Market_10"""
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

    """ make all unselected options as 0 in db. """
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

    """Market_1"""
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

    """Market_2"""
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
    
    """Market_3"""
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
            
    """Market_4"""
    if market4_rid_obj:
        if not market4_rid_obj.bet_1:
            market4_rid_obj.bet_1 = 0
            market4_rid_obj.money_bet_1 = 0
            market4_rid_obj.price_1 = 0

        if not market4_rid_obj.bet_2:
            market4_rid_obj.bet_2 = 0
            market4_rid_obj.money_bet_2 = 0
            market4_rid_obj.price_2 = 0

    """Market_5"""
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

    """Market_6"""
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

    """Market_7"""
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

    """Market_8"""
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

    """Market_9"""
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

    """Market_10"""
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
    return {'body': body, 'message': SUCCESS_MESSAGE['survey_ended']}
