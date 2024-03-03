import pytest
from os import path, makedirs, remove, rmdir
from uuid import uuid4
from database import reset_database


@pytest.fixture(autouse=True)
def _reset_database():
    """
    Reset the database before every test
    """
    reset_database()


@pytest.fixture
def temporary_databases_folder() -> str:
    """
    Create a temporary databases folder and return the path to it.
    The folder will be removed after the test has finished

    :return: The path to the generated temporary databases folder
    """
    temporary_databases_folder_path = path.join(path.dirname(__file__), "temporary_databases")
    makedirs(temporary_databases_folder_path, exist_ok=True)

    yield temporary_databases_folder_path

    rmdir(temporary_databases_folder_path)


@pytest.fixture
def temporary_database_path(temporary_databases_folder) -> str:
    """
    Generate a temporary database file and return the path to it.
    The database file will be removed after the test has finished

    :param temporary_databases_folder: The path to the temporary databases folder
    :return: The path to the generated temporary database
    """
    temporary_database_path = path.join(temporary_databases_folder, f"{uuid4()}.sqlite")
    open(temporary_database_path, "w").close()

    yield temporary_database_path

    remove(temporary_database_path)
