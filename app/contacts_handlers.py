from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile


from app.text import CONTACTS_TEXT, DOCS_TEXT, QUESTIONS_TEXT
from app.keyboards import inline_contacts, inline_back_kb


DOCS_PATH = 'media/docs.png'

contacts_router = Router()


@contacts_router.message(F.text == 'Контакты и часто задаваемые вопросы')
async def practice_start(message: Message):
    await message.answer(
        text=CONTACTS_TEXT,
        reply_markup=inline_contacts
    )


@contacts_router.callback_query(F.data == 'docs')
async def docs(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=DOCS_PATH),
        caption=DOCS_TEXT,
        reply_markup=inline_back_kb
    )


@contacts_router.callback_query(F.data == 'questions')
async def questions(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=QUESTIONS_TEXT,
        reply_markup=inline_back_kb
    )
