from ..extensions import db
from sqlalchemy.sql import func


class Research(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)
    template = db.Column(db.Integer, db.ForeignKey('template.id'))

    researchers = db.Column(db.Integer, db.ForeignKey('user.id'))
    #assistants = db.Column(db.Integer, db.ForeignKey('user.id'))
    #participants = db.Column(db.Integer, db.ForeignKey('user.id'))

    participants_answers = db.relationship('Response', backref='research_responses', lazy=True)

    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    publishing_date = db.Column(db.DateTime(timezone=True))

    in_progress = db.Column(db.Boolean(), default=False)
    closed = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return '{self.title}', '{self.researchers}',  '{self.assistants}', '{self.participants}',  '{self.template}', '{self.in_progress}', '{self.closed}'
