import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from datetime import datetime
BOT_TOKEN = "7615889631:AAG5eMZlSocOQvbkn7WC9k8LiVs3myO9An4"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_hendlar(m: types.Message):
    await m.answer(f"Salom  yaxshimisiz {m.from_user.first_name} 👍❤️🫠")

@dp.message()
async def data(m : types.Message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await m.answer(f"Bugungi sana va vaqt {now}")


async def main():
    print("Bot ishga tushdi .... ")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
