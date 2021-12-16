"""
   ElephantSQL creadentials:
    id: kartavyag5@gmail.com
    password: market_database

   Heroku credentials:
   id: kartavyag5@gmail.com
   password: Market_app
      
   step 1: go to the EleplantSQL account, login.
   step 2: go to "market". in Details you can see 'reset' option.
   step 3: after reset done, you have to go to heroku account.
   step 4: go to "personal", then select "market-flask-app".
   step 5: click "more" option from top-right corner.
   step 6: you can see the "run console" option there.click on it.
   step 7: you see the text-box there. type "python reset.py" then run it.
   step 8: python console is open there. after one or two seconds later you can see "process exited" msg at bottom-left. close it.
   step 9: now you can see the db tables are created with initial values in ElephantSQL market db.

"""

from market_app.models import db
from market_app.utils import initial_values_for_markets
def reset():
    db.create_all()
    return initial_values_for_markets(db)

reset()
