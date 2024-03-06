from typing import Any
from http import HTTPStatus


def landing_page() -> Any:
    """
    The application's landing page
    """
    return "Hello, world!", HTTPStatus.OK
