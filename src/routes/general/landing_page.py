from typing import Any
from flask import redirect, url_for
from middleware import redirect_if_logged_in


@redirect_if_logged_in
def landing_page() -> Any:
    """
    The application's landing page
    """
    return redirect(url_for("auth.login"))
