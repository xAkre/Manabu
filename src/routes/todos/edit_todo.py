from typing import Any
from http import HTTPStatus
from flask import (
    session as f_session,
    flash,
    request,
    render_template,
    redirect,
    url_for,
)
from database import session as d_session
from database.orm import select, and_
from database.exc import DatabaseError
from database.models import Todo, Category
from forms.todos import EditTodoForm
from middleware import require_login


@require_login
def edit_todo(todo_uuid: str) -> Any:
    """
    Handle editing todos
    """
    # Check if todo exists
    todo = d_session.get(Todo, todo_uuid)

    if todo is None:
        flash("That todo does not exist", "error")
        return redirect(url_for("todos.show")), HTTPStatus.BAD_REQUEST

    # Check if todo belongs to user
    if not todo.user == f_session.get("user"):
        flash("You do not have access to that category", "error")
        return redirect(url_for("todos.show")), HTTPStatus.FORBIDDEN

    if request.method == "GET":
        form = EditTodoForm()
        form.category.choices = [("", None)]
        for category in f_session.get("user").categories:
            form.category.choices.append((category.uuid, category.name))

        return render_template(
            "pages/todos/edit_todo.jinja",
            user=f_session.get("user"),
            todo=todo,
            form=form,
        )

    form = EditTodoForm(request.form)
    form.category.choices = [("", None)]
    for category in f_session.get("user").categories:
        form.category.choices.append((category.uuid, category.name))

    if not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "error")
        return (
            render_template(
                "pages/todos/edit_todo.jinja",
                user=f_session.get("user"),
                todo=todo,
                form=form,
            ),
            HTTPStatus.BAD_REQUEST,
        )

    # Check if a todo with the same data exists

    existing_category = d_session.execute(
        select(Category).where(
            and_(
                Category.uuid == form.category.data,
                Category.user == f_session.get("user"),
            )
        )
    ).scalar()
    try:
        existing_todo = d_session.execute(
            select(Todo).where(
                and_(
                    Todo.title == form.title.data,
                    Todo.due_date == form.date.data,
                    Todo.user == f_session.get("user"),
                    Todo.category == existing_category,
                )
            )
        ).scalar()
    except DatabaseError:
        flash("There was an error while trying to edit the todo", "error")
        return (
            render_template(
                "pages/todos/edit_todo.jinja",
                user=f_session.get("user"),
                todo=todo,
                form=form,
            ),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if existing_todo is not None:
        if not form.completed.data == existing_todo.completed:
            try:
                existing_todo.completed = form.completed.data
                d_session.commit()
                flash("Successfully edited todo", "success")
                return redirect(url_for("todos.show"))
            except DatabaseError:
                flash("There was an error while trying to edit the todo", "error")
                return (
                    render_template(
                        "pages/todos/edit_todo.jinja",
                        user=f_session.get("user"),
                        todo=todo,
                        form=form,
                    ),
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                )

        flash("That todo already exists", "error")
        return (
            render_template(
                "pages/todos/edit_todo.jinja",
                user=f_session.get("user"),
                todo=todo,
                form=form,
            ),
            HTTPStatus.BAD_REQUEST,
        )

    # Edit the todo
    try:
        todo.category_uuid = form.category.data
        todo.title = form.title.data
        todo.due_date = form.date.data
        todo.completed = form.completed.data
        d_session.commit()
        flash("Successfully edited todo", "success")
        return redirect(url_for("todos.show"))
    except DatabaseError:
        flash("There was an error while trying to edit the todo", "error")
        return (
            render_template(
                "pages/todos/edit_todo.jinja",
                user=f_session.get("user"),
                todo=todo,
                form=form,
            ),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )
