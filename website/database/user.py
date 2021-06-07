from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    _id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    first_name  = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    birth_date = db.Column(db.DateField())
    creation_date = db.Column(db.DateField())
    permissions  = db.Column(db.Integer, db.ForeignKey('permission.id'))
    researches = db.relationship('Research')

    def __init__(self, email, first_name, second_name, birth_date, permissions, password,
                        researches, creation_date):
        self.email = email
        self.first_name = first_name
        self.second_name = second_name
        self.birth_date = birth_date
        self.permissions = permissions
        self.password = password
        self.researches = researches
        self.creation_date = creation_date
