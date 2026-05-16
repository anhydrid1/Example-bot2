from aiogram import types, Router, F
from aiogram.filters.command import Command

import Keyboards.keyboard as kb

basic_router = Router()


@basic_router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}, я - бот!\n'
            'Отправь мне фото, аудио или стикер.',
            reply_markup=kb.main)


@basic_router.message(F.text, lambda message: "дурак" in message.text.lower())
async def rule(message: types.Message):
    await message.answer('Пожалуйста, соблюдайте правила общения.')


@basic_router.message()
async def mes(message: types.Message):
    await message.answer(f"Ваше сообщение: '{message.text}'")