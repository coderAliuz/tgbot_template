from aiogram import Dispatcher
from aiogram.types import Message,CallbackQuery
from tgbot.models import *
from tgbot.misc import *
from tgbot.keyboards import result_kb,main_kb


async def result_main(message:Message):
    await message.answer("Kerakli tugmani tanlang",reply_markup=result_kb)
    await home.result_states.set()

async def user_result(message:Message):
    info=result_info(message.chat.id)
    text=f"{info[0]}\nNatija: {info[1]}"
    print(type(info[1]))
    if info[1]==0:
        await message.answer(f"{text}\nHali test ishlanmagan.")
    elif info[2] is not None:
        await message.answer_photo(info[2],caption=f"{text}\nVaqt: {info[3]}\nSertifikat tasdiqlandi!")
    else:
        await message.answer(f"{text}\nVaqt: {info[3]}\nSertifikat tasdiqlanmadi!")

async def all_users_result(message:Message):
    tops=top_results()
    info=""
    for top in range(len(tops)):
        info+=f"{top+1}.{tops[top][0]}-{tops[top][1]} ta\n"
    await message.reply(info)

async def ret_home(message:Message):
    await message.answer("Kerakli tugmani tanlang",reply_markup=main_kb)
    await home.home_states.set()

def register_results(dp:Dispatcher):
    dp.register_message_handler(result_main,text="Natijalar",state=home.home_states)
    dp.register_message_handler(user_result,text="Mening natijam",state=home.result_states)
    dp.register_message_handler(all_users_result,text="Top natijalar",state=home.result_states)
    dp.register_message_handler(ret_home,text="Asosiy sahifaga",state=home.result_states)
    


