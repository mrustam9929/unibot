from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from db.models.users import User, BotUser, UserRole


class UserDAO:
    @staticmethod
    async def get_user(session: AsyncSession, user_id: int) -> User | None:
        """Получить пользователя по ID"""
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def create_user(session: AsyncSession, user_id: int, role: UserRole) -> User:
        """Создать пользователя"""
        user = User(id=user_id, role=role)
        session.add(user)
        await session.commit()
        return user


class BotUserDAO:
    @staticmethod
    async def create_bot_user(session: AsyncSession, user_id: int, bot_id: int) -> BotUser:
        """Добавить связь пользователя и бота"""
        bot_user = BotUser(user_id=user_id, bot_id=bot_id)
        session.add(bot_user)
        await session.commit()
        return bot_user
