from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile

from app.text import (PRACTICE_START, EDU_TEXT, PRACTICE_AND_TEXT,
                      ACADEM_TEXT, INFRA_TEXT, DEBT_START_TEXT,
                      DEBT_ONE_TEXT, DEBT_TWO_TEXT, DEBT_THREE_TEXT,
                      DEBT_FOUR_TEXT)
from app.keyboards import (practice_main_inline,
                           inline_back_kb, inline_debt_first,
                           inline_debt_sec, inline_debt_three,
                           inline_debt_four, back_to_main)


EDU_PATH = 'media/edu.png'
PRACTICE_PATH = 'media/practice.png'
DEBT_ONE_PATH = 'media/debt_one.png'
DEBT_THREE_PATH = 'media/debt_three.png'
DEBT_FOUR_PATH = 'media/debt_four.png'

practice_router = Router()


@practice_router.message(F.text == 'Учёба, практика и студенческая жизнь')
async def practice_start(message: Message):
    await message.answer(
        text=PRACTICE_START,
        reply_markup=practice_main_inline
    )


@practice_router.callback_query(F.data == 'edu')
async def educatuion(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=EDU_PATH),
        caption=EDU_TEXT,
        reply_markup=inline_back_kb
    )


@practice_router.callback_query(F.data == 'practice')
async def practice(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=PRACTICE_PATH),
        caption=PRACTICE_AND_TEXT,
        reply_markup=inline_back_kb
    )


@practice_router.callback_query(F.data == 'academ')
async def academ(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=ACADEM_TEXT,
        reply_markup=inline_back_kb
    )


@practice_router.callback_query(F.data == 'infra')
async def infra(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=INFRA_TEXT,
        reply_markup=inline_back_kb
    )


@practice_router.callback_query(F.data == 'debt')
async def debt(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=DEBT_START_TEXT,
        reply_markup=inline_debt_first
    )


@practice_router.callback_query(F.data == 'debt_one')
async def debt_one(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=DEBT_ONE_PATH),
        caption=DEBT_ONE_TEXT,
        reply_markup=inline_debt_sec
    )


@practice_router.callback_query(F.data == 'debt_two')
async def debt_two(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=DEBT_TWO_TEXT,
        reply_markup=inline_debt_three
    )


@practice_router.callback_query(F.data == 'debt_three')
async def debt_three(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=DEBT_THREE_PATH),
        caption=DEBT_THREE_TEXT,
        reply_markup=inline_debt_four
    )


@practice_router.callback_query(F.data == 'debt_four')
async def debt_four(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=DEBT_FOUR_PATH),
        caption=DEBT_FOUR_TEXT,
        reply_markup=back_to_main
    )
