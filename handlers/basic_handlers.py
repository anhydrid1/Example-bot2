from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.types import CallbackQuery

import Keyboards.keyboard as kb
from Keyboards.keyboard import inline_cars

basic_router = Router()


@basic_router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}, я - бот!\n'
            'Отправь мне фото, аудио или стикер.',
            reply_markup=kb.main)


@basic_router.message(Command('help'))
async def cmd_help(message: types.Message):
    text = (
        '<b>Справка по командам бота:</b>\n\n'
        '<b>/start</b> - <i>начало работы с ботом</i>\n'
        '<b>/help</b> - <i>показать это сообщение</i>\n'
        '<b>/send_photo</b> - <i>прислать тестовую картинку</i>\n'
        '<b>/send_doc</b> - <i>прислать тестовый документ</i>\n'
        '<b>/menu</b> - <i>показать меню возможностей</i>\n'
        '<b>/promo</b> - <i>получить акцию</i>\n'
        '<b>/card</b> - <i>получить открытку</i>\n'
        '<b>/cars</b> - <i>список машин</i>'
    )

    await message.answer(text, parse_mode='HTML')

@basic_router.callback_query(F.data == 'help')
async def help_cmd(callback: CallbackQuery):
    text = (
        '<b>Справка по командам бота:</b>\n\n'
        '<b>/start</b> - <i>начало работы с ботом</i>\n'
        '<b>/help</b> - <i>показать это сообщение</i>\n'
        '<b>/send_photo</b> - <i>прислать тестовую картинку</i>\n'
        '<b>/send_doc</b> - <i>прислать тестовый документ</i>\n'
        '<b>/menu</b> - <i>показать меню возможностей</i>\n'
        '<b>/promo</b> - <i>получить акцию</i>\n'
        '<b>/card</b> - <i>получить открытку</i>\n'
        '<b>/cars</b> - <i>список машин</i>'
    )

    await callback.answer('Вы открыли список комманд')
    await callback.message.edit_text(text,
                                     reply_markup=await kb.inline_cars(),
                                     parse_mode='HTML'
                                     )


@basic_router.message(F.text, lambda message: "дурак" in message.text.lower())
async def rule(message: types.Message):
    await message.answer('Пожалуйста, соблюдайте правила общения.')


@basic_router.message()
async def mes(message: types.Message):
    await message.answer(f"Ваше сообщение: '{message.text}'")
