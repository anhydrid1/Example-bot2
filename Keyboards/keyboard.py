from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton,)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/help')],
    [KeyboardButton(text='/menu'), KeyboardButton(text='/promo')]
],
    resize_keyboard=True
)

main2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дополнительно', url='https://google.com')]
])

cars = ['Toyota', 'Mercedes', 'Ferrari', 'Porsche']

async def reply_cars():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=f'{car}'))
    return keyboard.adjust(2).as_markup()

size = ['Small', 'Middle', 'Big', 'Giant']

async def inline_size():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=f'{size}', url='https://google.com'))
    return keyboard.adjust(2).as_markup()