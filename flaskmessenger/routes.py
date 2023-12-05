from flask import render_template, url_for
from flaskmessenger import app, db


@app.route("/")
def base():
    return render_template('base.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')