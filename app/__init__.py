from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URI
db = SQLAlchemy(app)

from app import views, models