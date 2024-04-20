from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date
from ..orm import Mapped, ForeignKey, mapped_column, relationship, Date
from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .category import Category


class Todo(Base):
    """
    Represents a todo in the database
    """

    __tablename__ = "todo"

    title: Mapped[str] = mapped_column(nullable=False)
    due_date: Mapped[date] = mapped_column(Date, nullable=False)
    completed: Mapped[bool] = mapped_column(nullable=False, default=False)
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"), nullable=False)
    category_uuid: Mapped[str] = mapped_column(
        ForeignKey("category.uuid", ondelete="SET NULL"), nullable=True
    )
    """
    Todos do not have to have a category
    """

    user: Mapped[User] = relationship(back_populates="todos")
    category: Mapped[Category] = relationship(back_populates="todos")
