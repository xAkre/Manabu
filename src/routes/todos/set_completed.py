from typing import Any
from http import HTTPStatus
from flask import session as f_session, request
from multidict import MultiDict
from database import session as d_session
from database.models import Todo
from database.exc import DatabaseError
from middleware import require_login
from forms.todos import SetCompletedStatusTodoForm


@require_login
def set_completed(todo_uuid) -> Any:
    """
    Handle setting the completed status of a todo. This route should be used as an api route as it does not return a page

    :param todo_uuid: The todo to update
    """
    todo = d_session.get(Todo, todo_uuid)
    if todo is None:
        return {"message": "That todo does not exist"}, HTTPStatus.BAD_REQUEST

    # Check if todo belongs to user
    if not todo.user == f_session.get("user"):
        return {"message": "Unauthorized"}, HTTPStatus.FORBIDDEN

    form = SetCompletedStatusTodoForm(MultiDict(request.json))

    if not form.validate():
        return {"message": "Invalid data"}, HTTPStatus.BAD_REQUEST

    # Update the todo
    try:
        todo.completed = form.status.data
        d_session.add(todo)
        d_session.commit()
        return {"message": ""}, HTTPStatus.OK
    except DatabaseError:
        d_session.rollback()
        return {
            "message": "There was an error while trying to update the todo"
        }, HTTPStatus.INTERNAL_SERVER_ERROR
