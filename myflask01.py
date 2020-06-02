#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
   return "Hello World"

@app.route("/zach")
def hello_zach():
    return "Hello Zach"

@app.route("/carriesecret")
@app.route("/carrie")
def hello_carrie():
    #script goes here that goes and services MSCs
    return "Script compelted."

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(port=5006, debug=True) # DEBUG MODE    
