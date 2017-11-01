''' Simple web server to run our map application for Project 5.
    General structure of app.py influenced by passt projects, and as a result,
    they were heavily referenced. 
'''

import flask
import config
import logging
import os
import sys


app = flask.Flask(__name__)
CONFIG = config.cfg_dict
# Set secret key so that session variable is available
app.secret_key = CONFIG["SECRET_KEY"]


@app.route("/")
@app.route("/index")
def index():
    poi_handler()
    # Reference: Information on render_template and its use with Jinja from docs
    # http://flask.pocoo.org/docs/0.12/quickstart/
    return flask.render_template("index.html", poi = flask.session["poi"])


@app.errorhandler
def page_not_found():
    return flask.render_template("404.html")

### POI Reading ###
def poi_handler():
    flask.session["poi"] = []
    # Reference for how to access current location:
    # https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-a-python-script
    with open(os.path.join(sys.path[0], "POI.txt")) as f:
        n = int(f.readline().strip())
        for i in range(n):
            line = f.readline().strip().split()
            flask.session["poi"].append(line)
        print(flask.session['poi'])


if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG["PORT"]))
    app.run(port=CONFIG["PORT"], host="0.0.0.0")