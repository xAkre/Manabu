import pytest
from http import HTTPStatus
from flask import url_for, session as f_session
from database import session as d_session
from database.orm import select
from database.models import User
from routes import auth_router, general_router


def test_url_for_register_page(flask_app) -> None:
    """
    Make sure that url for auth.register returns "/register/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)

    with flask_app.test_request_context():
        assert url_for("auth.register") == "/register/"


def test_can_get_register_page(flask_app) -> None:
    """
    Make sure that the register page can be fetched

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
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

    with flask_app.test_request_context():
        response = test_client.post(
            url_for("auth.register"),
            data={
                "username": "username",
                "email": "email@email.com",
                "password": "Password_123",
                "password_confirmation": "Password_123",
            },
            follow_redirects=True,
        )
        assert response.status_code == HTTPStatus.OK
        assert response.request.path == url_for("auth.login")

        user = d_session.execute(
            select(User).where(User.email == "email@email.com")
        ).scalar()
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

    with flask_app.test_request_context():
        test_client.post(
            url_for("auth.register"),
            data={
                "username": "username",
                "email": "email@email.com",
                "password": "Password_123",
                "password_confirmation": "Password_123",
            },
        )
        response = test_client.post(
            url_for("auth.register"),
            data={
                "username": "username",
                "email": "email@email.com",
                "password": "Password_123",
                "password_confirmation": "Password_123",
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.usefixtures("set_temporary_database")
def test_trying_to_register_with_invalid_password_confirmation_returns_bad_request(
    flask_app,
) -> None:
    """
    Make sure that the /register/ route returns a bad request status code when the password confirmation does not
    match the password

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        response = test_client.post(
            url_for("auth.register"),
            data={
                "username": "username",
                "email": "email@email.com",
                "password": "Password_123",
                "password_confirmation": "Password_1234",
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST


def test_url_for_login_page(flask_app) -> None:
    """
    Make sure that url for auth.login returns "/login/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)

    with flask_app.test_request_context():
        assert url_for("auth.login") == "/login/"


def test_can_get_login_page(flask_app) -> None:
    """
    Make sure that the login page can be fetched

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        response = test_client.get(url_for("auth.login"))
        assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures("set_temporary_database")
def test_can_log_in_with_username(flask_app) -> None:
    """
    Make sure that the /login/ route can successfully log a user in with their username

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(general_router)
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context(), test_client:
        test_client.post(
            url_for("auth.register"),
            data={
                "username": "username",
                "email": "email@email.com",
                "password": "Password_123",
                "password_confirmation": "Password_123",
            },
        )
        response = test_client.post(
            url_for("auth.login"),
            data={"username_or_email": "username", "password": "Password_123"},
            follow_redirects=True,
        )
        user = d_session.execute(
            select(User).where(User.username == "username")
        ).scalar()

        assert response.status_code == HTTPStatus.OK
        assert response.request.path == url_for("general.dashboard")
        assert user is not None
        assert f_session.get("user") == user


@pytest.mark.usefixtures("set_temporary_database")
def test_can_log_in_with_email(flask_app) -> None:
    """
    Make sure that the /login/ route can successfully log a user in with their email

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(general_router)
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context(), test_client:
        test_client.post(
            url_for("auth.register"),
            data={
                "username": "username",
                "email": "email@email.com",
                "password": "Password_123",
                "password_confirmation": "Password_123",
            },
        )
        response = test_client.post(
            url_for("auth.login"),
            data={"username_or_email": "email@email.com", "password": "Password_123"},
            follow_redirects=True,
        )
        user = d_session.execute(
            select(User).where(User.email == "email@email.com")
        ).scalar()

        assert response.status_code == HTTPStatus.OK
        assert response.request.path == url_for("general.dashboard")
        assert user is not None
        assert f_session.get("user") == user


@pytest.mark.usefixtures("set_temporary_database")
def test_cannot_log_in_with_a_username_or_email_that_does_not_exist(flask_app) -> None:
    """
    Make sure that you cannot log in with a username or email that does not exist

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        response = test_client.post(
            url_for("auth.login"),
            data={"username_or_email": "does_not_exist", "password": "Password_123"},
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.usefixtures("set_temporary_database")
def test_cannot_log_in_with_a_correct_username_but_incorrect_password(
    flask_app,
) -> None:
    """
    Make sure that you cannot log in with a password that doesn't match the username

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        test_client.post(
            url_for("auth.register"),
            data={
                "username": "username",
                "email": "email@email.com",
                "password": "Password_123",
                "password_confirmation": "Password_123",
            },
        )
        response = test_client.post(
            url_for("auth.login"),
            data={"username_or_email": "Password_123", "password": "Password_1234"},
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.usefixtures("set_temporary_database")
def test_cannot_log_in_with_a_correct_email_but_incorrect_password(
    flask_app,
) -> None:
    """
    Make sure that you cannot log in with a password that doesn't match the email

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        test_client.post(
            url_for("auth.register"),
            data={
                "username": "username",
                "email": "email@email.com",
                "password": "Password_123",
                "password_confirmation": "Password_123",
            },
        )
        response = test_client.post(
            url_for("auth.login"),
            data={
                "username_or_email": "email@email.com",
                "password": "Password_1234",
            },
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST


def test_url_for_logout_page(flask_app) -> None:
    """
    Make sure that url for auth.logout returns "/logout/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)

    with flask_app.test_request_context():
        assert url_for("auth.logout") == "/logout/"


@pytest.mark.usefixtures("set_temporary_database")
def test_can_log_out(flask_app) -> None:
    """
    Make sure that the /logout/ route can successfully log a user out

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(general_router)
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context(), test_client:
        test_client.post(
            url_for("auth.register"),
            data={
                "username": "username",
                "email": "email@email.com",
                "password": "Password_123",
                "password_confirmation": "Password_123",
            },
        )
        test_client.post(
            url_for("auth.login"),
            data={
                "username_or_email": "email@email.com",
                "password": "Password_123",
            },
        )
        response = test_client.get(url_for("auth.logout"), follow_redirects=True)

        assert response.status_code == HTTPStatus.OK
        assert response.request.path == url_for("general.landing_page")
        assert f_session.get("user") is None
