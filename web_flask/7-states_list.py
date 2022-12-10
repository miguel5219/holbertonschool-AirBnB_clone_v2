#!/usr/bin/python3
""" start a Flask web application """

from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    obj = [a for a in storage.all(State).values()]
    return render_template("7-states_list.html", obj=obj)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
