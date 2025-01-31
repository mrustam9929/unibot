from aiogram.fsm.state import State, StatesGroup


class BotCreateState(StatesGroup):
    TOKEN = State()


class BotState(StatesGroup):
    MENU = State()
    CREATE_BOT = State()
