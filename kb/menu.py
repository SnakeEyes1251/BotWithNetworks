from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [[KeyboardButton(text ='Профиль')], [KeyboardButton(text ='Выбрать нейросеть')]]

mainMenu = ReplyKeyboardMarkup(keyboard=buttons)

backButton = [[KeyboardButton(text = 'В главное меню')]]

back = ReplyKeyboardMarkup(keyboard=backButton)