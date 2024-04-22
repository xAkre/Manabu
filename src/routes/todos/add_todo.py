from typing import Any
from http import HTTPStatus
from flask import session as f_session, request, flash, render_template
from database import session as d_session
from database.orm import select, and_
from database.models import Todo, Category
from database.exc import DatabaseError
from middleware import require_login
from forms.todos import AddTodoForm


@require_login
def add_todo() -> Any:
    """
    Handle adding todos
    """
    if request.method == "GET":
        form = AddTodoForm()
        form.category.choices = [("", None)]
        for category in f_session.get("user").categories:
            form.category.choices.append((category.uuid, category))

        return render_template(
            "pages/todos/add_todo.jinja", user=f_session.get("user"), form=form
        )

    form = AddTodoForm(request.form)
    form.category.choices = [("", None)]
    for category in f_session.get("user").categories:
        form.category.choices.append((category.uuid, category))

    if not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "error")
        return (
            render_template(
                "pages/todos/add_todo.jinja", user=f_session.get("user"), form=form
            ),
            HTTPStatus.BAD_REQUEST,
        )

    # Check if the todo already exists
    try:
        existing_todo = d_session.execute(
            select(Todo).where(
                and_(
                    Todo.title == form.title.data,
                    Todo.due_date == form.date.data,
                    Todo.user == f_session.get("user"),
                )
            )
        ).scalar()
    except DatabaseError:
        flash("There was an error while trying to create the todo", "error")
        return (
            render_template(
                "pages/todos/add_todo.jinja", user=f_session.get("user"), form=form
            ),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if existing_todo is not None:
        flash("That todo already exists", "error")
        return (
            render_template(
                "pages/todos/add_todo.jinja", user=f_session.get("user"), form=form
            ),
            HTTPStatus.BAD_REQUEST,
        )

    category = d_session.execute(
        select(Category).where(Category.uuid == form.category.data)
    ).scalar()

    # Add The Todo
    try:
        new_todo = Todo(
            title=form.title.data,
            due_date=form.date.data,
            user=f_session.get("user"),
            category=category,
        )
        d_session.add(new_todo)
        d_session.commit()
        flash("Successfully added todo", "success")
        return "Todo List"
    except DatabaseError:
        flash("There was an error while trying to create the todo", "error")
        return (
            render_template(
                "pages/todos/add_todo.jinja", user=f_session.get("user"), form=form
            ),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )
