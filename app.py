#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask_restful import reqparse #For get query params
from flask_restful import Api, Resource
from flask.ext.sqlalchemy import SQLAlchemy
import json
import os


app = Flask(__name__)
api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/amritatoday'
db = SQLAlchemy(app)


##ADD time field in canteens tables in heroku.


#ThingsTODO
#1. Default value for rating and event count.
#2. Count functionality

#3. PUT, DELETE FOR Clubs (add/delete new clubs)

#4. ADD post time for menu DB, POST

#5. Query based params for Menu


##########################################################################################
# DB CLASS MODELS #
##########################################################################################

#Canteen Class models
class Main(db.Model):
    __tablename__ = "main"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    rating = db.Column(db.Float)
    category = db.Column(db.String(20))

class MBA(db.Model):
    __tablename__ = "mba"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    rating = db.Column(db.Float)
    category = db.Column(db.String(20))

class IT(db.Model):
    __tablename__ = "it"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    rating = db.Column(db.Float)
    category = db.Column(db.String(20))
#End of Canteen Class models


#Clubs Class models
class Clubs(db.Model):
    __tablename__ = "clubs"
    id = db.Column(db.Integer, primary_key=True)
    club = db.Column(db.String(20), unique=True)
#End of Clubs Class models


#ClubEvent Class models
class ClubEvents(db.Model):
    __tablename__ = "clubevents"
    id = db.Column(db.Integer, primary_key=True)
    club = db.Column(db.String(20), unique=True)
    event = db.Column(db.String(20))
    description = db.Column(db.String(1000))
    date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    venue = db.Column(db.String(20))
    poster = db.Column(db.String(200))
    count = db.Column(db.Integer)
#End of ClubEvent Class models

#Buy/Sell Class models
class BuySell(db.Model):
    __tablename__ = "buysell"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20))
    category = db.Column(db.String(20))
    price = db.Column(db.Integer)
    orig_price = db.Column(db.Integer)
    description = db.Column(db.String(200))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
#End of Buy/Sell Class models


##########################################################################################
# HTTP verbs' definitions #
##########################################################################################

#Start Canteen Defintions
#GET (LIST) and POST ONLY
class MainMenuListAPI(Resource):
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
        time = data['time']
        MainMenuADD = Main(item=item,price=price,time=time,category=category)
        db.session.add(MainMenuADD)
        db.session.commit()
        return 201

class MBAMenuListAPI(Resource):
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
        time = data['time']
        MBAMenuADD = MBA(item=item,price=price, time=time, category=category)
        db.session.add(MBAMenuADD)
        db.session.commit()
        return 201

class ITMenuListAPI(Resource):
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
        time = data['time']
        ITMenuADD = IT(item=item, price=price, time=time, category=category)
        db.session.add(ITMenuADD)
        db.session.commit()
        return 201



#GET (ID) and PUT,DELETE

class MainMenuAPI(Resource):
    def get(self,id):
        Menu=[]
        Menu.append(Main.query.filter_by(id=id).first().__dict__)
        del Menu[0]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'Main':(Menu) })

    def put(self,id):    
        data=request.json
        MainMenuUpdate = Main.query.filter_by(id=id).first()
        MainMenuUpdate.item = data['item']
        MainMenuUpdate.price = data['price']
        MainMenuUpdate.category = data['category']
        MainMenuUpdate.time = data['time']
        db.session.add(MainMenuUpdate)
        db.session.commit()
        return 201

    def delete(self,id):
        Main.query.filter_by(id=id).delete()
        db.session.commit()
        return 201 #Remember to return error code if entry is NOT deleted from DB


class MBAMenuAPI(Resource):
    def get(self,id):
        Menu=[]
        Menu.append(MBA.query.filter_by(id=id).first().__dict__)
        del Menu[0]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'MBA':(Menu) })

    def put(self,id):    
        data=request.json
        MBAMenuUpdate = MBA.query.filter_by(id=id).first()
        MBAMenuUpdate.item = data['item']
        MBAMenuUpdate.price = data['price']
        MBAMenuUpdate.category = data['category']
        MBAMenuUpdate.time = data['time']
        db.session.add(MBAMenuUpdate)
        db.session.commit()
        return 201

    def delete(self,id):
        MBA.query.filter_by(id=id).delete()
        db.session.commit()
        return 201 #Remember to return error code if entry is NOT deleted from DB


class ITMenuAPI(Resource):
    def get(self,id):
        Menu=[]
        Menu.append(IT.query.filter_by(id=id).first().__dict__)
        del Menu[0]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'IT':(Menu) })

    def put(self,id):    
        data=request.json
        ITMenuUpdate = IT.query.filter_by(id=id).first()
        ITMenuUpdate.item = data['item']
        ITMenuUpdate.price = data['price']
        ITMenuUpdate.category = data['category']
        MBAMenuUpdate.time = data['time']
        db.session.add(ITMenuUpdate)
        db.session.commit()
        return 201

    def delete(self,id):
        IT.query.filter_by(id=id).delete()
        db.session.commit()
        return 201 #Remember to return error code if entry is NOT deleted from DB
#End of Canteen Definitions



#Start of Clubs Definition
#GET ONLY
class ClubsListAPI(Resource):
    def get(self):
        ClubList=[]
        for u in Clubs.query.all():
            ClubList.append(u.__dict__)
        for i in range(len(ClubList)):
            del ClubList[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'Clubs':(ClubList) })      
#End of Clubs Definition


#Start of ClubEvents Defintions
#GET (LIST) and POST ONLY
class ClubEventsListAPI(Resource):
    def get(self):
        Events=[]

        parser = reqparse.RequestParser()
        parser.add_argument('club', action='append')
        args = parser.parse_args()

        if args.club is not None:
            ClubIDs = []        
            ClubIDs = list(args.club)

            for u in ClubEvents.query.filter(ClubEvents.club.in_(ClubIDs)).all():
                Events.append(u.__dict__)

        else:
            for u in ClubEvents.query.all():
                Events.append(u.__dict__)    

        for i in range(len(Events)):
            del Events[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'Events':(Events) })     

    def post(self):
        data = request.json
        club = data['club']
        event = data['event']
        description = data['description']
        date = data['date']
        end_date = data['end_date']
        venue = data['venue']
        poster = data['poster']

        ClubEventsADD = ClubEvents(club=club,event=event,description=description,date=date,end_date=end_date,venue=venue,poster=poster)
        db.session.add(ClubEventsADD)
        db.session.commit()
        return 201

#GET (ID), PUT, DELETE
class ClubEventsAPI(Resource):
    def get(self,id):
        Events=[]
        Events.append(ClubEvents.query.filter_by(id=id).first().__dict__)
        del Events[0]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'Events':(Events) })

    def put(self,id):    
        data=request.json
        ClubEventsUpdate = ClubEvents.query.filter_by(id=id).first()
        ClubEventsUpdate.club = data['club']
        ClubEventsUpdate.event = data['event']
        ClubEventsUpdate.description = data['description']
        ClubEventsUpdate.date = data['date']
        ClubEventsUpdate.end_date = data['end_date']
        ClubEventsUpdate.venue = data['venue']
        ClubEventsUpdate.poster = data['poster']

        db.session.add(ClubEventsUpdate)
        db.session.commit()
        return 201

    def delete(self,id):
        ClubEvents.query.filter_by(id=id).delete()
        db.session.commit()
        return 201 #Remember to return error code if entry is NOT deleted from DB
#End of ClubEvent Defintions

#Start of BuySell Definitions
class BuyListAPI(Resource):
    def get(self):
        BuyList=[]
        for u in BuySell.query.all():
            BuyList.append(u.__dict__)
        for i in range(len(BuyList)):
            del BuyList[i]['_sa_instance_state'] #Delete uncessary parameter in return object
        return jsonify({'BuyList':(BuyList) })     


class SellAPI(Resource):
    def post(self):
        data = request.json
        item = data['item']
        category = data['category']
        price = data['price']
        orig_price = data['orig_price']
        description = data['description']
        email = data['email']
        phone = data['phone']

        BuySellADD = BuySell(item=item, category=category, price=price, orig_price=orig_price, description=description, email=email, phone=phone)
        db.session.add(BuySellADD)
        db.session.commit()
        return 201


class SellModAPI(Resource):
    def put(self,id):    
        data=request.json
        BuySellUpdate = BuySell.query.filter_by(id=id).first()
        BuySellUpdate.item = data['item']
        BuySellUpdate.category = data['category']
        BuySellUpdate.price = data['price']
        BuySellUpdate.orig_price = data['orig_price']
        BuySellUpdate.description = data['description']
        BuySellUpdate.email = data['email']
        BuySellUpdate.phone = data['phone']

        db.session.add(BuySellUpdate)
        db.session.commit()
        return 201

    def delete(self,id):
        BuySell.query.filter_by(id=id).delete()
        db.session.commit()
        return 201 #Remember to return error code if entry is NOT deleted from DB
#End of BuySell Definitions




##########################################################################################
# Routes #
##########################################################################################

##CANTEEN
#GET (LIST), POST 
api.add_resource(MainMenuListAPI,'/api/v1.0/menu/main')
api.add_resource(MBAMenuListAPI,'/api/v1.0/menu/mba')
api.add_resource(ITMenuListAPI,'/api/v1.0/menu/it')
#GET (ID), PUT, DELETE
api.add_resource(MainMenuAPI,'/api/v1.0/menu/main/<int:id>')
api.add_resource(MBAMenuAPI,'/api/v1.0/menu/mba/<int:id>')
api.add_resource(ITMenuAPI,'/api/v1.0/menu/it/<int:id>')
##END CANTEEN APIS


##CLUBS
#GET (LIST), POST 
api.add_resource(ClubEventsListAPI,'/api/v1.0/events') #list of all events eg: /api/v1.0/events returns all events. Or, eg: /api/v1.0/events?club=T{know} returns events of T{know} alone
#GET (ID), PUT, DELETE
api.add_resource(ClubEventsAPI,'/api/v1.0/events/<int:id>') #events based on id
#GET ONLY - ClusListAPI
api.add_resource(ClubsListAPI,'/api/v1.0/clubs')  #for list of clubs
##END CLUBS APIS

##BUYSELL
#GET
api.add_resource(BuyListAPI,'/api/v1.0/buy')
#POST
api.add_resource(SellAPI,'/api/v1.0/sell')
#PUT, DELETE
api.add_resource(SellModAPI,'/api/v1.0/sell/<int:id>')
##END BUY SELL APIS

if __name__ == '__main__':
    app.run(debug=True)