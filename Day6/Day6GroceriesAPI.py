'''
Day 6 Groceries API
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/groceries', methods=['GET', 'POST'])
def groceries():
	if request.method == 'GET':
        return jsonify(data)
    else:
        new_grocery = {}
        new_grocery['name'] = request.json['name']
        new_grocery['qty'] = request.json['qty']
        data.append(new_grocery)
        return 'Added ' + request.json['name'] + '(s)' 




@app.route('/groceries/<string:name>', methods=['GET', 'DELETE'])
def getGrocery(name):
    if request.method == 'GET':
        for grocery in data:
            if name == grocery['name']:
                return grocery
        else:
            return 'Grocery item is not found', 404
    else:
        index = 0
        for grocery in data:
            if name == grocery['name']:
                data.pop(index)
                return 'Deleted ' + name + '(s)'    
            index += 1
        else:
            return 'Grocery item is not found', 404        