from aiogram import Dispatcher, F
from aiogram.types import Message

from aiogram.filters import Command

from config import CHANNEL_ID
from pyexpat.errors import messages

user_post_state = {}


async def start_command(message:Message):
    await message.answer("Salom, kanalga post yuborsh uchun /post buyrug'ini bosing.")


async def post_command(message:Message):
    user_post_state[message.from_user.id] = True
    await message.answer("Post yuborish uchun tayyormiz.Postni yuborish uchun /post buyrug'ini bosing.")


async def handler_text(message : Message):
    user_id = message.from_user.id
    if user_post_state.get(user_id):
        await message.answer("Post yuboriladi!")
        await message.bot.send_message(CHANNEL_ID,message.text)
        user_post_state[user_id] = False
    else:
        await message.answer("Post yuborish uchun avval /post buyrug'ini bosing.")

def register_post_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command("start"))
    dp.message.register(post_command, Command("post"))
    dp.message.register(handler_text, F.text)