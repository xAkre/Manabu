from typing import List
from ..orm import Mapped, String, ForeignKey, mapped_column, relationship
from .base import Base


class Category(Base):
    """
    Represents a category in the database
    """
    __tablename__ = "category"

    name: Mapped[str] = mapped_column(nullable=False)
    color: Mapped[str] = mapped_column(String(7), nullable=False, default="#a3a3a3")
    """
    The color of the category represented as a hex color
    """

    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="categories")  # noqa: Suppress "Unresolved reference 'User'"
    todos: Mapped[List["Todo"]] = relationship(
        back_populates="category")  # noqa: Suppress "Unresolved reference 'Todo'"
