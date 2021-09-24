from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "9513b0b66a8546799bb12ddb3fb80755"

username = "root"
password = ""
host = "localhost"
database = "market"

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/market'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Market(db.Model):
    market_name = db.Column(db.String(255), nullable=False, unique=True)
    market_info = db.Column(db.String)
    question = db.Column(db.String(500), unique=True)
    
    option_1 = db.Column(db.String(500), unique=True)
    option_2 = db.Column(db.String(500), unique=True)
    option_3 = db.Column(db.String(500), unique=True, nullable=True)
    option_4 = db.Column(db.String(500), unique=True, nullable=True)
    option_5 = db.Column(db.String(500), unique=True, nullable=True)
    option_6 = db.Column(db.String(500), unique=True, nullable=True)
    option_7 = db.Column(db.String(500), unique=True, nullable=True)
    option_8 = db.Column(db.String(500), unique=True, nullable=True)
    
    price_op1 = db.Column(db.Integer())
    price_op2 = db.Column(db.Integer())
    price_op3 = db.Column(db.Integer(), nullable=True)
    price_op4 = db.Column(db.Integer(), nullable=True)
    price_op5 = db.Column(db.Integer(), nullable=True)
    price_op6 = db.Column(db.Integer(), nullable=True)
    price_op7 = db.Column(db.Integer(), nullable=True)
    price_op8 = db.Column(db.Integer(), nullable=True)
    
    quntity_op1 = db.Column(db.Integer(), nullable=True)
    quntity_op2 = db.Column(db.Integer(), nullable=True)
    quntity_op3 = db.Column(db.Integer(), nullable=True)
    quntity_op4 = db.Column(db.Integer(), nullable=True)
    quntity_op5 = db.Column(db.Integer(), nullable=True)
    quntity_op6 = db.Column(db.Integer(), nullable=True)
    quntity_op7 = db.Column(db.Integer(), nullable=True)
    quntity_op8 = db.Column(db.Integer(), nullable=True)

    # op1_total = db.Column(db.Integer())
    # op2_total = db.Column(db.Integer())
    # op3_total = db.Column(db.Integer(), nullable=True)
    # op4_total = db.Column(db.Integer(), nullable=True)
    # op5_total = db.Column(db.Integer(), nullable=True)
    # op6_total = db.Column(db.Integer(), nullable=True)
    # op7_total = db.Column(db.Integer(), nullable=True)
    # op8_total = db.Column(db.Integer(), nullable=True)

    # grand_total = db.Column(db.Integer(),range(max=10))

    def __repr__(self):
        return f"{self.market_name}"


db.create_all()

# run flask app
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
