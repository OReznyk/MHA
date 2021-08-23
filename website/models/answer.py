from ..extensions import db
from sqlalchemy.sql import func
from . import question, response

class Answer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    answer = db.Column(db.String(250), nullable=False )
    response = db.Column(db.Integer, db.ForeignKey('response.id'))
    type = db.Column(db.String(50), nullable=False)
    question = db.Column(db.Integer, db.ForeignKey('question.id'))
    grade = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"Article('{self.question}', '{self.type}',  '{self.optional_answers}',  '{self.grade}')"
