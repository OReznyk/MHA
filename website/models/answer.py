from ..extensions import db


class Answer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    answer = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '{self.question}', '{self.type}',  '{self.optional_answers}',  '{self.weight}'
