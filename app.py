#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask_restful import Api, Resource
from flask.ext.sqlalchemy import SQLAlchemy
import json
import os


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/amritatoday'
db = SQLAlchemy(app)


##########################################################################################
# DB CLASS MODELS #
##########################################################################################


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


##########################################################################################
# HTTP verb definitions #
##########################################################################################


class MainMenu(Resource):
    def get(self):
        Menu=[]
        for u in Main.query.all():
            Menu.append(u.__dict__)
        for i in range(len(Menu)):
            del Menu[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'Main':(Menu) })

    def post(self):
        data = request.json
        item = data['item']
        price = data['price']
        category = data['category']
        MainMenuADD = Main(item=item,price=price,category=category)
        db.session.add(MainMenuADD)
        db.session.commit()
        return 201

    # def put(self):
    #     data = request.json
    #     item = data['item']
    #     price = data['price']
    #     category = data['category']     
    #     MainMenuUpdate = Menu.query.filter_by(item=item,price=price,category=category).first()

    def delete(self):
        data=request.json
        id = data['id']
        Main.query.filter_by(id=id).delete()
        db.session.commit()
        return 201 #Remember to return error code if entry is NOT deleted from DB


class MBAMenu(Resource):
    def get(self):
        Menu=[]
        for u in MBA.query.all():
            Menu.append(u.__dict__)
        for i in range(len(Menu)):
            del Menu[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'MBA':(Menu) })

    def post(self):
        data = request.json
        item = data['item']
        price = data['price']
        category = data['category']
        MBAMenuADD = MBA(item=item,price=price,category=category)
        db.session.add(MBAMenuADD)
        db.session.commit()
        return 201

    def delete(self):
        data=request.json
        id = data['id']
        MBA.query.filter_by(id=id).delete()
        db.session.commit()
        return 201 #Remember to return error code if entry is NOT deleted from DB


class ITMenu(Resource):
    def get(self):
        Menu=[]
        for u in IT.query.all():
            Menu.append(u.__dict__)
        for i in range(len(Menu)):
            del Menu[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'IT':(Menu) })

    def post(self):
        data = request.json
        item = data['item']
        price = data['price']
        category = data['category']
        ITMenuADD = IT(item=item,price=price,category=category)
        db.session.add(ITMenuADD)
        db.session.commit()
        return 201

    def delete(self):
        data=request.json
        id = data['id']
        IT.query.filter_by(id=id).delete()
        db.session.commit()
        return 201 #Remember to return error code if entry is NOT deleted from DB


##########################################################################################
# Routes #
##########################################################################################

api.add_resource(MainMenu,'/api/v1.0/menu/main')
api.add_resource(MBAMenu,'/api/v1.0/menu/mba')
api.add_resource(ITMenu,'/api/v1.0/menu/it')


if __name__ == '__main__':
    app.run(debug=True)