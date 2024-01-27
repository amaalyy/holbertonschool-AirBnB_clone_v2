#!/usr/bin/python3

"""script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_text(text):
    s = ""
    for i in text:
        s += i if i != "_" else " "
    return f"C {s}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, state="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, state="odd")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
