from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.text import (PAY_START_TEXT, PAY_GRAPHICS_TEXT,
                      PAY_GRANTS_TEXT)
from app.keyboards import pay_start, inline_back_kb


pay_router = Router()


@pay_router.message(F.text == 'Оплата, скидки и гранты')
async def pay(message: Message):
    await message.answer(
        text=PAY_START_TEXT,
        reply_markup=pay_start
    )


@pay_router.callback_query(F.data == 'graph')
async def graphics(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=PAY_GRAPHICS_TEXT,
        reply_markup=inline_back_kb
    )


@pay_router.callback_query(F.data == 'grants')
async def grants(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(
        text=PAY_GRANTS_TEXT,
        reply_markup=inline_back_kb
    )
