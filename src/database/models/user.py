from __future__ import annotations
from typing import List, TYPE_CHECKING
from ..orm import Mapped, mapped_column, relationship
from .base import Base


if TYPE_CHECKING:
    from .category import Category
    from .todo import Todo


class User(Base):
    """
    Represents a user in the database
    """

    __tablename__ = "user"

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    profile_picture: Mapped[str] = mapped_column(nullable=True)
    """
    Stores a path to the user's profile picture on the disk. Can be NULL,
    in which case there is a default profile picture
    """

    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    """
    The user's hashed password using SHA256
    """

    salt: Mapped[str] = mapped_column(nullable=False)
    """
    The salt used to hash the user's password
    """

    categories: Mapped[List[Category]] = relationship(back_populates="user")
    todos: Mapped[List[Todo]] = relationship(back_populates="user")
