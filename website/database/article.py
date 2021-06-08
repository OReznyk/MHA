from . import db
from sqlalchemy.sql import func

class Article(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    body = db.Column(db.String(25000))
    creator = db.Column(db.Integer, db.ForeignKey('user.id'))
    creation_date = db.Column(db.DateTime(timezone=true), default=func.now())

  def __init__(self, title, body, creator, creation_date):
          self.title = title
          self.body = body
          self.creator = creator
          self.creation_date = creation_date
