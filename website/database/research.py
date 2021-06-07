from . import db
from sqlalchemy.sql import func

class Research(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    body = db.Column(db.String(15000))
    main_researchers = db.Column(db.Integer, db.ForeignKey('user.id'))
    assistants = db.Column(db.Integer, db.ForeignKey('user.id'))
    participants = db.Column(db.Integer, db.ForeignKey('user.id'))
    questions = db.relationship('Question')
    results = db.Column(db.String(15000)
    creation_date = db.Column(db.DateTime(timezone=true), default=func.now())



    def __init__(self, title, body, creator, creation_date, creation_month, creation_year, main_researcher, assistants, participants, questions, results):
              self.title = title
              self.body = body
              self.creation_date = creation_date
              self.main_researcher = main_researcher
              self.assistants = assistants
              self.participants = participants
              self.questions = questions
              self.results = results
