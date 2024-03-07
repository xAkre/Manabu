from typing import Callable
from flask import session, redirect, url_for


def require_login[**P, T](f: Callable[P, T]) -> Callable[P, T]:
    """
    This is a decorator function that checks if a user is logged in by checking for
    a user key in the session, and if they aren't, redirects them to the login page
    """

    def wrapper(*args: P.args, **kwargs: P.kwargs):
        if session.get("user") is None:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    wrapper.__name__ = f.__name__

    return wrapper
