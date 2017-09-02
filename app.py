"""Module containing Flask's MVC (Model View Controller) methods.

Created: 2017-09-02
Author: Andrew Dean
"""
from functools import wraps

from flask import Flask, render_template, redirect, url_for, flash
from flask import request, session
from werkzeug.security import check_password_hash


app = Flask(__name__)

app.secret_key = "my secret key >:)"    # Required for `session` variable to be used


def logged_in() -> bool:
    """Return whether or not the user is logged in."""
    return "logged_in" in session


def login_required(function):
    """Decorator which only allows logged in users to access the route it decorates."""
    @wraps(function)
    def wrap(*args, **kwargs):
        if logged_in():
            return function(*args, **kwargs)
        else:
            flash("You need to log in first.")
            return redirect(url_for("login"))
    return wrap


USERNAME = "david"
PASSWORD_HASH = ("pbkdf2:sha256:50000$5IlJl0hD$d7de1b21471b85a7b6"
                 "efdd93bd5ee568309ab33c632648a9f58553208becdd6b")

@app.route("/login", methods=("GET", "POST"))
def login():
    """The login page of the website.

    A GET request will return the html for the login page.
    A POST request will attempt to login.
    """
    if logged_in():
        # Don't let logged in users log in again.
        return redirect(url_for("home"))

    error = None
    if request.method == "POST":    # Try to log in
        username = request.form["username"].lower()
        password = request.form["password"]
        if username == USERNAME and check_password_hash(PASSWORD_HASH, password):
            session["logged_in"] = True
            flash("You were just logged in.")
            return redirect(url_for("home"))
        else:
            error = "Invalid credentials. Please try again."

    return render_template("login.html", error=error)


@app.route("/logout")
@login_required
def logout():
    """Log the user out."""
    del session["logged_in"]
    flash("You were just logged out.")
    return redirect(url_for("login"))


@app.route("/")
@login_required
def home():
    """Return the index page of the website."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
