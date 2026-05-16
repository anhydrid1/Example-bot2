from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Помощь', callback_data='help')],
    [InlineKeyboardButton(text='Меню', callback_data='menu')],
    [InlineKeyboardButton(text='Акция', callback_data='promo')]
])

cars = ['Toyota', 'Mercedes', 'Ferrari', 'Porsche']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=f'{car}'))
    return keyboard.adjust(2).as_markup()

size = ['Small', 'Middle', 'Big', 'Giant']

async def inline_size():
    keyboard = InlineKeyboardBuilder()
    for size_s in size:
        keyboard.add(InlineKeyboardButton(text=f'{size_s}', url='https://google.com'))
    return keyboard.adjust(2).as_markup()
