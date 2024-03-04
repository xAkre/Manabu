import pytest
from uuid import uuid4
from database import reset_database


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
