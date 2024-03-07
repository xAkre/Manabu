from ..orm import Mapped, ForeignKey, mapped_column, relationship
from .base import Base


class Todo(Base):
    """
    Represents a todo in the database
    """
    __tablename__ = "todo"

    title: Mapped[str] = mapped_column(nullable=False)
    completed: Mapped[bool] = mapped_column(nullable=False, default=False)
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"), nullable=False)
    category_uuid: Mapped[str] = mapped_column(ForeignKey("category.uuid"), nullable=True)
    """
    Todos do not have to have a category
    """

    user: Mapped["User"] = relationship(back_populates="todos")  # noqa: Suppress "Unresolved reference 'User'"
    category: Mapped["Category"] = relationship(
        back_populates="todos")  # noqa: Suppress "Unresolved reference 'Category'"
