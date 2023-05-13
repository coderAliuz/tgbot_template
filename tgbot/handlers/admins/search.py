from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher.filters import Text
from tgbot.misc import *
from tgbot.keyboards import *
from tgbot.models import *

async def search_main(message:Message,state=FSMContext):
    await message.answer("Qidiruv bo'limini tanlang",reply_markup=search_kb)
    await searches.search.set()

async def search_test(message:Message,state=FSMContext):
    await message.answer("Test idsini yuboring",reply_markup=back_kbs)
    await searches.test_states.set()

async def info_test(message:Message,state:FSMContext):
        ids=message.text
        if ids.isdigit() and test_info(int(ids)) is not None:
            info=test_info(int(ids))
            if info[2]=="None":
                await message.answer(f"#id{info[0]}\n{info[1]}\n{info[3]}\n{info[4]}\n{info[5]}\n{info[6]}\n{info[7]}",reply_markup=delete_inline_kb(ids))
            else:
                await message.answer_photo(photo=info[2],caption=f"#id{info[0]}\n{info[1]}\n{info[3]}\n{info[4]}\n{info[5]}\n{info[6]}\n{info[7]}",reply_markup=delete_inline_kb(ids))
        else:
            await message.answer("Test topilmadi")

async def delete_tests(call:CallbackQuery,state:FSMContext):
    ids=(call.date).split("_")[1]
    test_delete(int(ids))
    await call.message.edit_text("Test o'chirildi\nTest idsini yuboring")

async def search_user(message:Message):
    await message.answer("Foydalanuvchi idsini yuboring",reply_markup=back_kbs)
    await searches.user_states.set()

async def info_user(message:Message):
        ids=message.text
        if ids.isdigit() and check_user(int(ids)) is not None:
            info=result_info(int(ids))
            text=f"#user{ids}\n{info[0]}\nNatija: {info[1]}"
            if info[1]==0:
                await message.answer(f"{text}\nHali test ishlanmagan.")
            elif info[2] is not None:
                await message.answer_photo(info[2],caption=f"{text}\nVaqt: {info[3]}\nSertifikat tasdiqlangan.")
            else:
                await message.answer(f"{text}\nVaqt: {info[3]}\n\nSertifikat tasdiqlanmagan.")
        else:
            await message.answer("Foydalanuvchi topilmadi")      

async def ret_home(message:Message):
    await message.answer("Kerakli tugmani tanlang",reply_markup=home_kb)
    await home.home_states.set()


def register_search(dp: Dispatcher):
    dp.register_message_handler(search_main, text="Qidirish",state=home.home_states, is_admin=True)
    dp.register_message_handler(search_main, text="Ortga",state=searches, is_admin=True)
    dp.register_message_handler(ret_home, text="Asosiy sahifaga",state=searches, is_admin=True)
    dp.register_message_handler(search_test,text="Test qidirish", state=searches.search, is_admin=True)
    dp.register_message_handler(info_test, state=searches.test_states, is_admin=True)
    dp.register_callback_query_handler(delete_tests,Text(startswith=("del")),state=searches.test_states,is_admin=True)
    dp.register_message_handler(search_user,text="Foydalanuvchi qidirish", state=searches.search, is_admin=True)
    dp.register_message_handler(info_user, state=searches.user_states, is_admin=True)


