"""Unit tests for the /login route.

Created: 2017-09-03
Author: Andrew Dean
"""
from spec.helper import *
from spec import credentials


with description("/login"):

    with it("should return a 200 OK"):
        test_app = app.test_client()
        response = test_app.get("/login", content_type="text/html")
        expect(response.status_code).to(equal(status_codes.OK))

    with it("should contain text asking the user to log in"):
        test_app = app.test_client()
        response = test_app.get("/login", content_type="text/html").data.decode()
        expect(response).to(contain("Please enter your credentials to login"))

    with it("should log the user in and redirect them when given valid credentials"):
        test_app = app.test_client()
        data = {"username": credentials.USERNAME, "password": credentials.PASSWORD}
        response = test_app.post("/login", data=data, follow_redirects=True).data.decode()
        expect(response).to(contain("Welcome to the home page!"))

    with it("should show an error message and not redirect when given invalid credentials"):
        test_app = app.test_client()
        data = {"username": "n0t4v4l1du53n4m3", "password": "0rp4$$w0rd"}
        response = test_app.post("/login", data=data, follow_redirects=True).data.decode()
        expect(response).to(contain("Invalid credentials. Please try again."))
        expect(response).to(contain("Please enter your credentials to login"))
