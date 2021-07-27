from website import db
from sqlalchemy.sql import func
from . import question, answer, user, template, response

class Research(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)
    researchers = db.Column(db.Integer, db.ForeignKey('user.id'))
    #assistants = db.Column(db.Integer, db.ForeignKey('user.id'))
    template = db.Column(db.Integer, db.ForeignKey('template.id'))
    questions = db.relationship('Question', backref='author', lazy=True)
    participants_answers = db.relationship('Response', backref='research_responses', lazy=True)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())



    def __repr__(self):
        return f"Article('{self.title}', '{self.main_researchers}',  '{self.assistants}',  '{self.template}', '{self.creation_date}')"
