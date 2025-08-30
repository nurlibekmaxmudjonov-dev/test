import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

BOT_TOKEN = "7615889631:AAG5eMZlSocOQvbkn7WC9k8LiVs3myO9An4"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_hendlar(m: types.Message):
    await m.answer(f"Salom  yaxshimisiz {m.from_user.first_name} 👍")


@dp.message()
async def salom_handler(m: types.Message):
    if m.text.lower() in ['salom', 'hi', 'hello']:
        await m.answer("Assalomu alaykum")
    elif m.text.lower() in ['bye', "i'm off"]:
        await m.answer("Hayr ko'rishguncha")
    else:
        await m.answer("Man faqat salom deyishni bilaman")


async def main():
    print("Bot ishga tushdi .... ")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
