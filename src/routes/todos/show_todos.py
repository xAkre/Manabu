from typing import Any
from datetime import date
from flask import render_template, session as f_session
from database import session as d_session
from database.orm import select, and_
from database.models import Todo
from middleware import require_login


@require_login
def show_todos() -> Any:
    """
    Handle showing categories
    """
    todos = d_session.scalars(
        select(Todo)
        .where(and_(Todo.user == f_session.get("user"), Todo.due_date >= date.today()))
        .order_by(Todo.due_date)
    ).all()

    sorted_dates = []
    sorted_todos = []
    for todo in todos:
        if todo.due_date in sorted_dates:
            sorted_todos[sorted_dates.index(todo.due_date)].append(todo)
        else:
            sorted_todos.append([todo])
            sorted_dates.append(todo.due_date)

    return render_template(
        "pages/todos/show_todos.jinja",
        user=f_session.get("user"),
        sorted_todos=sorted_todos,
    )
