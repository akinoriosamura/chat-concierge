from datetime import datetime

from chat.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False, default="concieru")
    ask_now = db.Column(db.Boolean, nullable=False, default=1)
    visit_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    budget = db.Column(db.Integer, nullable=False, default=1000)
    # here or station name
    place = db.Column(db.String(255), nullable=False, default="here")
    mail = db.Column(db.String(255), nullable=False, default="")
    inquiry = db.Column(db.String(255), nullable=False, default="")

    createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User {}:{}>'.format(self.id, self.name)
