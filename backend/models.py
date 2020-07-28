import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "bookshelf"
database_path = "postgres://{}:{}@{}/{}".format('student', 'student','localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
drop_db(app)
    binds a flask application and a SQLAlchemy service
'''
def drop_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.session.commit() 
    db.drop_all()

'''
Book

'''
class Book(db.Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    rating = Column(Integer)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def db_close():
        db.session.close()

    @staticmethod
    def count():
        return Book.query.count()

    def format(self):
        return {
          'id': self.id,
          'title': self.title,
          'author': self.author,
          'rating': self.rating,
    }

    def __str__(self):
        return str({
          'id': self.id,
          'title': self.title,
          'author': self.author,
          'rating': self.rating})