from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile

from app.text import (ADMISSION, ADMISSION_FIRST, ADMISSION_SECOND,
                      ADMISSION_THIRD, START_TEXT)
from app.keyboards import (inline_admission_first,
                           inline_admission_sec,
                           inline_admission_third,
                           main_keyboard,
                           back_to_main)


START_PHOTO = 'media/start.png'


admission_router = Router()


@admission_router.message(
    F.text == 'Поступление: шаг за шагом'
)
async def introduction(message: Message):

    await message.answer(
        text=ADMISSION,
        reply_markup=inline_admission_first
    )


@admission_router.callback_query(
    F.data == 'first_step'
)
async def first_step(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=ADMISSION_FIRST,
        reply_markup=inline_admission_sec
    )


@admission_router.callback_query(
    F.data == 'second_step'
)
async def second_step(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=ADMISSION_SECOND,
        reply_markup=inline_admission_third
    )


@admission_router.callback_query(
    F.data == 'third_step'
)
async def third_step(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=ADMISSION_THIRD,
        reply_markup=back_to_main
    )


@admission_router.callback_query(
    F.data == 'main_menu'
)
async def back_to_menu(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo=FSInputFile(path=START_PHOTO),
        caption=START_TEXT,
        reply_markup=main_keyboard
    )
