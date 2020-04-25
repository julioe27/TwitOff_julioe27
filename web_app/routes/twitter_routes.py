# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify #, render_template, request, flash, redirect

from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import api as twitter_api
from web_app.services.basilica_service import connection as basilica_connection

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data():
    print("FETCHING...", screen_nmae)

    user = twitter_api.get_user(screen_name)

    db_user = User.query.get(user.id) or User(id.user.id)
    db_user.screen_name = user.screen_name
    db_user.name = user.name
    db_user.location = user.location
    db_user.follower_count = user.followers_count
    db.session.add(db_user)
    db.session.commit()

    statues = twitter_api.user_timeline(screen_name, tweet_mode="extended",count=150)
    print("STATUES", len(statues))

    tweet_texts = [status.full_text for status in statues]
    embeddings = list(basilica_connection.embed_sentences(tweet_texts, model='twitter'))
    print("EMBEDDINGS", len(embeddings))

    for index, status in enumerate(statues):
        print(status.full_text)
        print("-------")
        db_tweet = Tweet.query.get(status.id) or Tweet(id=staus.id)
        db_tweet.user_id = status.author.id
        db_tweet.user_id = status.full_text
        embedding = embeddings[index]
        print(len(embedding))
        db_tweet.embedding = embedding
        db.session.add(db_tweet)

    db.session.commit()

    return f" FETCHED {screen_name} OK"


