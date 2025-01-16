from sqlalchemy.orm import DeclarativeBase

from unibot.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
