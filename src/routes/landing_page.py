from .router import Router


landing_page_router = Router("landing_page", __name__)


@landing_page_router.route("/")
def landing_page():
    """
    The application's landing page
    """
    return "Hello, world!"
