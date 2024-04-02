from typing import Any
from flask import request, session as f_session, flash, url_for, redirect
from database import session as d_session
from database.models import Category
from database.exc import DatabaseError
from forms.categories import EditCategoryForm
from middleware import require_login


@require_login
def edit_category(category_uuid: str) -> Any:
    """
    Handle editing categories
    """
    if request.method == "GET":
        return "Edit Category"

    form = EditCategoryForm(request.form)

    # Check if category exists
    category = d_session.get(Category, category_uuid)
    if category is None:
        flash("There is no such category", "error")
        return redirect(url_for("categories.show"))

    # Validate user input
    if not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "error")
        return redirect(url_for("categories.show"))

    # Check if the category belongs to the current user
    d_session.add(f_session.get("user"))

    if not category.user == f_session.get("user"):
        flash("You do not have access to that category", "error")
        return redirect(url_for("categories.show"))

    # Update the category
    try:
        category.name = form.name.data
        category.color = form.color.data
        d_session.commit()
        flash("Successfully updated category", "success")
        return redirect(url_for("categories.edit", category_uuid=category.uuid))
    except DatabaseError:
        flash("There was an error while trying to edit the category", "error")
        return redirect(url_for("categories.show"))
