from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from kb.menu import back

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class profile(StatesGroup):
    profile= State()

router = Router()

@router.message(F.text == 'Профиль')
async def get_profile_button(message: Message, state: FSMContext):
    
    await get_profile_command(message, state)

@router.message(Command('profile', prefix = '/'))
async def get_profile_command(message: Message, state: FSMContext):

    await state.set_state(profile.profile)

    await message.answer("Здесь будет ваш профиль ...", reply_markup=back)