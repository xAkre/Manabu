from typing import Any
from http import HTTPStatus
from flask import (
    request,
    flash,
    session as f_session,
    render_template,
    redirect,
    url_for,
)
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
        return render_template(
            "pages/categories/create_category.jinja",
            user=f_session.get("user"),
            form=AddCategoryForm(),
        )

    # Validate user input
    form = AddCategoryForm(request.form)

    if not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "error")
        return (
            render_template(
                "pages/categories/create_category.jinja",
                user=f_session.get("user"),
                form=form,
            ),
            HTTPStatus.BAD_REQUEST,
        )

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
            render_template(
                "pages/categories/create_category.jinja",
                user=f_session.get("user"),
                form=form,
            ),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if existing_category is not None:
        flash("That category already exists", "error")
        return (
            render_template(
                "pages/categories/create_category.jinja",
                user=f_session.get("user"),
                form=form,
            ),
            HTTPStatus.BAD_REQUEST,
        )

    # Add the category
    try:
        new_category = Category(
            name=form.name.data, color=form.color.data, user=f_session.get("user")
        )
        d_session.add(new_category)
        d_session.commit()

        flash("Successfully created category", "success")
        return redirect(url_for("categories.show"))
    except DatabaseError:
        flash("There was an error while trying to create the category", "error")
        return (
            render_template(
                "pages/categories/create_category.jinja",
                user=f_session.get("user"),
                form=form,
            ),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )
