from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    middle_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    zipcode = db.Column(db.String())
    city = db.Column(db.String(), nullable=True)
    country = db.Column(db.String(), nullable=True)
    state = db.Column(db.String(), nullable=True)

    def __init__(self, first_name, middle_name, last_name, email, zipcode, city=None, country=None, state=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.zipcode = zipcode
        self.city = city
        self.country = country
        self.state = state

    def __repr__(self):
        return '<id {}>'.format(self.id)
