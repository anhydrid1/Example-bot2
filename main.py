import asyncio
import logging

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

# Импортируем наш роутер из пакета handlers
from handlers.basic_handlers import basic_router
from handlers.media_handlers import media_router
from handlers.menu_handlers import router

load_dotenv()
TOKEN = getenv('BOT_TOKEN')

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    # Подключаем роутеры к диспетчеру
    dp.include_router(router)
    dp.include_router(media_router)
    dp.include_router(basic_router)

    # Удаляем вебхук и пропускаем накопившиеся входящие сообщения
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
