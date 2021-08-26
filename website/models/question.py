from ..extensions import db


class Question(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    question = db.Column(db.String(250), nullable=False )
    research = db.Column(db.Integer, db.ForeignKey('research.id'))
    type = db.Column(db.String(50), nullable=False)
    optional_answers = db.relationship('Answer', backref='questioner', lazy=True)
    grade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Article('{self.question}', '{self.type}',  '{self.research}', '{self.optional_answers}',  '{self.grade}')"
