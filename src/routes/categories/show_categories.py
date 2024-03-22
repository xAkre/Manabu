from typing import Any
from flask import session as f_session
from database import session as d_session
from middleware import require_login


@require_login
def get_categories() -> Any:
    """
    Handle the /categories/ route which will render the users current categories
    """
    d_session.add(f_session.get("user"))
    return "Categories"
