from . import db
from sqlalchemy.sql import func

class Article(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creation_date = db.Column(db.DateTime(timezone=true), default=func.now())

  def __init__(self, title, body, author, creation_date):
          self.title = title
          self.body = body
          self.author = author
          self.creation_date = creation_date

    def __repr__(self):
        return f"Article('{self.title}', '{self.author}', '{self.creation_date}')"


db.create_all()
db.session.commit()
