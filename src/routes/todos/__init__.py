"""
This package contains a router that handles routes that manage todos
"""

from ..router import Router
from .add_todo import add_todo


todos_router = Router("todos", __name__, url_prefix="/todos")
todos_router.add_url_rule("/add/", "add", add_todo, methods=["GET", "POST"])
