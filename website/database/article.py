from website import db
from sqlalchemy.sql import func
from . import user

class Article(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"Article('{self.title}', '{self.author}', '{self.creation_date}')"
