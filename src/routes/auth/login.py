from typing import Any
from http import HTTPStatus
from flask import request, flash, redirect, url_for, session as f_session
from database import session as d_session
from database.orm import select, or_
from database.exc import DatabaseError
from database.models import User
from middleware import redirect_if_logged_in
from utils.flask import FieldNotFoundError, form_require
from utils.security import check_password


@redirect_if_logged_in
def login() -> Any:
    """
    Handles the /login/ route
    """
    if request.method == "GET":
        return "Login"

    # Validate user input
    try:
        username_or_email = form_require(
            "username_or_email", "Username or email is required"
        )
        password = form_require("password", "Password is required")
    except FieldNotFoundError as e:
        flash(e.message, "error")
        return e.message, HTTPStatus.BAD_REQUEST

    # Check if the email or username exists
    try:
        user = d_session.execute(
            select(User).where(
                or_(User.email == username_or_email, User.username == username_or_email)
            )
        ).scalar()
    except DatabaseError:
        flash("There was an error while trying to login", "error")
        return (
            "There was an error while trying to login",
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if user is None:
        flash("There is no user with that username or email", "error")
        return "There is no user with that username or email", HTTPStatus.BAD_REQUEST

    # Check if the password matches
    if not check_password(password, user.salt, user.hashed_password):
        flash("Incorrect password", "error")
        return "Incorrect password", HTTPStatus.BAD_REQUEST

    # Log the user in
    f_session.update({"user": user})
    flash("Successfully registered", "success")
    return redirect("/dashboard"), HTTPStatus.OK
