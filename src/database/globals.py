from typing import Any
from werkzeug.local import LocalProxy
from .orm import Session, Engine, create_engine, sessionmaker, scoped_session


# These types should be used to annotate parameters and variables of type scoped_session and Engine.
# These are simply aliases for the Session and Engine classes from SQLAlchemy, however I put them here
# so that I can import the session and engine as well as their types from the same place
# instead of having to import the types from database.orm
type SessionType = Session
type EngineType = Engine


# These are private variables that store the current engine and scoped session
_engine: Engine | None = None
_session: SessionType | None = None


def _get_session() -> SessionType:
    """
    A function that fetches the current database session

    :return: The current database session
    :raises RuntimeError: When trying to access the session without having set the database
    """
    global _session

    if _session is not None:
        return _session

    raise RuntimeError("Attempted to access the database session without a database being set")


def _get_engine() -> EngineType:
    """
    A function that fetches the current database engine

    :return: The current database engine
    :raises RuntimeError: When trying to access the engine without having set the database
    """
    global _engine

    if _engine is not None:
        return _engine

    raise RuntimeError("Attempted to access the database engine without a database being set")


# Proxies to the private variables, these will be exported from the package
session: SessionType = LocalProxy(_get_session) # noqa: Suppress: "Expected type 'Session', got 'LocalProxy[Session]' instead"
engine: EngineType = LocalProxy(_get_engine) # noqa: Suppress "Expected type 'Engine', got 'LocalProxy[Engine]' instead"


def set_database(database_path: str, *args: Any, **kwargs: any) -> None:
    """
    Set the current global database

    :param database_path: The path to the database
    :param args: Optional arguments to pass to the create engine function
    :param kwargs: Optional keyword arguments to pass to the create engine function
    """
    global _engine, _session

    _engine = create_engine(database_path, *args, **kwargs)
    _session = scoped_session(sessionmaker(bind=_engine))


def reset_database() -> None:
    """
    Set the global engine and session to None. If there is currently a session active, any changes will be
    rolled back
    """
    global _engine, _session

    if _session is not None:
        _session.rollback()
        _session.close()

    _session = None

    if _engine is not None:
        _engine.dispose()

    _engine = None
