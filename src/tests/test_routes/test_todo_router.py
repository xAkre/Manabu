import pytest
from http import HTTPStatus
from uuid import uuid4
from flask import url_for, session as f_session, get_flashed_messages
from database import session as d_session
from database.orm import select
from database.models import Category, Todo
from routes import todos_router, categories_router
from tests.utils import register_and_login, form_data


def test_url_for_add_todo_page(flask_app) -> None:
    """
    Make sure that url for todos.add returns "/todos/add/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)

    with flask_app.test_request_context():
        assert url_for("todos.add") == "/todos/add/"


@pytest.mark.usefixtures("set_temporary_database")
def test_can_get_add_todo_page(flask_app) -> None:
    """
    Make sure that the add todo page can be fetched

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        response = test_client.get(url_for("todos.add"))
        assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures("set_temporary_database")
def test_can_add_todo(flask_app) -> None:
    """
    Make sure that the add todo route can successfully add a todo

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context(), test_client:
        register_and_login(test_client, flask_app=flask_app)
        category_data = form_data({"name": "work", "color": "#FFFFFF"})
        test_client.post(url_for("categories.create"), data=category_data)
        category = d_session.execute(
            select(Category).where(Category.name == category_data.get("name"))
        ).scalar()
        todo_data = form_data(
            {
                "title": "Do some freelancing work",
                "date": "2024-12-12",
                "category": category.uuid,
            }
        )

        response = test_client.post(url_for("todos.add"), data=todo_data)
        assert response.status_code == 200
        assert len(f_session.get("user").todos) == 1
        assert f_session.get("user").todos[0].category == category


@pytest.mark.usefixtures("set_temporary_database")
def test_can_add_todo_without_category(flask_app) -> None:
    """
    Make sure that the add todo route can successfully add a todo without a category

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context(), test_client:
        register_and_login(test_client, flask_app=flask_app)
        todo_data = form_data(
            {"title": "Do some freelancing work", "date": "2024-12-12", "category": ""}
        )

        response = test_client.post(url_for("todos.add"), data=todo_data)
        assert response.status_code == 200
        assert len(f_session.get("user").todos) == 1
        assert not f_session.get("user").todos[0].category


@pytest.mark.usefixtures("set_temporary_database")
def test_cant_add_todo_that_already_exists(flask_app) -> None:
    """
    Make sure that the add todo route does not allow adding the same todo twice

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        todo_data = form_data(
            {"title": "Do some freelancing work", "date": "2024-12-12", "category": ""}
        )
        test_client.post(url_for("todos.add"), data=todo_data)
        response = test_client.post(url_for("todos.add"), data=todo_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.usefixtures("set_temporary_database")
def test_cant_add_todo_that_doesnt_belong_to_user(flask_app) -> None:
    """
    Make sure that the add todo route does not allow adding a todo with a category
    that does not belong to the user

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        todo_data = form_data(
            {
                "title": "Do some freelancing work",
                "date": "2024-12-12",
                "category": str(uuid4()),
            }
        )
        response = test_client.post(url_for("todos.add"), data=todo_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.usefixtures("set_temporary_database")
def test_cant_add_todo_with_invalid_date(flask_app) -> None:
    """
    Make sure that the add todo route does not allow adding a todo with an invalid due date

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        todo_data = form_data(
            {"title": "Do some freelancing work", "date": "2024-12-32", "category": ""}
        )
        response = test_client.post(url_for("todos.add"), data=todo_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST


def test_url_for_delete_todo_route(flask_app) -> None:
    """
    Make sure that url for todos.delete returns "/todos/<todo_uuid>/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    uuid = str(uuid4())

    with flask_app.test_request_context():
        assert url_for("todos.delete", todo_uuid=uuid) == f"/todos/{uuid}/"


@pytest.mark.usefixtures("set_temporary_database")
def test_can_delete_todo(flask_app) -> None:
    """
    Make sure that the delete todo route can successfully delete a todo

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context(), test_client:
        register_and_login(test_client, flask_app=flask_app)
        todo_data = form_data(
            {"title": "Go to work", "date": "2025-01-01", "category": ""}
        )
        test_client.post(url_for("todos.add"), data=todo_data)

        todo = d_session.execute(
            select(Todo).where(
                Todo.title == todo_data.get("title"),
            )
        ).scalar()

        response = test_client.delete(url_for("todos.delete", todo_uuid=todo.uuid))
        assert response.status_code == HTTPStatus.OK
        assert len(f_session.get("user").todos) == 0


def test_url_for_edit_todo_route(flask_app) -> None:
    """
    Make sure that url for todos.edit returns "/todos/<todo_uuid>/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    uuid = str(uuid4())

    with flask_app.test_request_context():
        assert url_for("todos.edit", todo_uuid=uuid) == f"/todos/{uuid}/"


@pytest.mark.usefixtures("set_temporary_database")
def test_can_edit_todo(flask_app) -> None:
    """
    Make sure that todos can be successfully edited

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    flask_app.register_blueprint(categories_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        todo_data = form_data(
            {"title": "Go to work", "date": "2024-01-01", "category": ""}
        )
        test_client.post(url_for("todos.add"), data=todo_data)

        todo = d_session.execute(
            select(Todo).where(
                Todo.title == todo_data.get("title"),
            )
        ).scalar()

        new_category_data = form_data({"name": "School", "color": "#FFFFFF"})
        test_client.post(url_for("categories.create"), data=new_category_data)
        category = d_session.execute(
            select(Category).where(Category.name == new_category_data.get("name"))
        ).scalar()

        edited_todo_data = form_data(
            {"title": "Go to school", "date": "2024-01-02", "category": category.uuid}
        )
        test_client.post(
            url_for("todos.edit", todo_uuid=todo.uuid),
            data=edited_todo_data,
        )

        todo = d_session.execute(
            select(Todo).where(
                Todo.title == edited_todo_data.get("title"),
            )
        ).scalar()

        assert todo.title == edited_todo_data.get("title")
        assert str(todo.due_date) == edited_todo_data.get("date")
        assert todo.category == category


def test_url_for_show_todos_page(flask_app) -> None:
    """
    Make sure that url for todos.show returns "/todos/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)

    with flask_app.test_request_context():
        assert url_for("todos.show") == "/todos/"


@pytest.mark.usefixtures("set_temporary_database")
def test_can_get_show_todos_page(flask_app) -> None:
    """
    Make sure that the show categories page can be fetched

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(todos_router)
    test_client = flask_app.test_client()

    with flask_app.test_request_context():
        register_and_login(test_client, flask_app=flask_app)
        response = test_client.get(url_for("todos.show"))

        assert response.status_code == HTTPStatus.OK
