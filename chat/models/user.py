from datetime import datetime

from chat.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.String(255), nullable=False, default="")
    name = db.Column(db.String(255), nullable=True, default="")
    # ask_now = db.Column(db.Boolean, nullable=True, default=1)
    # visit_time = db.Column(db.DateTime, nullable=True, default=datetime.now)
    budget = db.Column(db.Integer, nullable=False, default=3)
    # here or station name
    # place = db.Column(db.String(255), nullable=False, default="here")
    prefer = db.Column(db.String(255), nullable=True, default="")

    createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return '<User {}:{}>'.format(self.id, self.user_id)
