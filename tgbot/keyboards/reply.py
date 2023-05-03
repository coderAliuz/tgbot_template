from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,ReplyKeyboardRemove

def test_kb(*args):
    if args:
        kb=[list(args),["Bekor qilish"]]
    else:
        kb=[["Bekor qilish"]]
    keyboard=ReplyKeyboardMarkup(kb,row_width=1,resize_keyboard=True)
    return keyboard

home_kb=ReplyKeyboardMarkup([
    ["Test qo'shish","Qidirish"],
    ["Xabar yuborish",'Bot statistikasi']
],row_width=2,resize_keyboard=True)

beck_kb=ReplyKeyboardMarkup([
    ["Asosiy sahifaga"],
],row_width=1,resize_keyboard=True)

