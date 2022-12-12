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
    states_ob = [s for s in storage.all(State).values()]
    return render_template("9-states.html", states_ob=states_ob)


@app.route('/states/<id>', strict_slashes=False)
def states_route_id(id):
    """ display HTML page """
    states_ob = [s for s in storage.all(State).values()]
    states_ids = [s.id for s in storage.all(State).values()]
    cities_ob = [c for c in list(storage.all(City).values())]
    return render_template("9-states.html",
                           cities_ob=cities_ob,
                           states_ob=states_ob,
                           id=id, states_ids=states_ids)


@app.teardown_appcontext
def teardown_db(exception):
    """ close the current SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
