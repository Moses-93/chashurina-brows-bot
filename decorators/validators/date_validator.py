from datetime import datetime, time
import re
from db.db_reader import GetFreeDate
from utils.format_datetime import NowDatetime, FormatDate
from aiogram.types import Message
import logging

logger = logging.getLogger(__name__)


def validator_date(fucn):
    async def wrapper(message: Message, *args, **kwargs):
        logger.info(
            f"DATE(in validator_date 1): {message.text} | type: {type(message.text)}"
        )
        date = message.text
        if not re.match(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", date):
            await message.answer(
                "Дата повинна бути у форматі YYYY-MM-DD. \nПриклад: 1900-01-01."
            )
            return

        date = FormatDate().formats_date_str_to_datetime(date).date()
        logger.info(f"DATE(in validator_date 2): {date} | type: {type(date)}")
        if date < NowDatetime().now_datetime().date():
            await message.answer(
                "Дата повинна бути більшою або дорівнювати поточній даті. \nСпробуйте ще раз."
            )
            return

        existing_date = await GetFreeDate(date=date).get_date
        if existing_date:
            await message.answer(text=f"Дата - {date} вже є в списку")
            return
        date = datetime.combine(date, time(18, 0))
        logger.info(f"DATE(in validator_date 3): {date} | type: {type(date)}")
        await fucn(message, date, *args, **kwargs)
        return

    return wrapper
