from typing import Any
from http import HTTPStatus
from flask import session as f_session
from database import session as d_session
from database.models import Todo
from database.exc import DatabaseError
from middleware import require_login


@require_login
def delete_todo(todo_uuid) -> Any:
    """
    Handle deleting todos. This route should be used as an api route as it does not return a page

    :param todo_uuid: The todo to delete
    """
    todo = d_session.get(Todo, todo_uuid)
    if todo is None:
        return {"message": "That todo does not exist"}, HTTPStatus.BAD_REQUEST

    # Check if todo belongs to user
    if not todo.user == f_session.get("user"):
        return {"message": "Unauthorized"}, HTTPStatus.FORBIDDEN

    # Delete the todo
    try:
        d_session.delete(todo)
        d_session.commit()
        return {"message": "Successfully deleted todo"}, HTTPStatus.OK
    except DatabaseError:
        d_session.rollback()
        return {
            "message": "There was an error while trying to delete that todo"
        }, HTTPStatus.INTERNAL_SERVER_ERROR
