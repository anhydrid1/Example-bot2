from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from user import Reg

import Keyboards.keyboard as kb
import database.requests as rq
from middlewares import TestMiddleware

basic_router = Router()

basic_router.message.outer_middleware(TestMiddleware())


@basic_router.message(Command('start'))
async def cmd_start(message: types.Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в магазин кроссовок!',
            reply_markup=kb.main)


@basic_router.callback_query(F.data == 'help')
async def cmd_help(callback: CallbackQuery):
    await callback.answer('Вы выбрали помощь')

    text = ('- <b>Список доступных комманд</b> -\n\n'
            '<b>/start</b> - <i>начало работы с ботом</i>\n'
            '<b>/send_photo</b> - <i>отправить тестовое фото</i>\n'
            '<b>/send_doc</b> - <i>отправить тестовый документ</i>\n'
            '<b>/card</b> - <i>получить персональную открытку</i>\n'
            '<b>/cars</b> - <i>список авто</i>\n'
            '<b>/reg</b> - <i>регистрация</i>'
            )

    await callback.message.edit_text(text,
                                     parse_mode='HTML',
                                     reply_markup=await kb.inline_cars())

# Регистрация FSM

@basic_router.message(Command('reg'))
async def reg_one(message: types.Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя')

@basic_router.message(Reg.name)
async def reg_two(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона')

@basic_router.message(Reg.number)
async def two_three(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершена\nИмя: {data["name"]}\nНомер: {data["number"]}')
    await state.clear()

########################

@basic_router.message(F.text, lambda message: "дурак" in message.text.lower())
async def rule(message: types.Message):
    await message.answer('Пожалуйста, соблюдайте правила общения.')


@basic_router.message()
async def mes(message: types.Message):
    await message.answer(f"Ваше сообщение: '{message.text}'")