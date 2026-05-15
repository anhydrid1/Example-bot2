from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/help')],
    [KeyboardButton(text='/menu'), KeyboardButton(text='/promo')]
],
    resize_keyboard=True
)
