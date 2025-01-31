from aiogram import Bot, Dispatcher
from aiogram import types
from bots.main.keyboards import get_menu_keyboard
from settings import settings

bot = Bot(token=settings.main_bot_token)


