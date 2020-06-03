#!/usr/bin/python3

from flask import Flask
from flask import render_template
# and anything else you want to pull in!
from flask import request

app = Flask(__name__)

# index
@app.route("/")
def homeindex():
    return "Welcome to my API! Services are available at... /traffic... /reviews... /netconfig... so on.."



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
