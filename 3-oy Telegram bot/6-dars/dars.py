import asyncio
from email.policy import default
from itertools import dropwhile

from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, )
from aiogram import Bot, Dispatcher, types

TOKEN = "7615889631:AAHMhlpRiv8YnFDbctE9aC_-ka5yg_V7nSU"
bot = Bot(token=TOKEN)
dp = Dispatcher()
# bu oddi reply buton
reply_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Yangiliklar"), KeyboardButton(text="Ma'lumot")],
    [KeyboardButton(text="Aloqa "), KeyboardButton(text="Test")],
])

# inline keyboard
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Google", url="https://google.com")],
    [InlineKeyboardButton(text="You Tube", url="https://www.youtube.com/")],
    [InlineKeyboardButton(text="Twitter", url="https://x.com/")],
    [InlineKeyboardButton(text="Telegram", url="https://t.me//@mee_Roxila")]


])

o = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="yoshim : 12", url="https://google.com")],
    [InlineKeyboardButton(text="ismim : Nurlibek", url="https://google.com")]
])

m = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="99-999-99-99", url="https://google.com")]
])
s = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Quyidagi test", url="https://google.com")]
])
@dp.message()
async def main_hand(meesage: types.Message):
    if meesage.text == "/start":
        await meesage.answer("tugmalardan birini tanlang",reply_markup=reply_kb)

    elif meesage.text == "Yangiliklar":
        await meesage.answer("Tgmalardan birini tanlang", reply_markup=inline_kb)
    elif meesage.text == "Ma'lumot":
        await meesage.answer("O'zim haqimda malumotlar", reply_markup=o)
    elif meesage.text == "Aloqa":
        await meesage.answer("Biz bilan bog'laning", reply_markup=m)
    elif meesage.text == "Test":
        await meesage.answer("Bilimingizni sinab ko'ring", reply_markup=s)

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

