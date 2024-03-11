"""
This package contains utilities used with flask
"""

from flask import request


class FieldNotFoundError(Exception):
    """
    This error is raised when a field is not found in a flask object
    """

    def __init__(self, message: str):
        """
        This error is raised when a field is not found in a flask object

        :param message: The error's message
        """
        self.message = message


def form_require(field: str, message: str = "") -> str:
    """
    This function is used to require a field in flask's request's form field. If the field is present, it will
    be returned. If it is not, a KeyError will be thrown

    :param field: The field that is required
    :param message: Optional message that will be passed to the KeyError if it is thrown
    :raises FieldNotFoundError: When the field is not present
    """
    if request.form.get(field):
        return request.form.get(field)

    raise FieldNotFoundError(message)
