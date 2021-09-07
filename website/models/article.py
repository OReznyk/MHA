from ..extensions import db
from sqlalchemy.sql import func


class Article(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)
    #author_id = db.relationship('User', backref='article', lazy=True)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return '{self.title}', '{self.author}', '{self.creation_date}'
