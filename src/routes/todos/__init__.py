"""
This package contains a router that handles routes that manage todos
"""

from ..router import Router
from .add_todo import add_todo
from .delete_todo import delete_todo
from .edit_todo import edit_todo
from .show_todos import show_todos

todos_router = Router("todos", __name__, url_prefix="/todos")
todos_router.add_url_rule("/", "show", show_todos, methods=["GET"])
todos_router.add_url_rule("/add/", "add", add_todo, methods=["GET", "POST"])
todos_router.add_url_rule("/<todo_uuid>/", "delete", delete_todo, methods=["DELETE"])
todos_router.add_url_rule("/<todo_uuid>/", "edit", edit_todo, methods=["GET", "POST"])
