"""Module containing Flask's MVC (Model View Controller) methods.

Created: 2017-09-02
Author: Andrew Dean
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """Return the index page of the website."""
    return "index"


if __name__ == "__main__":
    app.run(debug=True)
