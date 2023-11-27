from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import g
from peewee import *


appbe = Flask ( __name__ )
appbe.config.from_object(__name__)
api = Api(appbe)


DATABASE = 'database.db'
PORT     = 8001


db = SqliteDatabase( DATABASE )

# Database model for user entries

class Users(Model):
   # peewee generates the id automatically as primary key
   #   id = IntegerField( unique=True, primary_key = True )
   username = CharField()
   password = CharField()

   class Meta:
       database = db

def getUserList():
    rows = list(Users.select().dicts()) 
    return rows

def insertUser ( username, password ):
    handle = Users ( username = username, password = password )
    handle.save()
    return handle


parser = reqparse.RequestParser()

class UserList(Resource):
    def get(self):
        return getUserList()

    def post(self):
        parser.add_argument( "username" )
        parser.add_argument( "password" )

        args = parser.parse_args()

        insertUser ( args["username"], args["password"] )

        return 201

api.add_resource(UserList, '/users/' )

if __name__ == '__main__':
    appbe.run( debug = True, port = PORT )
    

@appbe.before_request
def before_request():
    g.db = database
    g.db.connect()

@appbe.after_request
def after_request(response):
    g.db.close()