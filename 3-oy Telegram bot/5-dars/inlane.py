import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "7615889631:AAHMhlpRiv8YnFDbctE9aC_-ka5yg_V7nSU"  # <-- bu yerga tokeningizni yozing

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

btn1 = InlineKeyboardButton(text="Google", url="https://www.google.com/?hl=ru")
btn2 = InlineKeyboardButton(text="YouTube", url="https://youtube.com")
btn3 = InlineKeyboardButton(text="Salom", callback_data="Hello")
btn4 = InlineKeyboardButton(text="Xayr", callback_data="bye")

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [btn1, btn2],
    [btn3, btn4]
])


@router.message()
async def start_hand(message: types.Message):
    await message.answer("Quyidagi tugmalardan birini tanlang", reply_markup=inline_kb)


dp.include_router(router)


async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
