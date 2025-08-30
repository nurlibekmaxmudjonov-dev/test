import asyncio
import random
import datetime
import uuid
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from PIL import Image, ImageDraw, ImageFont

TOKEN = "7615889631:AAHMhlpRiv8YnFDbctE9aC_-ka5yg_V7nSU"
ADMIN_ID = 123456789

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()
dp.include_router(router)

class Komunal(StatesGroup):
    xizmat = State()
    summa = State()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ℹ️ Bot haqida"), KeyboardButton(text="📚 Yordam")],
        [KeyboardButton(text="🎲 Random son"), KeyboardButton(text="🔤 Random so‘z")],
        [KeyboardButton(text="🎲+🔤 Son+So‘z"), KeyboardButton(text="🧮 Kalkulyator")],
        [KeyboardButton(text="❓ Quiz"), KeyboardButton(text="👤 Profilim")],
        [KeyboardButton(text="💡 Komunal to‘lov")],
    ],
    resize_keyboard=True
)

# 🔹 Komunal menyu
komunal_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⚡ Elektr"), KeyboardButton(text="🔥 Gaz")],
        [KeyboardButton(text="💧 Suv"), KeyboardButton(text="🌐 Internet")],
        [KeyboardButton(text="⬅️ Orqaga")],
    ],
    resize_keyboard=True
)

sozlar = ["kitob", "telefon", "kompyuter", "samolyot", "maktab",
          "dastur", "oyna", "qalam", "daftar", "robot","go","abu bot","Nurilsulton","Bekzod","Nurlibek","kichkintoy"]

# 🔹 /start
@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        f"Salom {message.from_user.first_name}! 👋\n"
        "Men mukammal Telegram botman 🚀",
        reply_markup=main_menu
    )

@router.message()
async def main_handler(message: types.Message, state: FSMContext):
    text = message.text

    if text == "ℹ️ Bot haqida":
        await message.answer("Men Python + Aiogram yordamida tuzilgan katta botman ⚡️")

    elif text == "📚 Yordam":
        await message.answer("Savollaringiz bo‘lsa, admin bilan bog‘laning 📩")

    elif text == "🎲 Random son":
        son = random.randint(1, 10)
        await message.answer(f"🎲 Tasodifiy son: {son}")

    elif text == "🔤 Random so‘z":
        soz = random.choice(sozlar)
        await message.answer(f"🔤 Tasodifiy so‘z: {soz}")

    elif text == "🎲+🔤 Son+So‘z":
        son = random.randint(1, 10)
        soz = random.choice(sozlar)
        await message.answer(f"🎲+🔤 Natija: {son}-{soz}")

    elif text == "🧮 Kalkulyator":
        await message.answer("Misol kiriting. Masalan: 12+8 yoki 15/3")

    elif text == "❓ Quiz":
        await bot.send_poll(
            chat_id=message.chat.id,
            question="Python dasturlash tilini kim yaratgan?",
            options=["Bill Gates", "Guido van Rossum", "Elon Musk", "Mark Zuckerberg"],
            type="quiz",
            correct_option_id=1,
            is_anonymous=False
        )

    elif text == "👤 Profilim":
        await message.answer(
            f"🆔 ID: {message.from_user.id}\n"
            f"👤 Ism: {message.from_user.first_name}\n"
            f"📛 Username: @{message.from_user.username if message.from_user.username else 'yo‘q'}"
        )

    elif text == "💡 Komunal to‘lov":
        await message.answer("Qaysi xizmat uchun to‘lov qilmoqchisiz?", reply_markup=komunal_menu)

    elif any(op in text for op in ["+", "-", "*", "/"]):
        try:
            natija = eval(text)
            await message.answer(f"Natija: {natija}")
        except:
            await message.answer("❌ Xato ifoda!")

@router.message(F.text.in_(["⚡ Elektr", "🔥 Gaz", "💧 Suv", "🌐 Internet"]))
async def komunal_xizmat(message: types.Message, state: FSMContext):
    await state.update_data(xizmat=message.text)
    await message.answer(f"{message.text} uchun to‘lov summasini kiriting (so‘mda):")
    await state.set_state(Komunal.summa)

@router.message(F.text == "⬅️ Orqaga")
async def back_to_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Asosiy menyuga qaytdingiz ✅", reply_markup=main_menu)

@router.message(Komunal.summa)
async def komunal_summa(message: types.Message, state: FSMContext):
    try:
        summa = int(message.text)
    except:
        return await message.answer("❌ Faqat raqam kiriting!")

    data = await state.get_data()
    xizmat = data["xizmat"]

    chek_id = str(uuid.uuid4())[:8].upper()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    await message.answer(
        f"✅ To‘lov qabul qilindi!\n\n"
        f"📄 Kvitansiya:\n"
        f"Xizmat: {xizmat}\n"
        f"💰 Summasi: {summa:,} so‘m\n"
        f"🆔 To‘lovchi: {message.from_user.first_name}\n"
        f"🔖 Chek ID: {chek_id}\n"
        f"📅 Sana: {now}",
        reply_markup=main_menu
    )

    img = Image.new("RGB", (600, 400), "white")
    draw = ImageDraw.Draw(img)

    draw.rectangle([(0, 0), (600, 80)], fill=(0, 123, 255))
    draw.text((200, 25), "💵 KOMUNAL TO‘LOV", fill="white", font=ImageFont.load_default())

    draw.rounded_rectangle([(30, 100), (570, 350)], radius=20, outline="black", width=3, fill=(245, 245, 245))

    draw.text((50, 120), f"Xizmat: {xizmat}", fill="black", font=ImageFont.load_default())
    draw.text((50, 150), f"Summasi: {summa:,} so‘m", fill="black", font=ImageFont.load_default())
    draw.text((50, 180), f"To‘lovchi: {message.from_user.first_name}", fill="black", font=ImageFont.load_default())
    draw.text((50, 210), f"User ID: {message.from_user.id}", fill="black", font=ImageFont.load_default())
    draw.text((50, 240), f"Chek ID: {chek_id}", fill="black", font=ImageFont.load_default())
    draw.text((50, 270), f"Sana: {now}", fill="black", font=ImageFont.load_default())

    img.save("kvitansiya.png")
    await message.answer_photo(photo=types.FSInputFile("kvitansiya.png"))
    await state.clear()

async def main():
    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
