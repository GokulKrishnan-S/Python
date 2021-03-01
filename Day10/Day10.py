'''
Python Day 10
'''

#Rest API
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError, validate
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

api = Api(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veggie_name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, veggie_name, quantity):
        self.veggie_name = veggie_name
        self.quantity = quantity 

    def __repr__(self):
        return '<Grocery %r>' % self.veggie_name       


class GrocerySchema(ma.SQLAlchemySchema):
    #Validations
    veggie_name = fields.Str(validate=validate.Length(min=1))
    quantity = fields.Int(validate=validate.Range(min=1, max=100))
    class Meta:
        fields = ("veggie_name","quantity")

db.create_all()
grocery_schema = GrocerySchema()
groceries_schema = GrocerySchema(many=True) 

class CreateAndRead(Resource):
    def post(self):
        new_grocery = Grocery(veggie_name = request.json['veggie_name'], quantity = request.json['quantity'])
        veggie_name = request.json.get('veggie_name')
        if Grocery.query.filter_by(veggie_name = veggie_name).first() is not None:
            abort(400, message = f"Veggie {veggie_name} already exists.") 
        try:         
            db.session.add(new_grocery) 
            db.session.commit()    
            return f"Veggie {request.json['veggie_name']} has been added and the quantity is {request.json['quantity']}. ", 201 
        #Handling Validation Error
        except ValidationError as err:
            print(err.messages)


    def get(self):
        veggies = Grocery.query.all()
        return groceries_schema.dump(veggies), 200


class UpdateAndDelete(Resource):
    def put(self, veggie):
        veggie_in_db = Grocery.query.filter_by(veggie_name = veggie).first()
        if veggie_in_db == None:
            abort(404, message="Veggie not found")
        veggie_in_db.quantity =  request.json['quantity']
        db.session.commit()

        return f"{veggie_in_db.veggie_name} updated successfully", 202 


    def delete(self, veggie):
        veggie_in_db = Grocery.query.filter_by(veggie_name = veggie).first()
        if veggie_in_db == None:
            abort(404, message="Veggie not found")
        db.session.delete(veggie_in_db)
        db.session.commit()
        return "Successfully Deleted", 200


api.add_resource(CreateAndRead, '/veggies')
api.add_resource(UpdateAndDelete, '/veggies/<veggie_name>')









