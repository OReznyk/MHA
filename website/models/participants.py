"""from ..extensions import db
from sqlalchemy.orm import relationship, backref


class Participants(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    research_id = db.Column('research', db.ForeignKey('research.id'), primary_key=True)
    participant_id = db.Column('participant', db.ForeignKey('user.id'), primary_key=True)

    role = db.Column(db.Integer, db.ForeignKey('role.id'))
    responded = db.Column(db.Boolean(), default=False)
    invited = db.Column(db.Boolean(), default=False)

    #participants = db.relationship("User", backref=backref("participants", cascade="all, delete-orphan"))
    #research = db.relationship("Research", backref=backref("participants", cascade="all, delete-orphan"))

    def __repr__(self):
        return '{self.research_id}', '{self.participant_id}', '{self.role}', '{self.invited}', '{self.responded}'"""
