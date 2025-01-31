import enum

from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Enum

from db.base import Base

class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, autoincrement=False)
    role = Column(Enum(UserRole), nullable=False)

class BotUser(Base):
    __tablename__ = "bot_users"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    bot_id = Column(BigInteger, ForeignKey("bots.id"))
