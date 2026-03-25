import logging
from os import getenv
from dotenv import load_dotenv

import asyncio
import aiogram
from aiogram import Bot, Dispatcher, html
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties

load_dotenv()

logger = logging.getLogger(__name__)
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def startReaction(msg: Message):
    await msg.answer(f'Hello, {html.bold(msg.from_user.full_name)}')

async def main():
    logging.basicConfig(filename="main.log", level=logging.INFO)
    logger.info("Log started")

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
