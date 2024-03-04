from typing import Any
from flask import Blueprint
import settings


class Router(Blueprint):
    """
    This class represents a collection of application routes. It is based on a flask blueprint
    """

    def __init__(self, name: str, import_name: str, url_prefix: str = "", **kwargs: Any) -> None:
        """
        Represents a collection of application routes. Is based on a flask blueprint.
        This constructor automatically passes static and template folders from settings.py as named parameters
        to the blueprint

        :param name: The name of the router
        :param import_name: The name of the importing package
        :param url_prefix: What to prefix all routes from this router with
        :param kwargs: Optional keyword arguments to pass into the parent blueprint constructor
        """
        super().__init__(
            name,
            import_name,
            template_folder=settings.templates_folder,
            static_folder=settings.static_folder,
            **kwargs
        )
        self.url_prefix = url_prefix
