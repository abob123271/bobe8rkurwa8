from aiogram import Bot, Dispatcher, types, enums ,  F
from aiogram.filters.command import Command
from dotenv import dotenv_values
import asyncio
from aiogram.client.default import DefaultBotProperties


config = dotenv_values()

bot = Bot(token=config["TOKEN"], default=DefaultBotProperties( parse_mode=enums.ParseMode.HTML))
          

dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("<b>JOPA<b>")

async def main():
    print("DAD!dD")
    await dp.start_polling(bot)

asyncio.run(main())