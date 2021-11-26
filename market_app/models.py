from datetime import datetime
from dotenv import load_dotenv
from market_app import create_app
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = create_app(Config)
db = SQLAlchemy(app)
load_dotenv()


""" RID Model """
class RID(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    rid = db.Column(db.String(200), unique=True)
    time_started = db.Column(db.DateTime, default=datetime.now)
    time_submitted = db.Column(db.DateTime, nullable=True, default=None)
    
    def __repr__(self):
        return f"{self.rid}"

    def __repr__(self):
        return f"{self.time_started}:{self.time_submitted}"

"""
all market names:
    1. Kodiak Cakes Concept Test
    2. Jeopardy!
    3. BYU Football
    4. No Time To Die
    5. 
    6. 
    7. 
    8. 
    9. 
    10. 
"""

""" MARKET-1-Bets Kodiak survery """
class Market_1_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"),nullable=True, )
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)
    
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
    
    
""" Market-1 Prices """
class Market_1_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    price_4 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)


""" MARKET-2-Bets Jeopardy! """
class Market_2_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"), nullable=True)
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)
    
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

    
""" Market-2 Prices """
class Market_2_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    price_4 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)

    
""" MARKET-3-Bets BYU Football """
class Market_3_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"), nullable=True)
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)
    
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

    
""" Market-3 Prices """
class Market_3_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    price_4 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)
    
    
""" MARKET-4-Bets No Time To Die """
class Market_4_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"), nullable=True)
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)
    
    money_bet_1 = db.Column(db.Float())
    money_bet_2 = db.Column(db.Float())
    
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    
    bet_1 = db.Column(db.Integer())
    bet_2 = db.Column(db.Integer())

    def __repr__(self):
        return f"{self.rid.rid}"
    

""" Market-4 Prices """
class Market_4_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)


""" MARKET-5-Bets """
class Market_5_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"), nullable=True)
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)

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

    
""" Market-5 Prices """
class Market_5_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)
    
    
""" MARKET-6-Bets """
class Market_6_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"), nullable=True)
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)

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
    
    
""" Market-6 Prices """
class Market_6_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)


""" MARKET-7-Bets """
class Market_7_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"), nullable=True)
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)

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


""" Market-7 Prices """
class Market_7_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)
    
    
""" MARKET-8-Bets """
class Market_8_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"), nullable=True)
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)

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


""" Market-8 Prices """
class Market_8_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)
    
    
""" MARKET-9-Bets """
class Market_9_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"), nullable=True)
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)

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
    
    
""" Market-9 Prices """
class Market_9_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)


""" MARKET-10-Bets """
class Market_10_Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer(), db.ForeignKey(RID.id, ondelete="CASCADE"), nullable=True)
    rid_user = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True, default=None)

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
    
    
""" Market-10 Prices """
class Market_10_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)
    
    

# db.create_all()

# with app.app_context():
#     db.create_all()
