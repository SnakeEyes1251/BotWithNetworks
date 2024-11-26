from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def create_keyboard(networks: list):
    #Функция для создания клавиатуры из списка возможных вариантов
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{elem}")] for elem in networks])

def inline_create_keyboard(subscrubes):
    #Функция для создания клавиатуры под сообщением из списка возможных вариантов
    return InlineKeyboardMarkup(keyboard=[[InlineKeyboardButton(text=f"{elem}")] for elem in subscrubes])