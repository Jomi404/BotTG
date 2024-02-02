from aiogram.filters.command import Command
from aiogram import types
from loader import dp
from filters import IsEditor, IsUser
from aiogram import F

# выбор режима просмотр/редактирование
select_mode = 'Выбрать режим'

# view
see_post = 'Показать последний пост'

# edit
change_text = 'Изменить текст'
change_photo = 'Изменить фото'
change_buttons = 'Изменить кнопки'

# 2
view_post = 'Просмотреть пост'
edit_post = 'Редактировать пост'


@dp.message(IsUser(), Command("commands"))
async def cmd_menu_user(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=see_post),
            types.KeyboardButton(text=select_mode)
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer('Команды', reply_markup=keyboard)


@dp.message(IsEditor(), Command("commands"))
async def cmd_menu_editor(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=change_text),
            types.KeyboardButton(text=change_photo),
            types.KeyboardButton(text=change_buttons),
            types.KeyboardButton(text=select_mode)
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer('Команды', reply_markup=keyboard)


@dp.message(F.text.lower() == select_mode.lower())
async def cmd_select_mode(message: types.Message):
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
    await message.answer('Выберите режим', reply_markup=keyboard)
