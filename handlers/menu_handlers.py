from aiogram import types, Router
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

from functions.get_photo_by_name import get_photo

router = Router()


@router.message(Command('menu'))
async def cmd_menu(message: types.Message):
    text = (
        '<b>Меню возможностей:</b>\n\n'   
        '<i>Этот бот демонстрирует:</i>\n'
        ' - Отправку форматированного текста\n'
        ' - Отправку изображений и документов\n\n'
        'Воспользуйтесь командой /send_photo, чтобы получить картинку.\n'
        'Воспользуйтесь командой /send_doc, чтобы получить документ.\n\n'
        'Больше информации о фреймворке вы найдёте в '
        "<a href='https://aiogram.dev/'>документации aiogram 3</a>."

    )

    await message.answer(text, parse_mode='HTML')


@router.message(Command('send_photo'))
async def send_photo_cmd(message: types.Message):
    image_from_pc = get_photo('image_photo', 'cat.jpg')

    await message.answer_photo(
        photo=image_from_pc,
        caption="<b>Вот ваш котик!</b>  ᓚᘏᗢ\n\n"
                "<em>Этот котик был загружен с ПК.</em>",
        parse_mode='HTML'
    )


@router.message(Command('send_doc'))
async def cmd_send_doc(message: types.Message):
    document_test = FSInputFile('document.txt')

    await message.answer_document(
        document=document_test,
        caption="<i>Вот ваш документ</i>",
        parse_mode='HTML'
    )
