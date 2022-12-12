#!/usr/bin/python3
""" Flask: rendering template """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import os

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ removes the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_route():
    """ displays a HTML page """
    states = [state for state in storage.all(State).values()]
    return render_template(
            '9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """ displays a HTML page """
    states = [state for state in storage.all(State).values()]
    list_ids = [state.id for state in storage.all(State).values()]
    cities = [city for city in list(storage.all(City).values())]
    return render_template(
        '9-states.html',
        cities=cities,
        states=states,
        id=id, list_ids=list_ids)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
