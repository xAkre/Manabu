from typing import Any
from flask import render_template
from middleware import redirect_if_logged_in


@redirect_if_logged_in
def landing_page() -> Any:
    """
    The application's landing page
    """
    return render_template("pages/general/landing_page.jinja")
