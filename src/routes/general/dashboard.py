from typing import Any
from middleware import require_login


@require_login
def dashboard() -> Any:
    """
    Handles the /dashboard/ route
    """
    return "Dashboard"
