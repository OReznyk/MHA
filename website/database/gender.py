from website import db

class Gender(db.Model):
    _id = db.Column("id", db.Integer(), primary_key=True)
    gender = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f"Gender('{self.gender}')"
