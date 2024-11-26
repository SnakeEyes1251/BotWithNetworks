import asyncio
import logging

import handlers.profile as hp
import handlers.text as tp
import handlers.chooseNetwork as np
import handlers.back as bp
import handlers.image as ip

from config import BOT_TOKEN
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from kb.menu import mainMenu

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

class User:
    
    def __init__(self, id, cur_network, chat_id, conv_id, subscribe, dialogs):
        self.id = id
        self.cur_network = cur_network
        self.chat_id = chat_id
        self.conv_id = conv_id
        self.subscribe = subscribe
        self.dialogs = dialogs

class Networks:

    def __init__(self, id, name, context):
        self.id = id
        self.name = name
        self.context = context

class Subscribe:

    def __init__(self, name, start_date, exp_date, cost):
        self.name = name
        self.start_date = start_date
        self.exp_date = exp_date
        self.cost = cost

class Dialog:

    def __init__(self, id, messages, message_count, data):
        self.id = id
        self.messages = messages
        self.message_count = message_count
        self.data = data

class Chat_message:

    def __init__(self, author, text, time):
        self.author = author
        self.text = text
        self.time = time

context = "use imageStableDiffusion"

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! Выбрите действие:", reply_markup=mainMenu)

async def main():
    dp.include_routers(hp.router, np.router, bp.router, tp.router, ip.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
   