from src import db
from datetime import datetime


from werkzeug.security import generate_password_hash


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.String(128), unique=True, nullable=False)
    venue_id = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.Date, nullable=False)
    end_time = db.Column(db.Date, nullable=False)

    # def __init__(self, user_id, description, venue_id, organizer_id, start_time, end_time):

    #     self.user_id = user_id
    #     self.description = description
    #     self.venue_id = venue_id
    #     self.organizer_id = organizer_id
    #     self.start_time = start_time
    #     self.end_time = end_time
