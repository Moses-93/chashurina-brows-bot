import logging
from user_data import set_user_data
from aiogram.types import Message, CallbackQuery

logger = logging.getLogger(__name__)

def set_username(func):
    async def wrapper(event: Message|CallbackQuery, *args, **kwargs):
        name = event.from_user.first_name
        username = event.from_user.username
        user_id = event.from_user.id
        logger.info(f"User ID: {user_id}, Username: {username}")

        set_user_data(user_id, name=name, username=username)
        return await func(event, *args, **kwargs)
    
    return wrapper
