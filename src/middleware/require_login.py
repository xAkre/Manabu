from typing import Callable
from flask import session as f_session, redirect, url_for
from database import session as d_session


def require_login[**P, T](f: Callable[P, T]) -> Callable[P, T]:
    """
    This is a decorator function that checks if a user is logged in by checking for
    a user key in the session, and if they aren't, redirects them to the login page. It also
    automatically adds the user to the database session
    """

    def wrapper(*args: P.args, **kwargs: P.kwargs):
        user = f_session.get("user")
        if user is None:
            return redirect(url_for("auth.login"))

        user = d_session.merge(user)
        f_session.update({"user": user})
        return f(*args, **kwargs)

    wrapper.__name__ = f.__name__

    return wrapper
