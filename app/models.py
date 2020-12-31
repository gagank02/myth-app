from app import db

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return '<Name {}>'.format(self.name)