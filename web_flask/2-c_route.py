#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ func to display 'Hello HBNB!. """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ func to display 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_route(text):
    """ display “C ” followed by the value of the text variable """
    newText = text.replace('_', ' ')
    return 'C {}'.format(escape(newText))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
