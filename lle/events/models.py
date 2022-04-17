from sqlite3 import Date
from xmlrpc.client import DateTime
from mongoengine import *

class Events(Document):
    meta = {
        'db_alias': 'limitedlemonadedb',
        'collection': 'events'
    }
    address = StringField()
    startDt = DateTimeField()
    endDt = DateTimeField()
    createdDt = DateTimeField()
    title = StringField()
    city = StringField()
    state = StringField()
    zip = IntField()
    country = StringField()
    updatedDt = DateTimeField()
