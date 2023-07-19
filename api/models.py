from app import db
from sqlalchemy import Enum


class Language(Enum):
    en = 1
    es = 2


class PrivacyLevel(Enum):
    public = 1
    private = 2
    shared = 3


class NameCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    language = db.Column(db.Enum, nullable=False, default=Language.en)
    """
    v1/v2:
    pronounciation: string
    origin: string
    themes: string[]
    meaning: string
    ^^ or would just be NLP Vectors?
    syllables: number
    alternate spellings: namecard.id[]
    nicknames: namecard.id[]
    gender: number (spectrum of 1-10)
    """


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    # V1/2
    privacy = db.Column(db.Enum, default=PrivacyLevel.public)
    owner = db.relationship('User', back_populates='list')


class User(db.Model, db.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    lists = db.relationship('List', back_populates='user',
                            cascade='all, delete-orphan')


"""
TODO: Create login form, handle logins
@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)
"""
