# web_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, flash, redirect
from dotenv import load_dotenv
from web_app.models import db
import os

load_dotenv()

admin_routes = Blueprint("admin_routes", __name__)

API_KEY = os.getenv('API_KEY')

# GET /admin/db/reset?api_key=abc123
@admin_routes.route("/admin/db/reset")
def reset_db():
    print("URL PARMS", dict(request.args))
    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
        print(type(db))
        db.drop_all()
        db.create_all()
        print("PERMISSION GRANTED")
        return jsonify({"message": "DB RESET OK"})
    else:
        print("PERMISSION DENIED")
        flash("OOPS Permission Denied", "danger")
        return redirect("/")