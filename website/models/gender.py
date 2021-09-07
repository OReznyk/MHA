from ..extensions import db


class Gender(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True)
    gender = db.Column(db.String(50), unique=True)
    users = db.relationship('User', backref='gender', lazy=True)

    def __repr__(self):
        return "{self.gender}"
