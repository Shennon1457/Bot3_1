from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Отправь фото Леди Гаги')
    button2 = KeyboardButton('Перейти на следующую клавиатуру')
    keyboard.add(button1, button2)
    return keyboard


def get_keyboard2():
    keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button3 = KeyboardButton('Отправь фото Большой мамочки')
    button4 = KeyboardButton('Назад')
    keyboard2.add(button3, button4)
    return keyboard2
