from datetime import datetime

from chat.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    visit_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    budget = db.Column(db.String(255), nullable=False)
    place = db.Column(db.String(255), nullable=False)

    createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User {}:{}>'.format(self.id, self.name)
