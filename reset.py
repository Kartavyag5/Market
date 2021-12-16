from market_app.models import db
from market_app.utils import initial_values_for_markets

def reset():
    db.create_all()
    return initial_values_for_markets(db)

reset()
