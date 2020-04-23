# web_app/__init__.py

from flask import Flask
from web_app.models imprt db.migrate
from web_app.routes.admin_routes import admin_routes
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import  book_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.stats_routes import stats_routes

DATABASE_URI = "sqlite:///C:\Users\julio\Desktop\Lambda\TwitOff_julioe27\twitoff_development.db"
SECRET_KEY = "super secret"

def create_app():
    app=Flask(__name__)
    app.config["SECRET_KYE"] = SECRET_KEY

    app.config['SQLALCHEMY_DATABASSE_URI'] =DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migriate.init_app(app,db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)