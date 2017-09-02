"""Module containing Flask's MVC (Model View Controller) methods.

Created: 2017-09-02
Author: Andrew Dean
"""
from flask import Flask, render_template, redirect, url_for
from werkzeug.security import check_password_hash


app = Flask(__name__)


@app.route("/")
def index():
    """Return the index page of the website."""
    return "index"


PASSWORD_HASH = ("pbkdf2:sha256:50000$5IlJl0hD$d7de1b21471b85a7b6"
                 "efdd93bd5ee568309ab33c632648a9f58553208becdd6b")

@app.route("/login", methods=("GET", "POST"))
def login():
    """The login page of the website.

    A GET request will return the html for the login page.
    A POST request will attempt to login.
    """
    error = None
    username = request.form["username"].lower()
    password = request.form["password"]
    if request.method == "POST":    # Try to log in
        if username == "daviddeanadmin" and check_password_hash(PASSWORD_HASH, password):
            return redirect(url_for("index"))
        else:
            error = "Invalid username or password. Please try again."

    return render_template("login.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)
