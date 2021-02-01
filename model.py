from main import db
from datetime import date


class User(db.Model):  # notice that our class extends db.Model
 tablename__ = 'mtn users'  # this is the name we want the table in database to have.

    id=db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=False, nullable=False)
    othernames = db.Column(db.String(20), unique=False, nullable=True)
    DOB = db.Column(db.String(50), unique=True, nullable=False)
    nationality = db.Column(db.String(100), unique=False, nullable=False)

    # represent the object when it is queried for
    def __repr__(self):
        return '<Register {}>'.format(self.id)





