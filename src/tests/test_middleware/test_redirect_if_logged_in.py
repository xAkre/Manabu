import pytest
from flask import session
from middleware import redirect_if_logged_in


def test_function_redirects_if_user_is_logged_in(flask_app) -> None:
    """
    Make sure that the redirect if logged in middleware decorator redirects
    the user when they are logged in

    :param flask_app: A flask application
    """
    with flask_app.app_context(), flask_app.test_request_context():
        session["user"] = "user"

        @redirect_if_logged_in
        def raise_error_if_called() -> None:
            """
            Raises an error if called

            :raises Exception: If called
            """
            raise Exception()

        raise_error_if_called()  # noqa: Suppress "Parameter 'P' unfilled"

        assert True


def test_function_does_not_redirect_when_user_not_logged_in(flask_app) -> None:
    """
    Make sure that the redirect if logged in middleware decorator does not redirect when the user
    is not logged in

    :param flask_app: A flask application
    """
    with flask_app.app_context(), flask_app.test_request_context(), pytest.raises(Exception):
        @redirect_if_logged_in
        def raise_error_if_called() -> None:
            """
            Raises an error if called

            :raises Exception: If called
            """
            raise Exception()

        raise_error_if_called()  # noqa: Suppress "Parameter 'P' unfilled"

        assert False
