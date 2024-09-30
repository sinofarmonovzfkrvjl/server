from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart

bot = Bot(token='7596605488:AAHUBAtgxNIjRWzNW1-J79LCp2NcJVHyRzA')
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("hello")

@dp.startup()
async def startup():
    print("Bot is starting up...")

async def main():
    await dp.start_polling(bot)
