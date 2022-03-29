from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_toilet = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    can_take_calls = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)


@app.route('/')
def home():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes)

@app.route('/<int:cafe_id>')
def cafe_page(cafe_id):
    cafe=Cafe.query.filter_by()
    return render_template("cafe.html", cafe=cafe)

if __name__ == "__main__":
    app.run(port=5000, debug=True)