import logging
from os import getenv
from dotenv import load_dotenv

import asyncio
import aiogram
from aiogram import Bot, Dispatcher, html
from aiogram.types import Message
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties

###################

startReplyMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Create profile"), KeyboardButton(text="Info")]
            ]
        )

###################

load_dotenv()

logger = logging.getLogger(__name__)
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def startReaction(msg: Message):
    await msg.answer(f'Hello, {html.bold(msg.from_user.full_name)}', reply_markup=startReplyMarkup)
    logger.info("start command has been received")

async def main():
    logging.basicConfig(filename="main.log", level=logging.INFO)
    logger.info(f"{"-"*30} Start {"-"*30}")

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
