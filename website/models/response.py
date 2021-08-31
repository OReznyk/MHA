from ..extensions import db
from sqlalchemy.sql import func


class Response(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    answer = db.Column(db.Integer, db.ForeignKey('answer.id'))
    question = db.Column(db.Integer, db.ForeignKey('question.id'))
    answerer = db.Column(db.Integer, db.ForeignKey('user.id'))
    finished = db.Column(db.Boolean, nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    finished_date = db.Column(db.DateTime(timezone=True))

    def __repr__(self):
        return f"Response('{self.answer}', '{self.research}',  '{self.answerer}',  '{self.finished}',  '{self.creation_date}',  '{self.finished_date}')"
