from db.base import Base
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Boolean


class Bot(Base):
    __tablename__ = 'bots'
    id = Column(BigInteger, primary_key=True)
    token = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    is_active = Column(Boolean, default=True)


class Module(Base):
    __tablename__ = 'modules'
    id = Column(BigInteger, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)


class BotModule(Base):
    __tablename__ = 'bot_modules'
    id = Column(BigInteger, primary_key=True)
    bot_id = Column(Integer, ForeignKey('bots.id'))
    function_id = Column(Integer, ForeignKey('modules.id'))
