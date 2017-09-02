"""Module containing Flask's MVC (Model View Controller) methods.

Created: 2017-09-02
Author: Andrew Dean
"""
from flask import Flask, render_template, redirect, url_for, flash
from flask import request, session
from werkzeug.security import check_password_hash


app = Flask(__name__)

app.secret_key = "my secret key >:)"    # Required for `session` variable to be used


@app.route("/")
def home():
    """Return the index page of the website."""
    return render_template("index.html")

USERNAME = "david"
PASSWORD_HASH = ("pbkdf2:sha256:50000$5IlJl0hD$d7de1b21471b85a7b6"
                 "efdd93bd5ee568309ab33c632648a9f58553208becdd6b")

@app.route("/login", methods=("GET", "POST"))
def login():
    """The login page of the website.

    A GET request will return the html for the login page.
    A POST request will attempt to login.
    """
    error = None
    if request.method == "POST":    # Try to log in
        username = request.form["username"].lower()
        password = request.form["password"]
        if username == USERNAME and check_password_hash(PASSWORD_HASH, password):
            session["logged_in"] = True
            flash("You were just logged in.")
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password. Please try again."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    """Log the user out."""
    session.pop("logged_in", None)  # Remove the "logged_in" key if it's there
    flash("You were just logged out.")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
