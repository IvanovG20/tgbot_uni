import os
import asyncio
import logging

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv

from app.facult_handlers import facult_router
from app.admission_handlers import admission_router
from app.pay_handlers import pay_router
from app.practices_handlers import practice_router
from app.contacts_handlers import contacts_router

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


async def main():
    dp.include_routers(
        facult_router,
        admission_router,
        pay_router,
        practice_router,
        contacts_router
        )
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
