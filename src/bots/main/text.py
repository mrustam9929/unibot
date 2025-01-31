STATIC_TEXT = {
    'start': {
        'ru': 'Меню'
    }
}


def get_text(key: str, lang: str = 'ru') -> str:
    return STATIC_TEXT[key][lang]
