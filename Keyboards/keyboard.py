from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.requests import get_categories, get_category_item

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Помощь', callback_data='help')],
    [InlineKeyboardButton(text='Меню', callback_data='menu')],
    [InlineKeyboardButton(text='Акция', callback_data='promo')]
])

cars = ['Toyota', 'Mercedes', 'Ferrari', 'Porsche']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=f'{car}', url='https://google.com'))
    return keyboard.adjust(2).as_markup()

async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()
