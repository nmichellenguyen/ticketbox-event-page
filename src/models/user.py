from src import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # email = some string
    # password_hash = some string 128 wide
    # events = db.relationship('Event', backref='event', lazy=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    events = db.relationship('Event', backref='user', lazy=True)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, email, password):
        self.email = email
        self.password_hash  = generate_password_hash(password)

    def __repr__(self):
        return f"{self.email}:{self.id}"