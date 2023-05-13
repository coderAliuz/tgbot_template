from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher.filters import Text
from tgbot.misc import *
from tgbot.keyboards import *
from tgbot.models import *
from datetime import datetime

async def admin_start(message: Message,state:FSMContext):
    await state.finish()
    await message.reply("Salom, admin!")
    await message.answer("Kerakli tugmani tanlang",reply_markup=home_kb)
    await home.home_states.set()

async def bot_statistika(message:Message):
    counts=tests_count()
    info=f"Bot foydalanuvchilari: {counts[0]}\nBo'limlar soni: {counts[2]}\nTestlar soni: {counts[1]}"
    await message.answer(info)

async def send_message(message:Message):
    pass
def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    