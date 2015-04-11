from app import db, app
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy, BaseQuery


#Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    searchingForName = db.Column(db.String(120))
    message = db.Column(db.Text)
    phoneNumber = db.Column(db.String(30), default="0000000")

    def __init__(self, name , searchingForName, message, phoneNumber):
        self.name = name 
        self.searchingForName = searchingForName
        self.message = message
        self.phoneNumber = phoneNumber

    def __repr__(self):
        return '<User %r is searching for %r>' % (self.name , self.searchingForName)

