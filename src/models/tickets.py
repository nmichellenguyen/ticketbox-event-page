from src import db
from datetime import datetime




class Tickets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    