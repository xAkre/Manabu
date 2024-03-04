from flask import url_for
from routes import general_router


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
    test_client = flask_app.test_client()

    with flask_app.app_context(), flask_app.test_request_context():
        response = test_client.get(url_for("general.landing_page"))
        assert response.status_code == 200