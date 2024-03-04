import pytest
from database import engine
from database.models import Base


@pytest.mark.usefixtures("set_temporary_database")
def test_can_create_models() -> None:
    """
    Make sure that all models can be created
    """
    Base.metadata.create_all(bind=engine)
