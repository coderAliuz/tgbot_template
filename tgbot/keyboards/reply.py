from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,ReplyKeyboardRemove

def test_kb(but=[]):
    keyboard=ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    keyboard.add(*but).row("Ortga","Asosiy sahifaga")
    return keyboard

def type_kb(args):
    kb=["Bo'lim qo'shish","Testni to'xtatish"]+args
    # kb.append("Asosiy sahifaga")
    keyboard=ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    keyboard.add(*kb).row("Asosiy sahifaga")
    return keyboard
    
test_add_kb=ReplyKeyboardMarkup([
    ["Test qo'shish","Test boshlash"],
    ["Ortga","Asosiy sahifaga"],
],resize_keyboard=True)

home_kb=ReplyKeyboardMarkup([
    ["Test","Qidirish"],
    ["Xabar yuborish",'Bot statistikasi']
],resize_keyboard=True)

##search
search_kb=ReplyKeyboardMarkup([
    ["Test qidirish"],
    ["Foydalanuvchi qidirish"],
    ["Asosiy sahifaga"],
],resize_keyboard=True)

back_kbs=ReplyKeyboardMarkup([
    ["Ortga"],
    ["Asosiy sahifaga"],
],resize_keyboard=True)



#user keyboard
main_kb=ReplyKeyboardMarkup(
    [
        ["Test ishlash"],
        ["Natijalar","Qoidalar"]
    ],resize_keyboard=True)


cancel_kb=ReplyKeyboardMarkup([
    ["Bekor qilish"],
],resize_keyboard=True)

result_kb=ReplyKeyboardMarkup([
    ["Mening natijam"],
    ["Top natijalar"],
    ["Asosiy sahifaga"],
],resize_keyboard=True)