from aiogram.filters import BaseFilter
from aiogram.types import Message
from data.config import EDITORS


class IsEditor(BaseFilter):

    async def __call__(self, message: Message):
        return message.from_user.id in EDITORS
