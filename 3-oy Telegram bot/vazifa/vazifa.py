import asyncio
import random
import ast
import json
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
    Message
)
import aiohttp

TOKEN = "7615889631:AAHMhlpRiv8YnFDbctE9aC_-ka5yg_V7nSU"
ADMIN_ID = 123456789
DB_PATH = "db.json"

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

_db = {"users": {}}

def load_db():
    global _db
    if os.path.exists(DB_PATH):
        try:
            with open(DB_PATH, "r", encoding="utf-8") as f:
                _db = json.load(f)
        except Exception:
            _db = {"users": {}}
    else:
        _db = {"users": {}}

def save_db():
    try:
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(_db, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def get_user(uid: int):
    u = _db["users"].get(str(uid))
    if not u:
        u = {"lang": "uz", "points": 0}
        _db["users"][str(uid)] = u
        save_db()
    return u

SOZLAR = [
    "python", "kompyuter", "dastur", "maktab", "telefon", "robot",
    "samarqand", "toshkent", "algoritm", "matematika", "internet", "kitob", "qalam"
]

def menu_for(uid: int) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="ℹ️ Bot haqida"), KeyboardButton(text="📚 Yordam")],
            [KeyboardButton(text="🎲 Random son"), KeyboardButton(text="🔤 Random so‘z")],
            [KeyboardButton(text="📅 Sana/Soat"), KeyboardButton(text="🎯 Dice (kubik)")],
            [KeyboardButton(text="🐶 It rasmi"), KeyboardButton(text="🐱 Mushuk rasmi")],
        ],
        resize_keyboard=True
    )
    return kb

@dp.message(CommandStart())
async def cmd_start(message: Message):
    get_user(message.from_user.id)
    await message.answer(
        "👋 Salom! Men ko‘p funksiyali botman.\n"
        "Quyidagi menyudan foydalaning:",
        reply_markup=menu_for(message.from_user.id)
    )

@dp.message(F.text == "ℹ️ Bot haqida")
async def bot_info(message: Message):
    await message.answer("🤖 Ushbu bot turli xil o‘yinlar, ensiklopediya, kalkulyator va qiziqarli funksiyalarni o‘z ichiga oladi.")

@dp.message(F.text == "📚 Yordam")
async def bot_help(message: Message):
    await message.answer(
        "📖 Yordam:\n"
        "- 🎲 Random son: 1 dan 100 gacha son chiqaradi\n"
        "- 🔤 Random so‘z: tasodifiy so‘z chiqaradi\n"
        "- 📅 Sana/Soat: hozirgi vaqtni ko‘rsatadi\n"
        "- 🎯 Dice: kubik tashlaydi\n"
        "- 🐶 It rasmi, 🐱 Mushuk rasmi: API’dan surat olib keladi"
    )

@dp.message(F.text == "🎲 Random son")
async def random_number(message: Message):
    num = random.randint(1, 100)
    await message.answer(f"🎲 Sizning random soningiz: {num}")

@dp.message(F.text == "🔤 Random so‘z")
async def random_word(message: Message):
    word = random.choice(SOZLAR)
    await message.answer(f"🔤 Tasodifiy so‘z: {word}")

@dp.message(F.text == "📅 Sana/Soat")
async def date_time(message: Message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await message.answer(f"📅 Bugungi sana va soat:\n{now}")

@dp.message(F.text == "🎯 Dice (kubik)")
async def dice(message: Message):
    await message.answer_dice(emoji="🎲")

async def fetch_dog() -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
            data = await resp.json()
            return data["message"]

async def fetch_cat() -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
            data = await resp.json()
            return data[0]["url"]

@dp.message(F.text == "🐶 It rasmi")
async def dog_image(message: Message):
    url = await fetch_dog()
    await message.answer_photo(url, caption="🐶 Mana sizga tasodifiy it rasmi!")

@dp.message(F.text == "🐱 Mushuk rasmi")
async def cat_image(message: Message):
    url = await fetch_cat()
    await message.answer_photo(url, caption="🐱 Mana sizga tasodifiy mushuk rasmi!")

async def main():
    load_db()
    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
