"""Утилиты для клавиатур и прочего."""
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_keyboard():
    kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add(KeyboardButton('Добавить фильм'), KeyboardButton('Мои фильмы'))
    return kb

def rating_keyboard():
    kb = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
    kb.add(*[KeyboardButton(str(i)) for i in range(1, 11)])
    kb.add(KeyboardButton('Отмена'))
    return kb
