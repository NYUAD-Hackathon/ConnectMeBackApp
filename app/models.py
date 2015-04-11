from app import db, app
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy, BaseQuery


#Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    searchingForName = db.Column(db.String(120))
    message = db.Column(db.Text)
    phoneNumber = db.Column(db.String(30))

    def __init__(self, firstName, searchingForName, message, phoneNumber):
        self.firstName = firstName
        self.searchingForName = searchingForName
        self.message = message
        self.phoneNumber = phoneNumber

    #def __repr__(self):
        #return '<User %r is searching for %r>' % (self.firstName, self.searchingForName)

