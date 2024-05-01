from http import HTTPStatus
from flask import url_for
from routes import general_router, auth_router


def test_url_for_landing_page(flask_app) -> None:
    """
    Make sure that url for general.landing_page returns "/"

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(general_router)

    with flask_app.app_context(), flask_app.test_request_context():
        assert url_for("general.landing_page") == "/"


def test_can_get_landing_page(flask_app) -> None:
    """
    Make sure that the landing page can be fetched

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(general_router)
    flask_app.register_blueprint(auth_router)
    test_client = flask_app.test_client()

    with flask_app.app_context(), flask_app.test_request_context():
        response = test_client.get(
            url_for("general.landing_page"), follow_redirects=True
        )
        assert response.status_code == HTTPStatus.OK
        assert response.request.path == url_for("auth.login")


def test_url_for_dashboard(flask_app) -> None:
    """
    Make sure that url for general.dashboard returns /dashboard/

    :param flask_app: A flask application
    """
    flask_app.register_blueprint(general_router)

    with flask_app.app_context(), flask_app.test_request_context():
        assert url_for("general.dashboard") == "/dashboard/"
