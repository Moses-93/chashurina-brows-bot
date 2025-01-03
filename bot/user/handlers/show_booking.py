from aiogram import Router
import logging
from aiogram.types import CallbackQuery
from bot.user.keyboards.cancellation_keyboard import (
    cancel_booking_button,
)
from db.db_reader import get_notes
from utils.formatted_view import ViewController
from utils.message_templates import template_manager

logger = logging.getLogger(__name__)
show_booking_router = Router()


@show_booking_router.callback_query(lambda c: c.data == "all_notes")
async def show_all_notes(callback: CallbackQuery, user_id):
    logger.info(f"Користувач з ID: {user_id} переглядає всі записи")

    notes = await get_notes.get_notes(user_id=user_id)
    if notes:
        formatted_notes = ViewController(notes=notes, view_type="all").get()
        await callback.message.answer(text=formatted_notes, parse_mode="Markdown")
        await callback.answer()
        return

    msg = template_manager.booking_not_found()
    await callback.message.answer(text=msg)
    await callback.answer()


@show_booking_router.callback_query(lambda c: c.data == "active_notes")
async def show_active_notes(callback: CallbackQuery, user_id):
    logger.info(f"Користувач з ID: {user_id} переглядає активні записи")

    active_notes = await get_notes.get_notes(active=True, user_id=user_id)
    if active_notes:
        cancel = await cancel_booking_button(active_notes)
        formatted_notes = ViewController(notes=active_notes, view_type="active").get()
        await callback.message.answer(
            text=f"{formatted_notes}", reply_markup=cancel, parse_mode="Markdown"
        )
        await callback.answer()
        return

    msg = template_manager.booking_not_found()
    await callback.message.answer(text=msg)
    await callback.answer()
