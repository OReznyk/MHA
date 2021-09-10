from ..extensions import db


class Role(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True)
    role = db.Column(db.String(50), unique=True)
    participant = db.relationship('Participants', backref='role', lazy=True)

    def __repr__(self):
        return self.role
