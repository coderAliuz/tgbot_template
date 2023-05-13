from aiogram.types.inline_keyboard import InlineKeyboardButton,InlineKeyboardMarkup

chekcout=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Yo'q",callback_data="check_no"),
        InlineKeyboardButton("Ha",callback_data="check_yes")
        ]
    ],
    row_width=2
)
def delete_inline_kb(ids):
    delete_kb=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Testni o'chirish",callback_data=f"del_{ids}"),
            ]
        ],
        row_width=1
    )
    return delete_kb


def answer_kb(uuid,i=0):
    kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("A",callback_data=f"answer_{uuid}_{i}_0"),
            InlineKeyboardButton("B",callback_data=f"answer_{uuid}_{i}_1")
        ],
        [
            InlineKeyboardButton("C",callback_data=f"answer_{uuid}_{i}_2"),
            InlineKeyboardButton("D",callback_data=f"answer_{uuid}_{i}_3")
        ]
    ],
    row_width=2)
    return kb