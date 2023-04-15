from app import app

from flask import render_template

# main route
@app.route("/")
def index():
    return render_template("public/index.html")

# about page route
@app.route("/about")
def about():
    return "<h1>About page<h1>"