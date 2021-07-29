from website import db
from sqlalchemy.sql import func
from . import answer, user, research

class Response(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    answers = db.relationship('Answer', backref='response_answers', lazy=True)
    research = db.Column(db.Integer, db.ForeignKey('research.id'))
    aswerer = db.Column(db.Integer, db.ForeignKey('user.id'))
    finished = db.Column(db.Boolean, nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    finished_date = db.Column(db.DateTime(timezone=True))


    def __repr__(self):
        return f"Response('{self.answers}', '{self.research}',  '{self.answerer}',  '{self.finished}',  '{self.creation_date}',  '{self.finished_date}')"
