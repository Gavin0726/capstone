import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "capstone"
database_path = "postgres://{}@{}/{}" \
  .format('gavin', 'localhost: 5432', database_name)

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
Assign

'''


class Assign(db.Model):
    __tablename__ = 'assign'
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'),
                         primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'),
                         primary_key=True)
    movie = db.relationship("Movie", back_populates="assign_movie")
    actor = db.relationship("Actor", back_populates="assign_actor")

    def __init__(self, movie_id, actor_id):
        self.movie_id = movie_id
        self.actor_id = actor_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
          'movie_id': self.movie_id,
          'actor_id': self.actor_id,
        }


'''
Movie

'''


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    boxoffice = db.Column(db.String(120))
    assign_movie = db.relationship('Assign', back_populates="movie")

    def __init__(self, title, release_date, boxoffice):
        self.title = title
        self.release_date = release_date
        self.boxoffice = boxoffice

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
          'id': self.id,
          'question': self.title,
          'answer': self.release_date,
          'category': self.boxoffice,
        }


'''
Actor

'''


class Actor(db.Model):
    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.String(120))
    gender = db.Column(db.String(120))
    assign_actor = db.relationship('Assign', back_populates="actor")

    def __init__(self, name, age, gender):
        self.type = name
        self.type = age
        self.type = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
          'id': self.id,
          'name': self.name,
          'age': self.age,
          'gender': self.gender
        }
