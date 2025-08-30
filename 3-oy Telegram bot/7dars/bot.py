import asyncio
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN
from handlers import register_handlers


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
register_handlers(dp)
async def main ():
    print("Bot started")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())