import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# db.init_app(app)

from models import *

def main():
    db.create_all()
    db.session.commit()
    # load_data()

def load_data():
    f = open('books.csv')
    reader = csv.reader(f)
    count = 0
    for isbn, title, author, year in reader:
        count = count + 1
        # print(type(isbn), type(title), type(author), type(year))
        book = Books(isbn = isbn, title = title, author = author, year = year)
        db.session.add(book)
    print(count)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        load_data()
        # main()