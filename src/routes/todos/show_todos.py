from typing import Any
from flask import render_template, session as f_session
from database import session as d_session
from database.orm import select
from database.models import Todo
from middleware import require_login


@require_login
def show_todos() -> Any:
    """
    Handle showing categories
    """
    sorted_todos = d_session.scalars(
        select(Todo).where(Todo.user == f_session.get("user")).order_by(Todo.due_date)
    ).all()

    return render_template(
        "pages/todos/show_todos.jinja",
        user=f_session.get("user"),
        sorted_todos=sorted_todos,
    )
