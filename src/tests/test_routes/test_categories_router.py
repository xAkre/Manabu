import pytest
from uuid import uuid4
from http import HTTPStatus
from flask import url_for
from database import session as d_session
from database.orm import select
from database.models import User, Category
from routes import categories_router, todos_router
from tests.utils import form_data, register_and_login


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
    flask_app.register_blueprint(todos_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        response = test_client.get(url_for("categories.create"))
        assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures("set_temporary_database")
def test_can_add_category(flask_app) -> None:
    """
    Make sure that the add category route can successfully add a category

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)
    flask_app.register_blueprint(todos_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        data = form_data({"name": "work", "color": "#FFFFFF"})
        response = test_client.post(
            url_for("categories.create"), data=data, follow_redirects=True
        )
        assert response.status_code == HTTPStatus.OK
        assert response.request.path == url_for("categories.show")

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
    flask_app.register_blueprint(todos_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
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
    flask_app.register_blueprint(todos_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        data = form_data({"name": "work", "color": "#FFFFFF"})
        test_client.post(url_for("categories.create"), data=data)
        response = test_client.get(url_for("categories.show"))
        assert response.status_code == HTTPStatus.OK


def test_url_for_delete_category_route(flask_app) -> None:
    """
    Make sure that url for categories.delete returns "/categories/<category_id>/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)
    uuid = "a" * 32

    with flask_app.test_request_context():
        assert (
            url_for("categories.delete", category_uuid=uuid) == f"/categories/{uuid}/"
        )


@pytest.mark.usefixtures("set_temporary_database")
def test_can_delete_category(flask_app) -> None:
    """
    Make sure that the category route can successfully delete a category

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        category_data = form_data({"name": "work", "color": "#FFFFFF"})
        test_client.post(url_for("categories.create"), data=category_data)

        category = d_session.execute(
            select(Category).where(
                Category.name == category_data.get("name"),
            )
        ).scalar()

        response = test_client.delete(
            url_for("categories.delete", category_uuid=category.uuid)
        )
        assert response.status_code == HTTPStatus.OK


def test_url_for_edit_category_page(flask_app) -> None:
    """
    Make sure that url for categories.edit returns "/categories/<category_uuid>/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)
    category_uuid = uuid4()

    with flask_app.test_request_context():
        assert (
            url_for("categories.edit", category_uuid=category_uuid)
            == f"/categories/{category_uuid}/"
        )


@pytest.mark.usefixtures("set_temporary_database")
def test_can_edit_category(flask_app) -> None:
    """
    Make sure that categories can be successfully edited

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        category_data = form_data({"name": "work", "color": "#FFFFFF"})
        test_client.post(url_for("categories.create"), data=category_data)

        category = d_session.execute(
            select(Category).where(
                Category.name == category_data.get("name"),
            )
        ).scalar()

        edited_category_data = form_data({"name": "school", "color": "#000000"})
        test_client.post(
            url_for("categories.edit", category_uuid=category.uuid),
            data=edited_category_data,
        )

        category = d_session.execute(
            select(Category).where(
                Category.name == edited_category_data.get("name"),
            )
        ).scalar()

        assert category.name == edited_category_data.get("name")
        assert category.color == edited_category_data.get("color")
