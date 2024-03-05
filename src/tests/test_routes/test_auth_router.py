import pytest
from http import HTTPStatus
from flask import url_for
from database import session
from database.orm import select
from database.models import User
from routes import auth_router


def test_url_for_register_page(flask_app) -> None:
    """
    Make sure that url for auth.register returns "/register/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)

    with flask_app.app_context(), flask_app.test_request_context():
        assert url_for("auth.register") == "/register/"


def test_can_get_register_page(flask_app) -> None:
    """
    Make sure that the register page can be fetched

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.app_context(), flask_app.test_request_context():
        response = test_client.get(url_for("auth.register"))
        assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures("set_temporary_database")
def test_can_register_user(flask_app) -> None:
    """
    Make sure that the /register/ route can successfully register a user

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.app_context(), flask_app.test_request_context():
        response = test_client.post(url_for("auth.register"), data={
            "username": "username",
            "email": "email@email.com",
            "password": "password",
            "password_confirmation": "password"
        })
        assert response.status_code == HTTPStatus.CREATED

        user = session.execute(select(User).where(User.email == "email@email.com")).scalar()
        assert user is not None


@pytest.mark.usefixtures("set_temporary_database")
def test_trying_to_register_user_twice_returns_bad_request(flask_app) -> None:
    """
    Make sure that the /register/ route returns a bad request status code when trying to register
    a user twice

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.app_context(), flask_app.test_request_context():
        test_client.post(url_for("auth.register"), data={
            "username": "username",
            "email": "email@email.com",
            "password": "password",
            "password_confirmation": "password"
        })
        response = test_client.post(url_for("auth.register"), data={
            "username": "username",
            "email": "email@email.com",
            "password": "password",
            "password_confirmation": "password"
        })

        assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.usefixtures("set_temporary_database")
def test_trying_to_register_with_invalid_password_confirmation_returns_bad_request(flask_app) -> None:
    """
    Make sure that the /register/ route returns a bad request status code when the password confirmation does not
    match the password

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.app_context(), flask_app.test_request_context():
        response = test_client.post(url_for("auth.register"), data={
            "username": "username",
            "email": "email@email.com",
            "password": "password",
            "password_confirmation": "some_other_password"
        })

        assert response.status_code == HTTPStatus.BAD_REQUEST


