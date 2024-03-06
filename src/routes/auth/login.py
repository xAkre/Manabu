from typing import Any
from middleware import redirect_if_logged_in


@redirect_if_logged_in
def login() -> Any:
    """
    Handles the /login/ route
    """
    return "Login"
