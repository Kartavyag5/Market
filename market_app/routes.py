from flask import request
from datetime import datetime
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from .utils import *
from .market_util import *
from .models import *

load_dotenv()

"""global variable for get value in all page"""
started_time = 'no time'
data = 'no data'

"""this is data of sum of market all money"""

"""Start Survey API"""

@app.route('/api/start_survey', methods=['POST'])
@cross_origin()
def start_survey():
    initial_values_for_markets(db)

    """when you give rid in post request, every time new rid obj created with datetime.now()
    you have to give unique rid in request."""
    if request.method=='POST':
        Rid = request.form['rid']
        
        global started_time
        started_time = datetime.now()
        
    """this is for get the latest price of options in all markets"""
    return show_latest_prices(Rid,db,started_time)


"""End survey API"""

@app.route('/api/end_survey', methods=['GET','POST'])
@cross_origin()
def end_survey():

    if request.method=='POST':
        """FE response data"""
        global data
        data = request.get_json()

        Rid_check = RID.query.all()
        for i in Rid_check:
            if i.rid == data['rid']:
                return {'message':ERROR_MESSAGE['rid_used']}
        
        RID_obj = RID(rid=data['rid'], time_started=started_time, time_submitted = datetime.now())
        db.session.add(RID_obj)
        db.session.commit()

    resp= RID.query.filter_by(rid=data['rid']).first()    

    """get the last obj of markets."""
    return store_FE_response_data(data,resp)

"""prices API"""

@app.route('/api/prices')
@cross_origin()
def prices():
    Rid_startTime_EndTime_Added_to_Market_bets(db)
    return update_all_market_prices(data['rid'])
    
    
