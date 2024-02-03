import asyncio
import logging
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import CallbackQuery
from aiogram import types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import dp, bot
from data.config import EDITORS

import handlers
from aiogram.types import FSInputFile

view_post = 'Просмотреть пост'
edit_post = 'Редактировать пост'
see_post = 'Показать последний пост'


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=view_post),
            types.KeyboardButton(text=edit_post)
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer('''Привет! 👋

    🤖 Я бот по созданию карточек товаров любой категории.

    🛍️ Чтобы просмотреть доступные возможности возпользуйтесь командой /commands.

    ❓ Возникли вопросы? Не проблема! Команда /help поможет 
    разобраться с базовыми вопросами, которые возникают при работе с ботом.
    
    Тут вы можете выбрать режим:''', reply_markup=keyboard)


@dp.message(F.text.lower() == view_post.lower())
async def view_mode(message: types.Message):
    cid = message.chat.id
    if cid in EDITORS:
        EDITORS.remove(cid)
    await message.answer("Вы вошли в режим просмотра поста, введите /commands чтобы просмотреть доступные вам команды",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == edit_post.lower())
async def edit_mode(message: types.Message):
    cid = message.chat.id
    if cid not in EDITORS:
        EDITORS.append(cid)
    await message.answer("Вы вошли в режим редактирование поста, введите /commands чтобы просмотреть доступные вам "
                         "команды", reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == see_post.lower())
async def upload_photo_post(message: Message):
    buttons = [
        [types.InlineKeyboardButton(text="Panda", url='https://www.youtube.com/watch?v=hAOoMtRstJ8', callback_data="default_panda")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    photo = types.FSInputFile('./resources/default.jpg')
    await message.answer(text='Ваш пост выглядит так:')
    await bot.send_photo(message.chat.id, photo, reply_markup=keyboard)



async def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(name)s'
                                                   '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    # db.create_tables()
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
