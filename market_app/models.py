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

""" Market-1 Prices """
class Market_1_Prices(db.Model):
    price_1 = db.Column(db.Float())
    price_2 = db.Column(db.Float())
    price_3 = db.Column(db.Float())
    update_time = db.Column(db.DateTime, default=datetime.now)


""" MARKET-1 Kodiak survery """
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


""" MARKET-2 Jeopardy! """
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


""" MARKET-3 BYU Football """
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

    
""" MARKET-4 No Time To Die """
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


""" MARKET-5 """
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


""" MARKET-6 """
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


""" MARKET-7 """
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


""" MARKET-8 """
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


""" MARKET-9 """
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


""" MARKET-10 """
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

# db.create_all()

# with app.app_context():
#     db.create_all()
