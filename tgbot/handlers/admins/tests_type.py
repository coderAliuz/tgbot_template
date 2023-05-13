from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher.filters import Text
from tgbot.misc import *
from tgbot.keyboards import *
from tgbot.models import *
from datetime import datetime

async def type_menu(message:Message):
    await message.answer("Siz test bo'limidasiz",reply_markup=type_kb(select_all_type()))
    await tests.type_states.set()
async def stop_tests(message:Message):
    await message.answer("Barcha testlar to'xtatildi")
    restart_test()
async  def type_tests(message:Message):
    await message.answer("Test uchun bo'lim yarating.\nMasalan: IT, Matematika, SMM...",reply_markup=back_kbs)
    await tests.type_add_states.set()

async def type_title(message:Message):
    types=message.text
    type_add(types)
    await message.answer("Siz test bo'limidasiz",reply_markup=type_kb(select_all_type()))
    await tests.type_states.set()
    
async def type_add_tests(message:Message,state:FSMContext):
    types=message.text
    if types in select_all_type():
        await state.update_data(types=types)
        tests_len=len(get_tests(types))
        await message.answer(f"Siz {types} bo'limidasiz\n{tests_len} ta test mavjud\nKerakli tugmani tanlang",reply_markup=test_add_kb)
        await tests.test_add_state.set()
    else:
        await message.answer(f"Kerakli tugmani tanlang",reply_markup=test_add_kb)
        await tests.test_add_state.set()


async def to_home(message:Message,state:FSMContext):
    await state.finish()
    await message.answer("Siz asosiy sahifadasiz\nKerakli tugmani tanlang",reply_markup=home_kb)
    await home.home_states.set()

def register_type(dp:Dispatcher):
    dp.register_message_handler(type_menu,text="Test",state=home.home_states,is_admin=True)
    dp.register_message_handler(to_home,text="Asosiy sahifaga", state=tests, is_admin=True)
    dp.register_message_handler(type_menu,text="Ortga",state=tests.test_add_state, is_admin=True)
    dp.register_message_handler(type_menu,text="Ortga",state=tests.type_add_states,is_admin=True)
    dp.register_message_handler(type_tests,text="Bo'lim qo'shish",state=tests.type_states,is_admin=True)
    dp.register_message_handler(stop_tests,text="Testni to'xtatish",state=tests.type_states,is_admin=True)
    # dp.register_message_handler(to_home,text="Asosiy sahifaga", state=tests.type_add_states, is_admin=True)
    # dp.register_message_handler(to_home,text="Asosiy sahifaga", state=tests.type_states,is_admin=True)
    dp.register_message_handler(type_add_tests,text="Ortga",state=tests.test_states, is_admin=True)

    dp.register_message_handler(type_add_tests,state=tests.type_states,is_admin=True)
    dp.register_message_handler(type_title,state=tests.type_add_states,is_admin=True)
    