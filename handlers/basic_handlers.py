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


@basic_router.callback_query(F.data == 'help')
async def help_cmd(callback: CallbackQuery):
    await callback.answer('Вы открыли список команд', show_alert=True)
    await callback.message.edit_text('Ghbdtn', reply_markup=await inline_cars())

@basic_router.message(F.text, lambda message: "дурак" in message.text.lower())
async def rule(message: types.Message):
    await message.answer('Пожалуйста, соблюдайте правила общения.')


@basic_router.message()
async def mes(message: types.Message):
    await message.answer(f"Ваше сообщение: '{message.text}'")

