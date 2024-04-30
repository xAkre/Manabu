from typing import Any
from datetime import date
from flask import render_template, session as f_session
from database import session as d_session
from database.orm import select, and_
from database.models import Todo
from middleware import require_login


@require_login
def dashboard() -> Any:
    """
    Handles the /dashboard/ route
    """
    todos_today = d_session.scalars(
        select(Todo).where(
            Todo.user == f_session.get("user"), Todo.due_date == date.today()
        )
    ).all()
    todos_completed = len(
        d_session.scalars(
            select(Todo).where(
                and_(
                    Todo.user == f_session.get("user"),
                    Todo.completed,
                    Todo.due_date == date.today(),
                )
            )
        ).all()
    )
    if todos_completed == 0:
        todos_progress = 0
    else:
        todos_progress = int(todos_completed / len(todos_today) * 100)

    return render_template(
        "pages/general/dashboard.jinja",
        user=f_session.get("user"),
        todos_today=todos_today,
        todos_progress=todos_progress,
        todos_completed=todos_completed,
    )
