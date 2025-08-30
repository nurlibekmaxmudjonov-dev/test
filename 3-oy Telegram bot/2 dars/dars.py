import asyncio
from glob import translate

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from deep_translator import GoogleTranslator

BOT_TOKEN = "7615889631:AAG5eMZlSocOQvbkn7WC9k8LiVs3myO9An4"
bot = Bot(BOT_TOKEN)
dp = Dispatcher()



@dp.message(CommandStart())
async def start(messange: types.message):
    return messange.answer(
        "bu telegram bot translete qilib beradi ingiliz tilida biror so'z yozish va uni O'zbek tiliga tarjima qilib beraman 🫠❤️")






@dp.message
async def traslete(message: types.Message):
    text = message.text
    try:
        translator=GoogleTranslator(source='en',target='uz').translate(text)

        await message.answer(f"translated: {translator}")

    except Exception as e:
        await message.answer("tarjima qilib bo'lmaydi")


async def main():
    print("tarjima ishga tushmoqda")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
