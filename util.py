from app import Market_1,Market_2,Market_3,Market_4,Market_5,Market_6,Market_7,Market_8,Market_9,Market_10


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
    resp= RID.query.filter_by(rid=Rid).first()
    body = []
    body.append({
            'rid':resp.rid, 
            'time_started':resp.time_started, 
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


def unselected_options_set_0(resp):
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

