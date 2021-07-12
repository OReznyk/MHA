from . import db
from sqlalchemy.sql import func

class Research(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)
    main_researchers = db.Column(db.Integer, db.ForeignKey('user.id'))
    assistants = db.Column(db.Integer, db.ForeignKey('user.id'))
    participants = db.Column(db.Integer, db.ForeignKey('user.id'))
    template = db.Column(db.Integer, db.ForeignKey('template.id'))
    questions = db.relationship('question', backref='author', lazy=True)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())



    def __repr__(self):
        return f"Article('{self.title}', '{self.main_researchers}',  '{self.assistants}',  '{self.template}', '{self.creation_date}')"
