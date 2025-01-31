from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Создать бота")],
            [KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="ℹ️ Информация")],
        ],
        resize_keyboard=True
    )
