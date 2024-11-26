import re

from aiogram import Router, F
from aiogram.types import Message
from responses.coze import post_q, get_answ


from kb.menu import back
from temp import StableDiffusion

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class image(StatesGroup):
    imageGen= State()

router = Router()

context = ""
id = ""

@router.message(F.text == "StableDiffusion")
async def choose_text(message: Message, state: FSMContext):
        
        global context
        global id
        context = "use imageStableDiffusion"

        id = f"{StableDiffusion}"
        

        await state.set_state(image.imageGen)
        await message.answer("Задайте ваш вопрос.", reply_markup=back)


@router.message(image.imageGen)
async def handle_message(message: Message):
    user_query = f'{context}: {message.text}'
    user_id = message.from_user.id
    processing_msg = await message.reply("Обрабатываю ваш запрос...")
    print(user_query)

    chat_id, conversation_id = post_q(user_query, user_id, network_id=id)

    if chat_id and conversation_id:
        answer = get_answ(chat_id, conversation_id)
        if answer:
            from main import bot
            # Удаляем сообщение о процессе обработки
            await bot.delete_message(chat_id=processing_msg.chat.id, message_id=processing_msg.message_id)
                
            # Исправленное регулярное выражение
            if re.search(r".jpg|.png|.jpeg", answer):
                await message.answer_photo(photo=answer, reply_markup=back)
            else:
                await message.answer(answer, reply_markup=back)
        else:
            await message.reply("Не удалось получить ответ.")
    else:
        await message.reply("Не удалось получить ответ.")