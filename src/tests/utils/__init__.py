"""
This package contains utility functions for testing
"""

from multidict import MultiDict


def form_data(dictionary: dict) -> MultiDict:
    """
    Returns a dictionary as a multi dict that can be used as form data

    :return: The dictionary passed as an argument as a multi dict
    """

    return MultiDict(dictionary)
