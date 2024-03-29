"""
This package contains a router that handles general routes
"""

from ..router import Router
from .landing_page import landing_page
from .dashboard import dashboard

general_router = Router("general", __name__)
general_router.add_url_rule("/", "landing_page", view_func=landing_page)
general_router.add_url_rule("/dashboard/", "dashboard", view_func=dashboard)
