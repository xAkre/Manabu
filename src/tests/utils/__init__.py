"""
This package contains utility functions for testing
"""

from multidict import MultiDict
from flask import Flask, url_for
from flask.testing import FlaskClient
from routes import general_router, auth_router


def form_data(dictionary: dict) -> MultiDict:
    """
    Returns a dictionary as a multi dict that can be used as form data

    :return: The dictionary passed as an argument as a multi dict
    """

    return MultiDict(dictionary)


def register_and_login(
    test_client: FlaskClient,
    flask_app: Flask | None = None,
    username: str = "username",
    email: str = "email@email.com",
    password: str = "Password_123",
) -> dict:
    """
    Register and login a user using the application's routes. This function registers the auth and general routers
    if a flask application is passed as an argument. Make sure this function is called inside a test request
    context so that calls to url_for can be resolved

    :param test_client: The test client to post the data to
    :param flask_app: The flask app to register the required blueprints on. Defaults to None
    :param username: The user's username. Defaults to "username"
    :param email: The user's email. Defaults to "email@email.com"
    :param password: The user's password. Defaults to "Password_123"
    :return: The user's data as a dictionary
    """
    if flask_app:
        flask_app.register_blueprint(auth_router)
        flask_app.register_blueprint(general_router)

    register_form_data = form_data(
        {
            "username": username,
            "email": email,
            "password": password,
            "password_confirmation": password,
        }
    )
    test_client.post(url_for("auth.register"), data=register_form_data)
    login_form_data = form_data({"username_or_email": username, "password": password})
    test_client.post(url_for("auth.login"), data=login_form_data)

    return {"username": username, "email": email, "password": password}
