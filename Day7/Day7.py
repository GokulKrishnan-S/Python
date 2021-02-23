from flask import Flask, request, jsonify
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

data = [
    {
        'name': 'Carrot',
        'qty': 3,
    },
    {
        'name': 'Tomato',
        'qty': 7
    },
    {
        'name': 'Cabbage',
        'qty': 2
    },
    {
        'name': 'Capsicum',
        'qty': 4
    }
]

def abort_if_veggie_doesnt_exist(veggie_name):
    if veggie_name not in data:
        abort(404, message="Veggie {} doesn't exist".format(veggie_name))

class GetVegetables(Resource):
    def get(self):
        return jsonify(data)

    def post(self):
        newveggie = {}
        newveggie['name'] = request.json['name']
        newveggie['qty'] = request.json['qty']
        data.append(newveggie)
        return request.json
        
class GetAVegetable(Resource):
    def get(self, name):
        for vege in data:
            if name == vege['name']
                return vege, 200
        abort_if_veggie_doesnt_exist(name)

    def put(self, name):
        for vege in data:
            if name == vege['name']:
                vege['qty'] = request.json['qty']
                return vege, 201
        abort_if_veggie_doesnt_exist(name)
        

    def delete(self, name):	
        for vege in data:
            if name == vege['name']:	
                del data['name']
                return '', 204
        abort_if_veggie_doesnt_exist(name)


api.add_resource(GetVegetables, '/vegetables')
api.add_resource(GetAVegetable, '/vegetables/<string:name>')
