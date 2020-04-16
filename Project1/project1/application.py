import os
from dotenv import load_dotenv
from models import *

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))
db.init_app(app)
# db = SQLAlchemy(app)

def main():
    db.create_all()

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("registration.html")
    
    elif request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"name is {name}")
        print(f"username is {username}")
        print(f"password is {password}")
        return f"Welcome {name}"

if __name__ == "__main__":
    with app.app_context():
        main()