'''
Day 8
Python Practice Programs 
'''

#Programs 1 and 2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veggie_name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Grocery %r>' % self.veggie_name


class GrocerySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Grocery
        load_instance = True

    id = ma.auto_field()
    veggie_name = ma.auto_field()
    quantity = ma.auto_field()


db.create_all()
grocery_schema = GrocerySchema()
veggie1 = Grocery(veggie_name = "Carrot", quantity = 5)
veggie2 = Grocery(veggie_name = "Capsicum", quantity = 3)
db.session.add(veggie1)
db.session.add(veggie2)
db.session.commit()
grocery_schema.dump(veggie1)
grocery_schema.dump(veggie2)
      



