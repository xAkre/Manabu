"""
This package contains a router that handles routes that manage categories
"""

from ..router import Router
from .create_category import create_category
from .show_categories import get_categories
from .delete_category import delete_category
from .edit_category import edit_category


categories_router = Router("categories", __name__, url_prefix="/categories")
categories_router.add_url_rule(
    "/create/", "create", create_category, methods=["GET", "POST"]
)
categories_router.add_url_rule("/", "show", get_categories, methods=["GET"])
categories_router.add_url_rule(
    "/<category_uuid>/", "delete", delete_category, methods=["DELETE"]
)
categories_router.add_url_rule(
    "/<category_uuid>/", "edit", edit_category, methods=["GET", "POST"]
)
