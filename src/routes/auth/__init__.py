"""
This package contains a router that handles auth routes
"""
from ..router import Router
from .register import register


auth_router = Router("auth", __name__)
auth_router.add_url_rule("/register/", "register", view_func=register, methods=["GET", "POST"])
