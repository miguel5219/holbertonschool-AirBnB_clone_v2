#!/usr/bin/python3
""" Flask: rendering template """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
import os

app= Flask(__name__)


@app.teardown_appcontext
def teardow(exception):
    """ close the current SQLAlchemy session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states_route():
    """ display HTML page """
    _states = [state for state in storage.all(State).values()]
    _cities = [city for city in list(storage.all(City).values())]
    _amenities = [amenity for amenity in storage.all(Amenity).values()]
    return render_template(
            '10-hbnb_filters.html',
            _states=_states,
            _cities=_cities,
            _amenities=_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
