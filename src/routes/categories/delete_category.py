from typing import Any
from http import HTTPStatus
from flask import session as f_session
from database import session as d_session
from database.exc import DatabaseError
from database.models import Category
from middleware import require_login


@require_login
def delete_category(category_uuid: str) -> Any:
    """
    Handle deleting categories

    :param category_uuid: The uuid of the category to delete
    """
    d_session.add(f_session.get("user"))

    # Check if category exists
    category = d_session.get(Category, category_uuid)
    if category is None:
        return {"message": "That category does not exist"}, HTTPStatus.BAD_REQUEST

    # Check if category belongs to user
    if not category.user == f_session.get("user"):
        return {"message": "Unauthorized"}, HTTPStatus.FORBIDDEN

    # Delete the category
    try:
        d_session.delete(category)
        d_session.commit()
        return {"message": "Successfully deleted category"}, HTTPStatus.OK
    except DatabaseError:
        d_session.rollback()
        return {
            "message": "There was an error while trying to delete that category"
        }, HTTPStatus.INTERNAL_SERVER_ERROR
