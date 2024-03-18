from typing import Any
from flask import render_template
from middleware import require_login


@require_login
def dashboard() -> Any:
    """
    Handles the /dashboard/ route
    """
    return render_template("pages/general/dashboard.jinja")
