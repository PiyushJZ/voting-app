from flask import Flask, jsonify, session, request
from app import users, candidates
import uuid

class User:
    
    def start_session(self, user):
        del user["password"]
        session["logged_in"] = True
        session["user"] = user
        return jsonify("user"), 201
    
    def login(self):
        user = users.find_one({
            "email": request.form.get("email")
        })
        if user and request.form.get("password") == user["password"]:
            return self.start_session(user)
        return jsonify({"error": "Invalid Login Credentials"}), 401

    def admin_login(self):
        user = users.find_one({
            "email": request.form.get("email")
        })
        if user and request.form.get("password") == user["password"] and user["admin"]:
            return self.start_session(user)
        return jsonify({"error": "Invalid Login Credentials"}), 401

    def logout(self, data):
        if not data:
            return jsonify({"error": "Voting Failed"}), 401

        candidate = candidates.find_one({
            "name": data
        })
        votes = candidate["vote"] + 1
        candidates.find_one_and_update(
            {candidate["name"]},
            {'$set': {"vote": votes}}
            )
        session.clear()
        return redirect("/")