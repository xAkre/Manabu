import pytest
from secrets import token_urlsafe
from uuid import uuid4
from flask import Flask
from flask_session import Session as ServerSideSession
from database import set_database, reset_database
from config import Config


@pytest.fixture(autouse=True)
def _reset_database():
    """
    Reset the database before every test
    """
    reset_database()


@pytest.fixture
def temporary_database_path(tmp_path) -> str:
    """
    Generate a temporary database file and return the path to it.
    The database file will be removed after the test has finished

    :param tmp_path: The path to the temporary directory provided by pytest
    :return: The path to the generated temporary database
    """
    temporary_database_path = tmp_path / f"{uuid4()}.sqlite"
    temporary_database_path.touch()

    return str(temporary_database_path)


@pytest.fixture
def set_temporary_database(temporary_database_path) -> str:
    """
    Set the global database to a temporary database and return the path to it.
    The database will be automatically deleted after the test has finished

    :param temporary_database_path: The path to the temporary database
    :return: The path to the temporary database
    """
    database_url = f"sqlite:///{temporary_database_path}"
    set_database(database_url)

    return temporary_database_path


@pytest.fixture
def flask_app() -> Flask:
    """
    Returns a new Flask instance loaded with settings from config.py and basic configuration

    :return: A new flask instance
    """
    app = Flask(
        __name__,
        template_folder=Config.TEMPLATES_FOLDER,
        static_folder=Config.STATIC_FOLDER
    )

    app.config["TESTING"] = True
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SECRET_KEY"] = token_urlsafe(16)

    ServerSideSession(app)

    yield app
