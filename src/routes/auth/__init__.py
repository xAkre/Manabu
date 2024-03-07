"""
This package contains a router that handles auth routes
"""
from ..router import Router
from .register import register
from .login import login

auth_router = Router("auth", __name__)
auth_router.add_url_rule("/register/", "register", view_func=register, methods=["GET", "POST"])
auth_router.add_url_rule("/login/", "login", view_func=login, methods=["GET", "POST"])
