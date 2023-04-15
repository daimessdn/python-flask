from app import app

# main route
@app.route("/")
def index():
    return "Hello, world"

# about page route
@app.route("/about")
def about():
    return "<h1>About page<h1>"