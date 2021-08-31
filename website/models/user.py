from ..extensions import db, login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func
#from sqlalchemy.orm import relationship
from . import participants


class User(db.Model, UserMixin):
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    email_verified = db.Column(db.Boolean(), default=False)

    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    birth_date = db.Column(db.Date(), default=func.now())
    gender = db.Column(db.Integer, db.ForeignKey('gender.id'))
    image = db.Column(db.String(20), nullable=False, default='profile-default.png')
    permission = db.Column(db.Integer, db.ForeignKey('permissions.id'))
    permission_confirmation = db.Column(db.Boolean(), default=False)

    #participant_at = db.relationship("Research", secondary=participants,  backref=db.backref("participants", lazy='dynamic'))
    #articles = db.relationship('Article', backref='author', lazy=True)

    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    active = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return '{self.email}', '{self.first_name}', '{self.second_name}', '{self.birth_date}', '{self.gender}', '{self.permission}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
