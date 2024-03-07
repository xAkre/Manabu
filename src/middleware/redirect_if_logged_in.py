from typing import Callable
from flask import session, redirect


def redirect_if_logged_in[**P, T](f: Callable[P, T]) -> Callable[P, T]:
    """
    This is a decorator function that checks if a user is logged in by checking for
    a user key in the session, and if they are, redirects them to the dashboard
    """

    def wrapper(*args: P.args, **kwargs: P.kwargs):
        if session.get("user"):
            return redirect("/dashboard")
        return f(*args, **kwargs)

    wrapper.__name__ = f.__name__

    return wrapper
