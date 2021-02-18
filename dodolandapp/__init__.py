from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from dodolandapp.db import db
from dodolandapp.resources.metadata import metadata

# INITIALISE APP
app = Flask(__name__)
api = Api(app)

# CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dodoland.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
db.init_app(app)  # instantiating db object...

# CREATE DATABASE
with app.app_context():
    db.create_all()

# ADD ENDPOINT TO API
api.add_resource(metadata, "/metadata/<int:gene>")
