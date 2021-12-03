from flask import request
from datetime import datetime
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from .utils import *
from .market_util import *
from .models import *

load_dotenv()

"""global variable for get value in all page"""
Rid = 'no id'
started_time = 'no time'
prices_user_see = 'no prices'

"""this is data of sum of market all money"""

"""Start Survey API"""

@app.route('/api/start_survey', methods=['POST'])
@cross_origin()
def start_survey():
    initial_values_for_markets(db)

    """when you give rid in post request, every time new rid obj created with datetime.now()
    you have to give unique rid in request."""
    if request.method=='POST':
        global Rid
        Rid = request.form['rid']
        global started_time
        started_time = datetime.now()
        
    """this is for get the latest price of options in all markets"""
    global prices_user_see
    prices_user_see = prices_seen_by_user(Rid,db,started_time)

    return show_latest_prices(Rid,db,started_time)


"""End survey API"""

@app.route('/api/end_survey', methods=['GET','POST'])
@cross_origin()
def end_survey():

    if request.method=='POST':
        Rid_check = RID.query.all()
        for i in Rid_check:
            if i.rid == Rid:
                return {'message':ERROR_MESSAGE['rid_used']}
        
        RID_obj = RID(rid=Rid, time_started=started_time)
        db.session.add(RID_obj)
        db.session.commit()
        
        """FE response data"""
        data = request.get_json()

    """get the rid Object for rid.id"""
    resp= RID.query.filter_by(rid=Rid).first()

    if resp:
        resp.time_submitted = datetime.now()
        db.session.commit()
    else:
        return {'msg':ERROR_MESSAGE['id_not_found']}
    

    """get the last obj of markets."""
    return store_FE_response_data(data,resp,prices_user_see)

"""prices API"""

@app.route('/api/prices')
@cross_origin()
def prices():
    Rid_startTime_EndTime_Added_to_Market_bets(db)
    return update_all_market_prices(Rid)
    
    
