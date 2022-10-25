from flask import jsonify, request, Flask
# Python SQLite3 module is used to integrate the SQLite database with Python.
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
# This library adds Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application
from flask_sqlalchemy import SQLAlchemy
# SQLAlchemy is a library that facilitates the communication between Python programs and databases.
from sqlalchemy import event
from sqlalchemy.engine import Engine


application = Flask(__name__)

# database configuration
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0


# Allowing to configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

# creating instance of the database by passing app into SQLAlchemy class
# This class is used to control the SQL alchemy integration to one or more flask applications
# connecting ORM with flask application
db = SQLAlchemy(application)
# this is used to update date values while updating tables
current_time = datetime.now()

# class User represents a table in the database
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    # this is a foreign key with another table "BlogPost"
    posts = db.relationship("BlogPost", cascade="all, delete")

# class BlogPost represents a table in the database
class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    # this is a foreign key with another table "User"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)