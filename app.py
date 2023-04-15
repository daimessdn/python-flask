from flask import Flask

app = Flask(__name__)

# main route
@app.route("/")
def index():
    return "Hello, world"

# about page route
@app.route("/about")
def about():
    return "<h1>About page<h1>"

if (__name__ == "__main__"):
    app.run(debug=True)