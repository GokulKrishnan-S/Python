'''
Python Day 10
'''

#Rest API
from flask import Flask, request, abort, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError, validate
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from flask_restful import Api, Resource
from functools import wraps
import jwt
import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'PUBLICINSECURESECRET')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, name, password):
        self.name = name
        self.password = password

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veggie_name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, veggie_name, quantity):
        self.veggie_name = veggie_name
        self.quantity = quantity 

    def __repr__(self):
        return '<Grocery %r>' % self.veggie_name       


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ("name", "password")


class GrocerySchema(ma.SQLAlchemySchema):
    #Validations
    veggie_name = fields.Str(validate=validate.Length(min=1))
    quantity = fields.Int(validate=validate.Range(min=1, max=100))
    class Meta:
        fields = ("veggie_name","quantity")


db.create_all()

userSchema = UserSchema()
usersSchema = UserSchema(many = True)
grocery_schema = GrocerySchema()
groceries_schema = GrocerySchema(many=True) 


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            print(data)
            user = User.query.filter_by(
                id=data['id']
            ).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(user, *args, **kwargs)
    
    return wrapper        



class Registration(Resource):
    def post(self):
        hashed_password = generate_password_hash(request.json['password'], method='sha256')
        new_user = User(name=request.json['name'],  password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'registered successfully'})

class Login(Resource):
    def post(self):
        auth = request.authorization
        user = User.query.filter_by(name=auth.username).first()
        if user is None:
            return 'Could not verify username or pass', 401
        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])
            return jsonify({'token': token})
        return make_response('could not verify username/ pass', 401)


class CreateAndRead(Resource):
    @token_required
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
    @token_required
    def put(self, veggie):
        veggie_in_db = Grocery.query.filter_by(veggie_name = veggie).first()
        if veggie_in_db == None:
            abort(404, message="Veggie not found")
        veggie_in_db.quantity =  request.json['quantity']
        db.session.commit()

        return f"{veggie_in_db.veggie_name} updated successfully", 202 

    @token_required
    def delete(self, veggie):
        veggie_in_db = Grocery.query.filter_by(veggie_name = veggie).first()
        if veggie_in_db == None:
            abort(404, message="Veggie not found")
        db.session.delete(veggie_in_db)
        db.session.commit()
        return "Successfully Deleted", 200


api.add_resource(Registration, '/register')
api.add_resource(Login, '/login')
api.add_resource(CreateAndRead, '/veggies')
api.add_resource(UpdateAndDelete, '/veggies/<veggie_name>')

if __name__ == "__main__": 
	app.run(debug = True)







