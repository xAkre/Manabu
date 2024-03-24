import pytest
from http import HTTPStatus
from flask import Flask, url_for
from flask.testing import FlaskClient
from database import session as d_session
from database.orm import select
from database.models import User
from routes import categories_router, auth_router, general_router
from tests.utils import form_data


def test_url_for_add_category_page(flask_app) -> None:
    """
    Make sure that url for categories.create returns "/categories/create/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)

    with flask_app.test_request_context():
        assert url_for("categories.create") == "/categories/create/"


@pytest.mark.usefixtures("set_temporary_database")
def test_can_get_add_category_page(flask_app) -> None:
    """
    Make sure that the add category page can be fetched

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        _register_and_login_test_user(flask_app, test_client)
        response = test_client.get(url_for("categories.create"))
        assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures("set_temporary_database")
def test_can_add_category(flask_app) -> None:
    """
    Make sure that the add category route can successfully add a category

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        _register_and_login_test_user(flask_app, test_client)
        data = form_data({"name": "work", "color": "#FFFFFF"})
        response = test_client.post(url_for("categories.create"), data=data)
        assert response.status_code == HTTPStatus.CREATED

        user = d_session.execute(
            select(User).where(User.email == "email@email.com")
        ).scalar()
        assert len(user.categories) == 1


@pytest.mark.usefixtures("set_temporary_database")
def test_cant_add_category_with_invalid_color(flask_app) -> None:
    """
    Make sure that the add category route does not add categories with invalid colors

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        _register_and_login_test_user(
            flask_app,
            test_client,
        )
        data = form_data({"name": "work", "color": "#FFFFF"})
        response = test_client.post(url_for("categories.create"), data=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST

        user = d_session.execute(
            select(User).where(User.email == "email@email.com")
        ).scalar()
        assert len(user.categories) == 0


def test_url_for_show_categories(flask_app) -> None:
    """
    Make sure that url for categories.show returns "/categories/"
    """
    flask_app.register_blueprint(categories_router)

    with flask_app.test_request_context():
        assert url_for("categories.show") == "/categories/"


@pytest.mark.usefixtures("set_temporary_database")
def test_can_show_categories(flask_app) -> None:
    """
    Make sure that the show categories route can successfully show the users categories

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        _register_and_login_test_user(flask_app, test_client)
        data = form_data({"name": "work", "color": "#FFFFFF"})
        test_client.post(url_for("categories.create"), data=data)
        response = test_client.get(url_for("categories.show"))
        assert response.status_code == HTTPStatus.OK


def _register_and_login_test_user(flask_app: Flask, test_client: FlaskClient) -> None:
    """
    Register and login a user with the following fields:

    - username: username
    - email: email@email.com
    - password: Password_123

    This function registers the auth and general routers. Make sure that this function is called inside a
    test request context so that calls to url for can be resolved

    :param flask_app: The flask app to register the blueprints on
    :param test_client: The flask test client to send the data to
    """
    if not flask_app.blueprints.get("auth"):
        flask_app.register_blueprint(auth_router)
    if not flask_app.blueprints.get("general"):
        flask_app.register_blueprint(general_router)

    register_form_data = form_data(
        {
            "username": "username",
            "email": "email@email.com",
            "password": "Password_123",
            "password_confirmation": "Password_123",
        }
    )
    test_client.post(url_for("auth.register"), data=register_form_data)
    login_form_data = form_data(
        {"username_or_email": "username", "password": "Password_123"}
    )
    test_client.post(url_for("auth.login"), data=login_form_data)
