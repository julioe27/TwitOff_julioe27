# TwitOff_julioe27

## Setup a database

``````
set FLASK_APP=web_app
flask db init # only need to do it once
flask db migrate
flask db upgrade
``````

## Usage

`````# Mac:
FLASK_APP=hello.py flask run
`````
# Windows:

``````
set FLASK_APP=hello.py # one-time thing, to set the env var
flask run
``````