from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery
from tgbot.keyboards import *
from tgbot.misc import *
from tgbot.models import *
from aiogram.dispatcher.filters import Text

import asyncio
import random
from datetime import datetime
from random import randint

async def start_tests(message:Message,state:FSMContext):
    start=check_start_test()
    if start is not None:
        today=datetime.today()
        end_time=datetime(today.year,today.month,today.day,today.hour+1,today.minute)
        tests=get_tests(start[0])[:20]
        await message.answer(f"Test boshlandi!!!\nBoshlanish vaqti:{today.strftime('%H:%M')}\nTugash vaqti:{today.strftime('%H:%M')}",reply_markup=cancel_kb)
        await users_tests.start_states.set()
        test=tests.pop()
        print(test)
        if test:
            title=test[1]
            photo=test[2]
            keys=list(test[3:7])
            correct_answer=keys[0]
            random.shuffle(keys)
            correct_id=keys.index(correct_answer)
            uuid=randint(1,99999)
            alpha=["A","B","C","D"]
            answers=""
            for i in range(4):
                answers+=f"{alpha[i]}. {keys[i]}\n" 
            if photo=="None":
                await message.answer(f"{title}\n{answers}",reply_markup=answer_kb(uuid))
            else:
                await message.answer_photo(photo,caption=f"{title}\n{answers}",reply_markup=answer_kb(uuid))
            await state.update_data(tests=tests)
            await state.update_data(correct_id=correct_id)
            await state.update_data(uuid=uuid)
            await state.update_data(end_time=end_time)
        else:
            await message.reply("Test mavjud emas")
    else:
        await message.answer("Testga start berilmagan")

async def check_answer(call:CallbackQuery,state:FSMContext):
    get_data=await state.get_data()
    tests=get_data['tests']
    c_id=get_data['correct_id']
    end_time=get_data['end_time']
    uuid=get_data['uuid']
    data=call.data.split("_")
    await call.message.delete()
    if int(data[1])==int(uuid):
        answer_id=int(data[3])
        c_num=int(data[2])
        if answer_id==c_id:
            print("to'gri")
            c_num+=1
        else:
            print("notogir")
        
        if end_time>datetime.today() and tests:
            test=tests.pop()
            title=test[1]
            photo=test[2]
            keys=list(test[3:7])
            #############################
            correct_answer=keys[0]
            random.shuffle(keys)
            correct_id=keys.index(correct_answer)
            alpha=["A","B","C","D"]
            answers=""
            for i in range(4):
                answers+=f"{alpha[i]}. {keys[i]}\n" 
            if photo=="None":
                await call.message.answer(f"{title}\n{answers}",reply_markup=answer_kb(uuid,c_num))
            else:
                await call.message.answer_photo(photo,caption=f"{title}\n{answers}",reply_markup=answer_kb(uuid,c_num))
            await state.update_data(tests=tests)
            await state.update_data(correct_id=correct_id)
        else:

            await call.message.answer(f"Test yakunlandi. Sizning natijangiz {c_num}")
            await call.message.answer("Kerakli tugmani tanlang",reply_markup=main_kb)

            await state.finish()
            await home.home_states.set()
    else:
        await call.message.answer("Test yopilgan")

async def cancel_test(message:Message,state:FSMContext):
    await message.reply("Test bekor qilindi")
    await message.answer("Kerakli tugmani tanlang",reply_markup=main_kb)
    await state.finish()
    await home.home_states.set()


def register_tests_start(dp: Dispatcher):
    dp.register_message_handler(start_tests,Text(equals="Test ishlash"),state=home.home_states)
    dp.register_message_handler(cancel_test,Text(equals=("Bekor qilish")), state=users_tests.start_states)
    dp.register_callback_query_handler(check_answer,Text(startswith="answer_"),state=users_tests.start_states)
    