import pytest
from database import session, engine, set_database, reset_database


def test_can_set_database(temporary_database_path):
    """
    Make sure that the global database can be set
    """
    database_url = f"sqlite:///{temporary_database_path}"
    set_database(database_url)

    assert engine is not None
    assert str(engine.url) == database_url
    assert session is not None
    assert session.bind == engine


def test_can_reset_database(temporary_database_path):
    """
    Make sure that the global database can be reset
    """
    database_url = f"sqlite:///{temporary_database_path}"
    set_database(database_url)
    reset_database()

    with pytest.raises(RuntimeError):
        print(engine)

    with pytest.raises(RuntimeError):
        print(session)


def test_can_update_database(temporary_database_path):
    """
    Make sure that the global database can be updated
    """
    database_url = f"sqlite:///{temporary_database_path}"
    set_database(database_url)

    updated_database_url = f"sqlite:///{temporary_database_path}-updated"
    set_database(updated_database_url)

    assert str(engine.url) == updated_database_url


def test_trying_to_access_uninitialized_session_throws_error():
    """
    Make sure that a RuntimeError is thrown when trying to access the session variable before a database has been set
    """
    with pytest.raises(RuntimeError):
        print(session)


def test_trying_to_access_uninitialized_engine_throws_error():
    """
    Make sure that a RuntimeError is thrown when trying to access the engine variable before a database has been set
    """
    with pytest.raises(RuntimeError):
        print(engine)



