from typing import Any
from flask import (
    request,
    session as f_session,
    flash,
    url_for,
    redirect,
    render_template,
)
from database import session as d_session
from database.orm import select, and_
from database.models import Category
from database.exc import DatabaseError
from forms.categories import EditCategoryForm
from middleware import require_login


@require_login
def edit_category(category_uuid: str) -> Any:
    """
    Handle editing categories
    """
    # Check if category exists
    category = d_session.get(Category, category_uuid)
    if category is None:
        flash("There is no such category", "error")
        return redirect(url_for("categories.show"))

    # Check if the category belongs to the current user
    if not category.user == f_session.get("user"):
        flash("You do not have access to that category", "error")
        return redirect(url_for("categories.show"))

    if request.method == "GET":
        return render_template(
            "pages/categories/edit_category.jinja",
            user=f_session.get("user"),
            category=category,
            form=EditCategoryForm(),
        )

    form = EditCategoryForm(request.form)

    # Validate user input
    if not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "error")
        return render_template(
            "pages/categories/edit_category.jinja",
            user=f_session.get("user"),
            category=category,
            form=form,
        )

    # Check to make sure that the category name does not exist
    existing_category = d_session.execute(
        select(Category).where(
            and_(
                Category.uuid != category_uuid,
                Category.name == form.name.data,
                Category.user == f_session.get("user"),
            )
        )
    ).scalar()

    if existing_category is not None:
        flash("A category with that name already exists", "error")
        return render_template(
            "pages/categories/edit_category.jinja",
            user=f_session.get("user"),
            category=category,
            form=form,
        )

    # Update the category
    try:
        category.name = form.name.data
        category.color = form.color.data
        d_session.commit()
        flash("Successfully updated category", "success")
        return redirect(url_for("categories.show"))
    except DatabaseError:
        flash("There was an error while trying to edit the category", "error")
        return render_template(
            "pages/categories/edit_category.jinja",
            user=f_session.get("user"),
            category=category,
            form=form,
        )
