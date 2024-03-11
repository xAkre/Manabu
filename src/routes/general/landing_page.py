from typing import Any
from flask import render_template


def landing_page() -> Any:
    """
    The application's landing page
    """
    return render_template("pages/general/landing_page.jinja")
