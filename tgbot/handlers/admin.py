from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher.filters import Text
from tgbot.misc import *
from tgbot.keyboards import *
from tgbot.models import *
from datetime import datetime

async def admin_start(message: Message,state=FSMContext):
    await message.reply("Salom, admin!")
    await message.answer("Kerakli tugmani tanlang",reply_markup=home_kb)
    await home.home_states.set()

async def add_tests(message:Message,state=FSMContext):
    if message.text=="Test qo'shish":
        await message.answer("Test mazmunini kiriting",reply_markup=test_kb())
        await tests.test_states.set()
    elif message.text=="Qidirish":
        await message.answer("Test idsini yuboring",reply_markup=beck_kb) 
        await tests.delete_states.set()
    else:
        await message.answer("Kerakli tugmani tanlang",reply_markup=home_kb)


async def cancel_test(message:Message,state:FSMContext):
    await message.reply("Test bekor qilindi",reply_markup=home_kb)
    await state.finish()

async def test_title(message:Message,state:FSMContext):
    title=message.text
    await message.reply("Testni rasm bo'lsa, rasm yuboring aks holda o'tkazib yuboring",
                        reply_markup=test_kb("O'tkazib yuborish"))
    await state.update_data(title=title)
    await state.update_data(answer=[])
    await state.update_data(photo=None)
    await tests.next()

async def next_step(message:Message,state:FSMContext):
    await message.reply("To'g'ri javobni yuboring",reply_markup=test_kb())
    await tests.next()

async def test_photo(message:Message,state:FSMContext):
    photo=message.photo[-1].file_id
    await state.update_data(photo=photo)
    await message.reply("To'g'ri javobni yuboring",reply_markup=test_kb())
    await tests.next()

async def correct_answer(message:Message,state:FSMContext):
    test_answer= message.text
    answer_data=await state.get_data()
    answer=answer_data['answer']
    answer.append(test_answer)
    await message.answer("Noto'g'ri javobni kiriting")
    await state.update_data(answer=answer)

    if len(answer)==4:
        title=answer_data['title']
        testlar='\n '.join(answer)
        photo=answer_data['photo']
        if photo is None:
            await message.answer(f"{title}\n {testlar}\n\nTestni tasdiqlaysizmi",reply_markup=chekcout)
        else:
            await message.answer_photo(photo,caption=f"{title}\n {testlar}\n\nTestni tasdiqlaysizmi",reply_markup=chekcout)
        await tests.next()


async def check_test(call:CallbackQuery,state:FSMContext):
    check=call.data.split(("_"))[1]
    answer_data=await state.get_data()
    answer=answer_data['answer']
    title=answer_data['title']
    testlar='\n '.join(answer)
    photo=answer_data['photo']
    
    if photo is None:
        if check=="yes":
            ids=test_add(title, photo, answer, str(datetime.today()))
            await call.message.edit_text(f"#id{ids}\n{title} \n{testlar}\n\nTest qabul qilindi") 
        else:
            await call.message.edit_text(f"{title} \n{testlar}\n\nTest bekor qilindi")
    else:
        if check=="yes":
            ids=test_add(title, photo, answer, str(datetime.today()))
            await call.message.edit_caption(f"#id{ids}\n{title} \n{testlar}\n\nTest qabul qilindi")
        else:
            await call.message.edit_caption(f"{title} \n{testlar}\n\nTest bekor qilindi")    

    await state.finish()
    await call.message.answer("Kerakli tugmani tanlang",reply_markup=home_kb)
    await home.home_states.set()

async def info_tests(message:Message,state:FSMContext):
    ids= message.text
    if ids=="Asosiy sahifaga":
        await message.answer("Kerakli tugmani tanlang",reply_markup=home_kb)
        await home.home_states.set()
    else:
        if ids.isdigit() and test_info(int(ids)) is not None:
            info=test_info(int(ids))
            if info[2] is not None:
                await message.answer(f"#id{info[0]}\n{info[1]}\n{info[3]}\n{info[4]}\n{info[5]}\n{info[6]}\n{info[7]}",reply_markup=delete_inline_kb(ids))
            else:pass 
                # await message.answer_photo(photo=info[2],caption=f"#id{info[0]}\n{info[1]}\n{info[3]}\n{info[4]}\n{info[5]}\n{info[6]}\n{info[7]}",reply_markup=delete_inline_kb(ids))
        else:
            await message.answer("Test topilmadi")

async def delete_tests(call:CallbackQuery,state:FSMContext):
    ids=call.data.split("_")[1]
    test_delete(int(ids))
    await call.message.edit_text("Test o'chirildi\nTest idsini yuboring")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(add_tests, state=home.home_states, is_admin=True)
    dp.register_message_handler(info_tests, state=tests.delete_states, is_admin=True)
    dp.register_callback_query_handler(delete_tests,Text(startswith=("del")),state=tests.delete_states,is_admin=True)
    dp.register_message_handler(cancel_test,Text(equals=("Bekor qilish")), state=tests, is_admin=True)
    dp.register_message_handler(test_title, state=tests.test_states, is_admin=True)
    dp.register_message_handler(next_step, state=tests.photo_states, is_admin=True)
    dp.register_message_handler(test_photo,content_types=['photo'], state=tests.photo_states, is_admin=True)
    dp.register_message_handler(correct_answer, state=tests.answer_states, is_admin=True)
    dp.register_callback_query_handler(check_test,Text(startswith=("check")),state=tests.check_states,is_admin=True)
