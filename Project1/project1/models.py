from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "USERS"
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
