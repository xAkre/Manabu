"""
This package contains a router that handles routes that manage categories
"""

from ..router import Router
from .create_category import create_category


categories_router = Router("categories", __name__, url_prefix="/categories")
categories_router.add_url_rule(
    "/create/", "create", create_category, methods=["GET", "POST"]
)
