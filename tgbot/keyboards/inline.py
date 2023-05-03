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