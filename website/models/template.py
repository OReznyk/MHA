from ..extensions import db
from sqlalchemy.sql import func


class Template(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))

    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    publishing_date = db.Column(db.DateTime(timezone=True))
    question = db.relationship('Question', backref='questions', lazy=True)
    #TODO: change content val
    content = db.Column(db.String(150), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '{self.title}', '{self.author}', '{self.creation_date}'
