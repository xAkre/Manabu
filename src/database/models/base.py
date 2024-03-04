from datetime import datetime
from uuid import uuid4
from ..orm import DeclarativeBase, Mapped, String, DateTime, mapped_column, func


class Base(DeclarativeBase):
    """
    The base class for all database models
    """
    uuid: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    """
    This uuid will be generated server side, which is not the most optional solution,
    however, SQLite does not have native support for uuids, only workarounds, and this seems like the
    best solution for now
    """

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
