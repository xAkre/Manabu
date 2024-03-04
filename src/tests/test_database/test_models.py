from database import engine, set_database
from database.models import Base


def test_can_create_models(temporary_database_path) -> None:
    """
    Make sure that all models can be created

    :param temporary_database_path: The path to the temporary database
    """
    database_url = f"sqlite:///{temporary_database_path}"
    set_database(database_url)

    Base.metadata.create_all(bind=engine)

