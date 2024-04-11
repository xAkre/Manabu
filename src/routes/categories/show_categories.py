from typing import Any
from flask import session as f_session, render_template
from middleware import require_login


@require_login
def get_categories() -> Any:
    """
    Handle the /categories/ route which will render the users current categories
    """
    return render_template(
        "pages/categories/show_categories.jinja", user=f_session.get("user")
    )
