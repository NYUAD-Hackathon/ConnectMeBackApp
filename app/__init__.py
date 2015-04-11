from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URI
db = SQLAlchemy(app)
cors = CORS(app)

from app import views, models