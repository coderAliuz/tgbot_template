from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher.filters import Text
from tgbot.misc import *
from tgbot.keyboards import *
from tgbot.models import *
from datetime import datetime


async def start_tests(message:Message,state:FSMContext):
    check=check_start_test()
    data=await state.get_data()
    types=data['types']
    if check is not None:
        await message.reply(f"{check[0]} bo'limidagi testga start berilgan.\nTestni to'xtatib qayta start bering",reply_markup=type_kb(select_all_type()))
        await tests.type_states.set()
    else:
        update_start_test(types)
        await message.reply(f"{types} bo'limi testiga start berildi!")

async def add_tests(message:Message,state=FSMContext):
    await message.answer("Test mazmunini kiriting",reply_markup=test_kb([]))
    await tests.test_states.set()


async def test_title(message:Message,state:FSMContext):
    title=message.text
    await message.reply("Testni rasm bo'lsa, rasm yuboring aks holda o'tkazib yuboring",
                        reply_markup=test_kb(["O'tkazib yuborish"]))
    await state.update_data(title=title)
    await state.update_data(answer=[])
    await state.update_data(photo="None")
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
    await state.update_data(answer=answer)
    if len(answer)==4:
        title=answer_data['title']
        testlar='\n '.join(answer)
        photo=answer_data['photo']
        ids=get_test_id()
        if photo=="None":
            await message.answer(f"#id{ids}\n{title}\n {testlar}\n\nTestni tasdiqlaysizmi",reply_markup=test_kb(but=["Yo'q","Ha"]))
        else:
            await message.answer_photo(photo,caption=f"id{ids}\n{title}\n {testlar}\n\nTestni tasdiqlaysizmi",reply_markup=test_kb(but=["Yo'q","Ha"]))
        await tests.next()
    else:
        await message.answer("Noto'g'ri javobni kiriting")

async def check_test(message:Message,state:FSMContext):
    check=message.text
    if check=="Ha":
        ids=test_add(title, photo, answer,types, str(datetime.today()))
        await message.reply("Test qabul qilindi\nKerakli tugmani tanlang",reply_markup=test_add_kb)
    elif check=="Yo'q":
        await message.reply("Test qabul qilinmadi\nKerakli tugmani tanlang",reply_markup=test_add_kb)    
    await state.finish()
    await tests.test_add_state.set()

async def to_home(message:Message,state:FSMContext):
    await state.finish()
    await message.answer("Siz asosiy sahifadasiz\nKerakli tugmani tanlang",reply_markup=home_kb)
    await home.home_states.set()
    
def register_tests(dp: Dispatcher):
    dp.register_message_handler(start_tests, text="Test boshlash",state=tests.test_add_state, is_admin=True)
    dp.register_message_handler(add_tests, text="Test qo'shish",state=tests.test_add_state, is_admin=True)
    dp.register_message_handler(test_title, state=tests.test_states, is_admin=True)
    dp.register_message_handler(add_tests,text="Ortga",state=tests, is_admin=True)
    dp.register_message_handler(next_step,text="O'tkazib yuborish", state=tests.photo_states, is_admin=True)
    dp.register_message_handler(test_photo,content_types=['photo'], state=tests.photo_states, is_admin=True)
    dp.register_message_handler(correct_answer, state=tests.answer_states, is_admin=True)
    dp.register_message_handler(check_test,text=["Ha","Yo'q"],state=tests.check_states,is_admin=True)

