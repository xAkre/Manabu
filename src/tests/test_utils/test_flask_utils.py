import pytest
from utils.flask import FieldNotFoundError, form_require


def test_form_require_returns_field_when_present(flask_app) -> None:
    """
    Make sure that the form require utility function correctly returns the required field when it is present
    """
    with flask_app.app_context(), flask_app.test_request_context(data={"username": "username"}):
        assert form_require("username") == "username"


def test_form_require_throws_error_when_field_not_present(flask_app) -> None:
    """
    Make sure that the form require utility function throws a FieldNotFoundError when the required
    field is not present
    """
    with flask_app.app_context(), flask_app.test_request_context():
        with pytest.raises(FieldNotFoundError):
            form_require("username")
