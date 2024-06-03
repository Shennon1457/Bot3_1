from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def k_inl():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://ru.wikipedia.org/wiki/Леди_Гага')
    but_inline2 = InlineKeyboardButton('Look', url='https://ru.wikipedia.org/wiki/Леди_Гага')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
