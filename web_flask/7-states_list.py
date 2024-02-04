#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage"""
    from models import storage

    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    from models import storage

    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
