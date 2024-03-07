from typing import Any
from http import HTTPStatus
from flask import session, flash
from middleware import require_login


@require_login
def logout() -> Any:
    """
    Logs the user out upon accessing the /logout/ route
    """
    session.pop("user")
    flash("Successfully logged out", "success")
    return "Logged out", HTTPStatus.OK
