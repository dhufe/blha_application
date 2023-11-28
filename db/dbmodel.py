#####
# Simple ORM approach using Peewee for accessing a (SQLite) database.
# Peewee supports SQLite, MySQL, Postgres, and CockroachDB
# 
# Code abstracts the database scheme, establishes a connection and
# creates new users.
#
# Author: Daniel Hufschläger
# Date: 27.11.2023
# Last Modified: 28.11.2023
#####

from peewee import *

db = SqliteDatabase('database.db')

# Database model for user entries
class Users(Model):
   # peewee generates the id automatically as primary key
   #   id = IntegerField( unique=True, primary_key = True )
   username = CharField()
   password = CharField()

   class Meta:
       database = db

# Connect to database
db.connect()


def create_table():
    with db:
        db.create_tables([Users])

# function interface to ORM model 
# create an user with given password
def insertUser ( username, password ):
    handle = Users ( username = username, password = password )
    handle.save()
    return handle

# create tables according out model
create_table()

# create some users
insertUser ( 'hugo', 'T3stlauf')
insertUser ( 'daniel', 'p455w0rt')
insertUser ( 'birgit', 'ho53')
insertUser ( 'hans', 't35t')
insertUser ( 'steffi', 'gru3n')
insertUser ( 'torsten', '5chw4rz')

# be tidy closing db handle
db.close()
