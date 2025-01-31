from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from bots.main.bot import bot
from bots.main.keyboards import get_menu_keyboard
from bots.main.state import BotState, BotCreateState
from bots.main.text import get_text

router = Router()


@router.message()
async def start(message: types.Message, state: FSMContext):
    await state.set_state(BotState.MENU)
    await bot.send_message(message.from_user.id, get_text('start'), reply_markup=get_menu_keyboard())


@router.message(state=BotState.MENU)
async def menu(message: types.Message, state: FSMContext):
    if message.text == get_text('create_bot'):
        await state.set_state(BotCreateState.TOKEN)
        await bot.send_message(message.from_user.id, get_text('create_bot_token'), reply_markup=get_menu_keyboard())


@router.message(state=BotCreateState.TOKEN)
async def create_bot_token(message: types.Message, state: FSMContext):
    token = message.text.strip()

