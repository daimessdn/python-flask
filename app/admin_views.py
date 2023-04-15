from app import app

# main route
@app.route("/admin/dashboard")
def index():
    return "<h1>Admin dashboard</h1>"

# about page route
@app.route("/admin/profile")
def about():
    return "<h1>Admin profile<h1>"