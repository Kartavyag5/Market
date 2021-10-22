from market_app import create_app
from market_app.routes import *
from market_app.models import app

# app = create_app()

if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(debug=True)