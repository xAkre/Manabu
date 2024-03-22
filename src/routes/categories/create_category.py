from typing import Any
from http import HTTPStatus
from flask import request, flash, session as f_session
from database import session as d_session
from database.orm import select, and_
from database.exc import DatabaseError
from database.models import Category
from middleware import require_login
from forms.categories import AddCategoryForm


@require_login
def create_category() -> Any:
    """
    Handle creating categories
    """
    if request.method == "GET":
        return "Create category"

    # Validate user input
    form = AddCategoryForm(request.form)

    if not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "error")
        return "Invalid Input", HTTPStatus.BAD_REQUEST

    # Check if the category already exists
    try:
        existing_category = d_session.execute(
            select(Category).where(
                and_(
                    Category.name == form.name.data,
                    Category.user == f_session.get("user"),
                )
            )
        ).scalar()
    except DatabaseError:
        flash("There was an error while trying to create the category", "error")
        return (
            "There was an error while trying to create the category",
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if existing_category is not None:
        flash("That category already exists", "error")
        return "That category already exists", HTTPStatus.BAD_REQUEST

    # Add the category
    try:
        new_category = Category(
            name=form.name.data, color=form.color.data, user=f_session.get("user")
        )
        d_session.add(new_category)
        d_session.commit()

        flash("Successfully created category", "success")
        return "Successfully created category", HTTPStatus.CREATED
    except DatabaseError:
        flash("There was an error while trying to create the category", "error")
        return (
            "There was an error while trying to create the category",
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )
