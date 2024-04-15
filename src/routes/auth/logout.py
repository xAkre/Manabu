from typing import Any
from flask import session, flash, redirect, url_for
from middleware import require_login


@require_login
def logout() -> Any:
    """
    Logs the user out upon accessing the /logout/ route
    """
    session.pop("user")
    session.pop("user_uuid")
    flash("Successfully logged out", "success")
    return redirect(url_for("general.landing_page"))
