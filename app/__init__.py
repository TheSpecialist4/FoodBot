from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

#def create_app():
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodbot.db'
db.init_app(app)

migrate = Migrate(app, db)

from app import models
from app import routes

#    return app