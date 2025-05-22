from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery

from app.text import (START_TEXT, FACULT_TEXT, AD_TEXT, TOUR_TEXT,
                      HOTEL_TEXT, SERVICE_TEXT, DOUBLE_AD_TEXT)
from app.keyboards import (main_keyboard, facult_inline_kb,
                           inline_back_kb)


START_PHOTO = 'media/start.png'
FACULT_PHOTO = 'media/facult.png'
AD_PHOTO = 'media/ad.png'
TOUR_PHOTO = 'media/tour.png'
HOTEL_PHOTO = 'media/hotel.png'
SERVICE_PHOTO = 'media/service.png'
DOUBLE_AD_PHOTO = 'media/double_ad.png'

facult_router = Router()


@facult_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(
        photo=FSInputFile(path=START_PHOTO),
        caption=START_TEXT,
        reply_markup=main_keyboard
    )


@facult_router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.delete()


@facult_router.message(F.text == 'Факультет и программы обучения')
async def about_faculty(message: Message):
    await message.answer_photo(
        photo=FSInputFile(path=FACULT_PHOTO),
        caption=FACULT_TEXT,
        reply_markup=facult_inline_kb
    )


@facult_router.callback_query(F.data == 'ad')
async def ad(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=AD_PHOTO),
        caption=AD_TEXT,
        reply_markup=inline_back_kb
    )


@facult_router.callback_query(F.data == 'tour')
async def tour(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=TOUR_PHOTO),
        caption=TOUR_TEXT,
        reply_markup=inline_back_kb
    )


@facult_router.callback_query(F.data == 'hotel')
async def hotel(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=HOTEL_PHOTO),
        caption=HOTEL_TEXT,
        reply_markup=inline_back_kb
    )


@facult_router.callback_query(F.data == 'service')
async def service(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=SERVICE_PHOTO),
        caption=SERVICE_TEXT,
        reply_markup=inline_back_kb
    )


@facult_router.callback_query(F.data == 'double_ad')
async def double_ad(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=DOUBLE_AD_PHOTO),
        caption=DOUBLE_AD_TEXT,
        reply_markup=inline_back_kb
    )
