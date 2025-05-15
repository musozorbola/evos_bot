import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, InlineKeyboardMarkup
from database import database
from keyboards import start_buttons
router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    full_name = f"{message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else ''}"
    lang = database.get_user_lang(message.from_user.id)
    user = database.get_user(message.from_user.id)
    if not user:
        database.insert_user(first_name=message.from_user.first_name,
                             last_name=message.from_user.last_name,
                             telegram_id=message.from_user.id)
    await message.answer_photo(caption=f"{full_name}", photo=img, reply_markup=start_buttons(lang))
