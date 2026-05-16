from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.types import CallbackQuery

import Keyboards.keyboard as kb

basic_router = Router()


@basic_router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}, я - бот!\n'
            'Отправь мне фото, аудио или стикер.',
            reply_markup=kb.main)

@basic_router.callback_query(F.data == 'help')
async def cmd_help(callback: CallbackQuery):
    await callback.answer('Вы выбрали помощь')

    text = ('- <b>Список доступных комманд</b> -\n\n'
            '<b>/start</b> - <i>начало работы с ботом</i>\n'
            '<b>/send_photo</b> - <i>отправить тестовое фото</i>\n'
            '<b>/send_doc</b> - <i>отправить тестовый документ</i>\n'
            '<b>/card</b> - <i>получить персональную открытку</i>\n'
            '<b>/cars</b> - <i>список авто</i>'
            )

    await callback.message.answer(text, parse_mode='HTML')
    await callback.message.edit_text('Выберите авто: ',
                                     reply_markup=await kb.inline_cars())

@basic_router.message(F.text, lambda message: "дурак" in message.text.lower())
async def rule(message: types.Message):
    await message.answer('Пожалуйста, соблюдайте правила общения.')


@basic_router.message()
async def mes(message: types.Message):
    await message.answer(f"Ваше сообщение: '{message.text}'")