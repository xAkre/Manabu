"""
This package contains SQLAlchemy core and ORM objects and functions. Strictly speaking this package is not needed,
however, I would like to be able to import all database functionality from database, which is why this is here
"""

from sqlalchemy import *  # noqa: Suppress "Unused import statement 'from sqlalchemy import *'"
from sqlalchemy.orm import *  # noqa: Suppress "Unused import statement 'from sqlalchemy.orm import *'"
