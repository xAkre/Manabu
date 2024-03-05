"""
This package contains SQLAlchemy exceptions. Strictly speaking this package is not needed,
however, I would like to be able to import all database functionality from database, which is why this is here
"""
from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *