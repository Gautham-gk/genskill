from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'

db=SQLAlchemy(app)


class Item(db.Model):
# This is a model which will be table inside Database
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False,unique=True)
    price=db.Column(db.Integer(),nullable=False)
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)
    description=db.Column(db.String(),nullable=False)

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')


@app.route("/market")
def market():
    items=Item.query.all()


#     items = [
#     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
#     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
#     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
# ]
    return render_template('market.html',items=items)


@app.route("/about/<name>")
def about_page(name):
    return f"Hello {name}"
