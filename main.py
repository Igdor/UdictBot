import asyncio
import logging

from config_reader import config

import Commands

from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

Udict_bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(Udict_bot, storage=MemoryStorage())

async def main():

    Commands.register_commands(dp)

    await dp.skip_updates()
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
