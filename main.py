from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart

bot = Bot(token='7436824817:AAE6g7Ecj-B0HVWT58t_VefKFDMibk4BfMU')
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("hello")

@dp.startup()
async def startup():
    print("Bot is starting up...")

async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())