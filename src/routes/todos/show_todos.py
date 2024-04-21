from typing import Any
from middleware import require_login


@require_login
def show_todos() -> Any:
    """
    Handle showing categories
    """
    return "Todo List"
