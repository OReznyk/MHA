from ..extensions import db
from sqlalchemy.sql import func


class Research(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)
    #template = db.Column(db.Integer, db.ForeignKey('template.id'))

    #participants = relationship("User", secondary=participants)

    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    publishing_date = db.Column(db.DateTime(timezone=True))
    #published_by = db.relationship("User", backref='published_researches', lazy=True)
    #last_changed_by = db.relationship("User", backref='changed_researches', lazy=True)

    approved = db.Column(db.Boolean(), default=False)
    closed = db.Column(db.Boolean(), default=False)
    summary = db.Column(db.Text)

    def __repr__(self):
        return '{self.title}', '{self.researchers}',  '{self.assistants}',  '{self.template}', '{self.in_progress}', '{self.closed}'
