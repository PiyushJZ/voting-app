from flask import Flask, render_template, session, request, redirect, url_for
import pymongo
app = Flask(__name__)
app.secret_key = b'\x1f\xdc?\x8c\xcb\xcf8\xc6\xc7\xc2$\x04\x19\x1c+\xcd'

# Database
client = pymongo.MongoClient("mongodb+srv://piyush:1234@mycluster.vrmjm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["voting-db"]
users = db["users"]
candidates = db["candidates"]

# Routes
from user import routes

@app.route("/", methods=["GET", "POST"])
@app.route("/home/", methods=["GET", "POST"])
def home_page():
    return render_template("index.html")

@app.route("/user/", methods=["GET", "POST"])
def user_page():
    cand = []
    for each in candidates.find():
        cand.append(each["name"])
    return render_template("user.html", cand=cand)

@app.route("/admin/", methods=["GET", "POST"])
def admin_page():
    cand = {}
    for each in candidates.find():
        cand[each["name"]] = each["vote"]
    return render_template("admin.html", cand=cand)

