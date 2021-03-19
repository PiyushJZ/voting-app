from flask import Flask
from app import app
from user.models import User

@app.route("/logout/<data>")
def logout(data):
    return User().logout(data)

@app.route("/login/user/", methods=["GET", "POST"])
def login():
    return User().login()

@app.route("/login/admin/", methods=["GET", "POST"])
def admin_login():
    return User().admin_login()
