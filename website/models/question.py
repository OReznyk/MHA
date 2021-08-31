from ..extensions import db


class Question(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    question = db.Column(db.String(250), nullable=False)
    template = db.Column(db.Integer, db.ForeignKey('template.id'))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    research = db.Column(db.Integer, db.ForeignKey('research.id'))
    type = db.Column(db.String(50), nullable=False)
    optional_answers = db.relationship('Answer', backref='answers', lazy=True)
    response = db.relationship('Response', backref='response', lazy=True)
    weight = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '{self.question}', '{self.type}',  '{self.research}', '{self.author}', '{self.optional_answers}',   '{self.response}',  '{self.weight}'
