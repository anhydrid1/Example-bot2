from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)



main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/help')],
    [KeyboardButton(text='/menu'), KeyboardButton(text='/promo')]
],
    resize_keyboard=True
)

main2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дополнительно', url='https://google.com')]
])