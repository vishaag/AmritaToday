#!flask/bin/python
from flask import Flask, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

tasks = [
    {
        'id': 1,
        'item': u'Chappathi Channa',
        'price': u'10+20', 
        'done': False
    },
    {
        'id': 2,
        'item': u'Apple MilkShake',
        'price': u'50', 
        'done': False
    }
]

# @app.route('/amritatoday/api/v1.0/menu', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})

class Menu(Resource):
    def get(self):
        return jsonify({'tasks': tasks})

api.add_resource(Menu,'/api/v1.0/menu')

if __name__ == '__main__':
    app.run(debug=True)
