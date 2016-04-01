#!flask/bin/python
from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask.ext.sqlalchemy import SQLAlchemy
import json
import os


app = Flask(__name__)
api = Api(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/amritatoday'
db = SQLAlchemy(app)


class Main(db.Model):
    __tablename__ = "main"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)
    rating = db.Column(db.Float)
    category = db.Column(db.String(20))

class MBA(db.Model):
    __tablename__ = "mba"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)
    rating = db.Column(db.Float)
    category = db.Column(db.String(20))

class IT(db.Model):
    __tablename__ = "it"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)
    rating = db.Column(db.Float)
    category = db.Column(db.String(20))


class MainMenu(Resource):
    def get(self):
        Menu=[]
        for u in Main.query.all():
            Menu.append(u.__dict__)
        for i in range(len(Menu)):
            del Menu[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'Main':(Menu) })


class MBAMenu(Resource):
    def get(self):
        Menu=[]
        for u in MBA.query.all():
            Menu.append(u.__dict__)
        for i in range(len(Menu)):
            del Menu[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'MBA':(Menu) })


class ITMenu(Resource):
    def get(self):
        Menu=[]
        for u in IT.query.all():
            Menu.append(u.__dict__)
        for i in range(len(Menu)):
            del Menu[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'IT':(Menu) })


api.add_resource(MainMenu,'/api/v1.0/menu/main')
api.add_resource(MBAMenu,'/api/v1.0/menu/mba')
api.add_resource(ITMenu,'/api/v1.0/menu/it')


if __name__ == '__main__':
    app.run(debug=True)