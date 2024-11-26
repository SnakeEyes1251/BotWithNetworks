from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from kb.keyboards import create_keyboard
from temp import networksList

router = Router()

@router.message(F.text == 'Выбрать нейросеть')
async def choose_network_button(message: Message):
    
    await choose_network_command(message)

@router.message(Command('text', prefix = '/'))
async def choose_network_command(message: Message):
    
    keyboard = create_keyboard(networksList)

    await message.answer("Выберите нейросеть:", reply_markup=keyboard)