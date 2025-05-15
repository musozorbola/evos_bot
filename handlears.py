import os

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile

from database import database
from keyboards import select_language, start_buttons
from messages import messages

router = Router()


@router.message(F.text == "🏢 Kampaniya haqida")
async def handle_message(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    await message.answer_photo(photo=img, caption="Evos judayam shirin kompaniya")

@router.message(F.text == "Filialari")
async def handle_message(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    await message.answer_photo(photo=img, caption="Evos Filiali toshkentda 83")

@router.message(F.text == "Bo'sh ish o'rinlari")
async def handle_message(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    await message.answer_photo(photo=img, caption="")

@router.message(F.text == "Menyu")
async def handle_message(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    await message.answer_photo(photo=img, caption="menyu judayam shirin")

@router.message(F.text == "Yangiliklar")
async def handle_message(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    await message.answer_photo(photo=img, caption="Yangiliklar judaxam kop")

@router.message(F.text == "Kantaktlar/Manzil")
async def handle_message(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    await message.answer_photo(photo=img, caption="Kantaktlar/Manzil toshken varavskoy")

@router.message(F.text.in_(["🇺🇿/🇷🇺 Til", "🇺🇿/🇷🇺 Язык"]))
async def get_language(message: Message):
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(messages[lang]['select_lang'], reply_markup=select_language())

@router.callback_query(F.data.in_(["uz", "ru"]))
async def set_language(callback_query: CallbackQuery):
    lang = callback_query.data
    database.set_user_lang(telegram_id=callback_query.from_user.id, lang=lang)
    await callback_query.message.answer(text='Salom', reply_markup=start_buttons(lang))

