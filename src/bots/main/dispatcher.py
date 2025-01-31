from aiogram import Dispatcher
from bots.main.handlers import router
dispatcher = Dispatcher()

dispatcher.include_router(router=router)