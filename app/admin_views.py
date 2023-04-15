from app import app

from flask import render_template

# main route
@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

# about page route
@app.route("/admin/profile")
def admin_profile():
    return "<h1>Admin profile<h1>"