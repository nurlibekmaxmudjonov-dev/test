import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from datetime import datetime

BOT_TOKEN = "7615889631:AAHMhlpRiv8YnFDbctE9aC_-ka5yg_V7nSU"  # <-- bu yerga tokeningizni yozing

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Qiziqarli faktlar ro‘yxati
facts = [
    "Bugun yangi imkoniyatlar kuni! 🌟",
    "Har kuni yangi narsani o‘rganishga harakat qiling 📚",
    "Tabassum qiling — bugun yaxshi kun bo‘ladi 😄",
    "Kichik qadamlar katta natijaga olib keladi 🚀",
    "Bugun biror yaxshi ish qiling ❤️"
]


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Salom! Men bugungi kun haqida aytadigan botman.\nMenga biror narsa yozing 😊")


@dp.message()
async def today_handler(message: types.Message):
    today = datetime.now()
    sana = today.strftime("%Y-%m-%d")
    hafta_kuni = today.strftime("%A")  # Inglizcha hafta kuni
    # Haftani tarjima qilamiz
    days_uz = {
        "Monday": "Dushanba",
        "Tuesday": "Seshanba",
        "Wednesday": "Chorshanba",
        "Thursday": "Payshanba",
        "Friday": "Juma",
        "Saturday": "Shanba",
        "Sunday": "Yakshanba"
    }
    hafta_uz = days_uz.get(hafta_kuni, hafta_kuni)

    # Tasodifiy fakt tanlaymiz
    import random
    fact = random.choice(facts)

    await message.answer(
        f"📅 Sana: {sana}\n"
        f"📆 Hafta kuni: {hafta_uz}\n"
        f"💡 Qiziqarli fakt: {fact}"
    )


async def main():
    print("Bugungi sana bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())