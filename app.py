#!flask/bin/python
from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask.ext.sqlalchemy import SQLAlchemy
import json



app = Flask(__name__)
api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)


class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)


class MenuList(Resource):
    def get(self):
        menu=[]
        for u in Menu.query.all():
            menu.append(u.__dict__)
        for i in range(len(menu)):
            del menu[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'menu':(menu) })


api.add_resource(MenuList,'/api/v1.0/menu')

if __name__ == '__main__':
    app.run(debug=True)
