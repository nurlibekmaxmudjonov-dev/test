import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = "7615889631:AAHMhlpRiv8YnFDbctE9aC_-ka5yg_V7nSU"  # <-- bu yerga tokeningizni yozing

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

btn1 = KeyboardButton(text="Moshina 🚗")
btn2 = KeyboardButton(text="Tabiat 🏞️")
btn3 = KeyboardButton(text="O'zim haqimda 🤷‍♂️")
btn4 = KeyboardButton(text="Yordam 👍")
btn5 = KeyboardButton(text="Dars 📋")

kb = ReplyKeyboardMarkup(
    keyboard=[
        [btn1, btn2],
        [btn3, btn4, btn5]
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start_hand(message: types.Message):
    await message.answer("Tugmalardan birini tanlang", reply_markup=kb)


@dp.message()
async def answer(message: types.Message):
    if message.text == "Moshina 🚗":
        await message.answer(
            "BMW Group premium avtomobillar va mototsikllarni yetkazib berish bo‘yicha"
            " dunyodagi yetakchi provayder bo‘lib, BMW, MINI, Rolls-Royce va BMW "
            "Motorrad brendlarining uyidir. Bizning transport vositalarimiz "
            "va mahsulotlarimiz mijozlarimizning ehtiyojlariga moslashtirilgan"
            " va doimiy ravishda takomillashtiriladi - barqarorlik va resurslarni "
            "tejashga aniq e'tibor qaratiladi.")

    elif message.text == "Tabiat 🏞️":
        await message.answer("Tabiat — odamning paydo boʻlgunicha ham, odam ishtiroki bilan ham mavjud borliq. Umuman — bu dunyo, odam, koinot; mikromakromega dunyolar; Jonsiz. va jonli narsalar bor. Tor maʼnoda — tabiat fanlari oʻrganadigan obyekt. Tabiat odamga, jamiyatga bogʻliq boʻlmagan qonuniyatga boʻysunadi. Odam tabiatning bir qismi. Odam tabiat qonunlarini oʻzgartira olmaydi, faqat qonunlardan foydalanib, tabiat elementlarini, qismlarini oʻzlashtirishi mumkin. Tabiat tushunchasi insoniyat jamiyati yashashi tabiiy sharoitlarining majmui sifatida ham qaraladi. Inson yashashi uchun mehnat qiladi, mehnat (mas., dehqonchilik, qurilish, sanoat), miya faoliyati va boshqa esa tabiatning baʼzi jihatlarini oʻzgartiradi. Odam tomonidan, yaʼni ijtimoiy mehnat jarayonida yaratiladigan moddiy boyliklar shartli ravishda „ikkinchi tabiat“ deyiladi. Masalan, vodoroddan urangacha boʻlgan 92 ta kimyoviy element"
                             " tabiiydir, undan keyingi kashf etilganlari sunʼiydir. Barcha sunʼiy sintetik kimyoviy birikmalar, odam yaratayotgan atom va yadro energiyalari „ikkinchi tabiat“ga kiradi.")


async def main():
    print("Bugungi darsgi bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
