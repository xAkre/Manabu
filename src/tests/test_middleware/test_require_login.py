import pytest
from flask import session
from routes import auth_router
from middleware import require_login


def test_function_redirects_when_not_logged_in(flask_app):
    """
    Make sure that the require login middleware decorator redirects
    the user when they are not logged in

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)

    with flask_app.app_context(), flask_app.test_request_context():

        @require_login
        def raise_error_if_called() -> None:
            """
            Raises an error if called

            :raises Exception: If called
            """
            raise Exception()

        raise_error_if_called()  # noqa: Suppress "Parameter 'P' unfilled"

        assert True


def test_function_does_not_redirect_when_logged_in(flask_app):
    """
    Make sure that the require login middleware decorator does not redirect
    the user when they are logged in

    :param flask_app: A flask application
    """
    with flask_app.app_context(), flask_app.test_request_context(), pytest.raises(
        Exception
    ):
        session.update({"user": "user"})

        @require_login
        def raise_error_if_called() -> None:
            """
            Raises an error if called

            :raises Exception: If called
            """
            raise Exception()

        raise_error_if_called()  # noqa: Suppress "Parameter 'P' unfilled"

        assert False
