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
        Rid_check = RID.query.all()
        for i in Rid_check:
            if i.rid == Rid:
                return {'message':ERROR_MESSAGE['rid_used']}
        
        RID_obj = RID(rid=Rid)
        db.session.add(RID_obj)  
        db.session.commit()

    """this is for get the latest price of options in all markets"""
    return show_latest_prices(Rid,db)

"""End survey API"""

@app.route('/api/end_survey', methods=['GET','POST'])
@cross_origin()
def end_survey():

    if request.method=='POST':
        data = request.get_json()

    """get the rid Object for rid.id"""
    resp= RID.query.filter_by(rid=Rid).first()

    if resp:
        resp.time_submitted = datetime.now()
        db.session.commit()
    else:
        return {'msg':ERROR_MESSAGE['id_not_found']}
    

    """get the last obj of markets."""
    return store_FE_response_data(data,resp)

"""prices API"""

@app.route('/api/prices')
@cross_origin()
def prices():
    return update_all_market_prices(Rid)
