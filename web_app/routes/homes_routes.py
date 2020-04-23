from flask import Flask

homes_routes = Blueprint("home_routes",__name__)

@homes_routes.route("/route")
def about():
    return "About Me"