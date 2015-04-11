from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
import settings
import os

app = Flask(__name__)
#Check if the app is running on Heroku.If yes set the DATABASE URI Appropriately
if "DYNO" in os.environ:
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URI

db = SQLAlchemy(app)
cors = CORS(app)

from app import views, models