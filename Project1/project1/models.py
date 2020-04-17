from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "USERS"
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    address = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
