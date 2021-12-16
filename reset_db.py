"""step 1: go to the EleplantSQL account, login
   step 2: go to "market_db". in Details you can see 'reset' option.
   step 3: after reset done, you have to go to heroku account.
   step 4: go to "personal", then select "market-flask-app".
   step 5: click "more" option from top-right corner.
   step 6: you can see the "run console" option there.click on it.
   step 7: you see the text-box there. type "python" then run it.
   step 8: python console is open there. Now type "python reset_db.py" then run it.

"""

from market_app.models import db
from market_app.utils import initial_values_for_markets
db.create_all()
initial_values_for_markets(db)
