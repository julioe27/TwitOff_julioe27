from flask import Flask

app = Flask(__name__)

@homes_routes.route("/") # registers the route and defines what should when someone visits this routes
def index():
    x = 2 + 2
    print("YOU VISTED THE HOMEPAGE")
    return f"Hello World! {x}"

@homes_routes.route("/route")
def about():
    return "About Me (TODO)"