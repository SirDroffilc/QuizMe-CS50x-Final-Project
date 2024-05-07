from .app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    quizzes = db.relationship('Quiz')

class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    instructions = db.Column(db.String(1000))
    total_items = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    items = db.relationship('Item')


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(2000), nullable=False)
    answer = db.Column(db.String(50), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))


