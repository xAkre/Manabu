from flask import url_for
from routes import auth_router


def test_url_for_register_page(flask_app):
    """
    Make sure that url for auth.register returns "/register/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)

    with flask_app.app_context(), flask_app.test_request_context():
        assert url_for("auth.register") == "/register/"


def test_can_get_register_page(flask_app):
    """
    Make sure that the register page can be fetched

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.app_context(), flask_app.test_request_context():
        response = test_client.get(url_for("auth.register"))
        assert response.status_code == 200
