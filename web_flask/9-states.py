#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import os

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_route():
    """ displa HTML page """
    _states = [state for state in storage.all(State).values()]
    return render_template("9-states.html", _states=_states)


@app.route('/states/<id>', strict_slashes=False)
def states_route_id(id):
    """ display HTML page """
    _states = [state for state in storage.all(State).values()]
    list_ids = [state.id for state in storage.all(State).values()]
    _cities = [city for city in list(storage.all(City).values())]
    return render_template("9-states.html",
                           _cities=_cities,
                           _states=_states,
                           id=id, list_ids=list_ids)


@app.teardown_appcontext
def teardown_db(exception):
    """ close the current SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
