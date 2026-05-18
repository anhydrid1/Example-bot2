from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.types import CallbackQuery
import Keyboards.keyboard as kb
from functions.get_photo_by_name import get_photo
import database.requests as rq

media_router = Router()


@media_router.message(F.photo)
async def photo(message: types.Message):
    text = (
        '<b>Техническая информация о фото:</b>\n\n'
        f'- ID файла:  <code>{message.photo[-1].file_id}</code>\n'
        f'- Ширина:  <i>{message.photo[-1].width} px</i>\n'
        f'- Высота:  <i>{message.photo[-1].height} px</i>'
    )
    await message.answer(text, parse_mode='HTML')


@media_router.message(F.sticker)
async def sticker(message: types.Message):
    await message.answer('Отличный стикер, спасибо!')


@media_router.message(F.audio)
async def audio(message: types.Message):
    await message.answer('Отличный трек! Добавляю в свой плейлист.')


@media_router.callback_query(F.data == 'promo')
async def cmd_promo(callback: CallbackQuery):
    await callback.answer('Вы выбрали акцию')

    promo_image = get_photo('image_photo', 'NikeAirMax.jpg')

    await callback.message.answer_photo(
        photo=promo_image,
        caption='<b>Наша новая акция!</b>',
        parse_mode='HTML'
    )

    text = (
        '<b>- Проведение акции осуществляется с 10.05 по 31.05 2026 года -</b>\n\n'
        'Цена: <s>2000$</s>\n'
        'Цена во время акции: <b>1000$</b>\n\n'
        'Воспользуйтесь акцией прямо сейчас в нашем '
        '<a href="https://www.ozon.ru">магазине</a>'
        )

    await callback.message.answer(text,
                         parse_mode='HTML',
                         reply_markup=await kb.categories())


@media_router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@media_router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\n'
                                  f'Описание: {item_data.description}\n'
                                  f'Цена: {item_data.price}$',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@media_router.message(Command('card'))
async def cmd_card(message: types.Message):
    card_photo = get_photo('image_photo', 'card_p.jpg')

    await message.answer_photo(
        photo=card_photo,
        caption=f'<b>{message.from_user.full_name}</b>, эта открытка специально для вас!\n'
        '<i>Хорошего дня!</i>',
        parse_mode='HTML'
    )


@media_router.message(Command('cars'))
async def cmd_cars(message: types.Message):
    await message.answer('<b>Вот машины на выбор:</b>',
                        parse_mode='HTML',
                        reply_markup=await kb.inline_cars())
