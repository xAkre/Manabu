from typing import Any
from http import HTTPStatus
from flask import request, redirect, abort, flash, url_for, render_template
from database import session
from database.orm import select
from database.exc import DatabaseError
from database.models import User
from middleware import redirect_if_logged_in
from forms.auth import RegisterForm
from utils.security import hash_password


@redirect_if_logged_in
def register() -> Any:
    """
    Handles the /register/ route
    """
    if request.method == "GET":
        return render_template("pages/auth/register.jinja", form=RegisterForm())

    # Validate input
    form = RegisterForm(request.form)

    if not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "error")
        return (
            render_template("pages/auth/register.jinja", form=form),
            HTTPStatus.BAD_REQUEST,
        )

    # Check if user has not already registered before
    existing_user = session.execute(
        select(User).where(User.email == form.email.data)
    ).scalar()

    if existing_user is not None:
        flash("This email already exists", "error")
        return (
            render_template("pages/auth/register.jinja", form=form),
            HTTPStatus.BAD_REQUEST,
        )

    # Add the user to the database
    hashed_password, salt = hash_password(form.password.data)

    try:
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            hashed_password=hashed_password,
            salt=salt,
        )
        session.add(new_user)
        session.commit()

        flash("Successfully registered", "success")
        return redirect(url_for("auth.login"))
    except DatabaseError:
        flash("There was an error while trying to register", "error")
        return (
            render_template("pages/auth/register.jinja", form=form),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )
