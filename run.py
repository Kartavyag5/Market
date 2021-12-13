from market_app import create_app
from market_app.routes import *
from market_app.models import app
from market_app.utils import initial_values_for_markets


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    initial_values_for_markets(db)
    app.run(debug=True, threaded=True)
