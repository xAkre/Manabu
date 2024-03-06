from typing import Any
from http import HTTPStatus
from flask import request, redirect, abort, flash, url_for
from utils.flask import FieldNotFoundError, form_require
from database import session
from database.orm import select
from database.exc import DatabaseError
from database.models import User
from middleware import redirect_if_logged_in
from utils.security import hash_password


@redirect_if_logged_in
def register() -> Any:
    """
    Handles the /register/ route
    """
    if request.method == "GET":
        return "Register"

    # Validate input
    try:
        username = form_require("username", "Username is required")
        email = form_require("email", "Email is required")
        password = form_require("password", "Password is required")
        password_confirmation = form_require("password_confirmation", "Password confirmation is required")
    except FieldNotFoundError as e:
        flash(e.message, "error")
        return e.message, HTTPStatus.BAD_REQUEST

    if not password_confirmation == password:
        flash("Password confirmation does not match password", "error")
        return "Password confirmation does not match password", HTTPStatus.BAD_REQUEST

    # Check if user has not already registered before
    existing_user = session.execute(select(User).where(User.email == email)).scalar()

    if existing_user is not None:
        flash("This email already exists", "error")
        return "This email already exists", HTTPStatus.BAD_REQUEST

    # Add the user to the database
    hashed_password, salt = hash_password(password)

    try:
        new_user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            salt=salt
        )
        session.add(new_user)
        session.commit()
        flash("Successfully registered", "success")
        return redirect(url_for("auth.login")), HTTPStatus.CREATED
    except DatabaseError:
        flash("There was an error while trying to register", "error")
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
