from http import HTTPStatus
from typing import Any
from flask import (
    request,
    flash,
    render_template,
    redirect,
    session as f_session,
    url_for,
)
from database import session as d_session
from database.exc import DatabaseError
from database.models import User
from database.orm import select, or_
from middleware import redirect_if_logged_in
from forms.auth import LoginForm
from utils.security import check_password


@redirect_if_logged_in
def login() -> Any:
    """
    Handles the /login/ route
    """
    if request.method == "GET":
        return render_template("pages/auth/login.jinja", form=LoginForm())

    # Validate user input
    form = LoginForm(request.form)

    if not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "error")
        return (
            render_template("pages/auth/login.jinja", form=form),
            HTTPStatus.BAD_REQUEST,
        )

    # Check if the email or username exists
    try:
        user = d_session.execute(
            select(User).where(
                or_(
                    User.email == form.username_or_email.data,
                    User.username == form.username_or_email.data,
                )
            )
        ).scalar()
    except DatabaseError:
        flash("There was an error while trying to login", "error")
        return (
            render_template("pages/auth/login.jinja", form=form),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if user is None:
        flash("There is no user with that username or email", "error")
        return (
            render_template("pages/auth/login.jinja", form=form),
            HTTPStatus.BAD_REQUEST,
        )

    # Check if the password matches
    if not check_password(form.password.data, user.salt, user.hashed_password):
        flash("Incorrect password", "error")
        return (
            render_template("pages/auth/login.jinja", form=form),
            HTTPStatus.BAD_REQUEST,
        )

    # Log the user in
    f_session.update({"user": user})
    flash("Successfully logged in", "success")
    return redirect(url_for("general.dashboard"))
