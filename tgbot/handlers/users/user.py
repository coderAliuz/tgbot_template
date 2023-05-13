from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery
from tgbot.keyboards import *
from tgbot.misc import *
from tgbot.models import *


async def user_start(message: Message):
    if check_user(message.chat.id) is None:
        await message.reply(f"Assalom aleykum!\nBotdan to'liq foydalanish uchun ism va familiyangizni kiriting.\nESLATMA kiritilgan ism va familiya sertifikatga yoziladi.")
        await users_register.fullname.set()
    else:
        await message.answer("Kerakli tugmani tanlang",reply_markup=main_kb)
        await home.home_states.set()
async def user_fullname(message:Message,state:FSMContext):
    name=message.text
    if " " in name and name.replace(" ", "").isalpha() and len(name)<30:
        await state.update_data(name=name.title())
        await message.answer("Aloqa uchun telefon raqamingizni yuboring.\nNamuna: 998901234567")
        await users_register.next()
    else:
        await message.reply("Iltimos ism familiyangizni to'g'ri kiriting.\nNamuma: Aliyev Vali")

async def user_phone(message:Message,state:FSMContext):
    phone=message.text
    if phone.isdigit() and phone.startswith("998") and len(phone)==12:
        date=await state.get_data()
        name=date['name']
        user_add(message.chat.id,message.chat.username,name,phone)
        await message.answer("Ma'lumotlaringiz qabul qilindi.\nKerakli tugmani tanlang",reply_markup=main_kb)
        await state.finish()
        await home.home_states.set()
    else:
        await message.reply("Iltimos  telefon raqamingizni to'g'ri kiriting.\nNamuma: 998901234567")

async def remember(message:Message,state:FSMContext):
    await message.answer("Testda 20 ta savol va 4 ta javobdan iborat.\nEslatma!Agar testni bekor qilsangiz natijalaringizga qo'shilmaydi.\nNatijalarni bilish uchun testni oxirigacha ishlashingiz lozim.",reply_markup=cancel_kb)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_fullname, state=users_register.fullname)
    dp.register_message_handler(user_phone, state=users_register.phone)
    dp.register_message_handler(remember,text="Qoidalar",state=home.home_states)
