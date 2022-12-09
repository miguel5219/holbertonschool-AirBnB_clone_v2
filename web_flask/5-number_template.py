#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from markupsafe import escape
from flask import render_template

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


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """ . """
    newText = text.replace('_', ' ')
    return 'Python {}'.format(escape(newText))


@app.route("/number/<int:n>", strict_slashes=False)
def number_Route(n):
    """ . """
    return '{} is a number'. format(n)


@app.router("/number_template/<int:n>", strict_slashes=False)
def numberTemplateRouter(n):
    """ . """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
