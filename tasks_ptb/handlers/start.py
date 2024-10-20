from typing import cast

from telegram import Update
from telegram.ext import ContextTypes

from tasks_ptb.db.models import User
from tasks_ptb.handlers.response import send_response
from tasks_ptb.schemas.user_schemas import UserDto
from tasks_ptb.services.user import create_user
from tasks_ptb.template import render_template


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    external_data = {
        "id": user.id,
        "username": user.username,
        "full_name": f"{user.first_name}  {user.last_name}",
    }

    created_user = await create_user(UserDto(**external_data))

    greeting = f"Привет, {user.full_name}! Выбери необходимое действие"
    if created_user is None:
        greeting = f"Привет, новый пользователь! Выбери необходимое действие"

    # await context.bot.send_message(chat_id=update.effective_chat.id, text=greeting)
    await send_response(
        update,
        context,
        render_template(
            "start.j2",
            {"greeting": greeting},
        ),
    )
