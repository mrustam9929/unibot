import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from settings import settings

bot = Bot(token=settings.main_bot_token)
dp = Dispatcher()
