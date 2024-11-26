from aiogram import F, Router
from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from kb.menu import mainMenu

router = Router()

@router.message(F.text == 'В главное меню')
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Чем ещё могу помочь?", reply_markup=mainMenu)