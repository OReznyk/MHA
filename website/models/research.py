from ..extensions import db
from sqlalchemy.sql import func


class Research(db.Model):
    d = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)

    #participant = db.relationship('User', secondary='participants', backref='researches', lazy='select')

    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    publishing_date = db.Column(db.DateTime(timezone=True), onupdate=db.func.current_timestamp())
    #published_by = db.relationship("User", backref='published_researches', lazy=True)
    #last_changed_by = db.relationship("User", backref='changed_researches', lazy=True, onupdate=current_user)

    approved = db.Column(db.Boolean(), default=False)
    closed = db.Column(db.Boolean(), default=False)
    summary = db.Column(db.Text)

    #
    questioner = db.relationship('Questioner', backref=db.backref('research', lazy='joined'), lazy=True)

    def __repr__(self):
        return '{self.title}', '{self.researchers}',  '{self.assistants}',  '{self.template}', '{self.in_progress}', '{self.closed}'
