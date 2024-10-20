import telegram
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from tasks_ptb.handlers.response import send_response
from tasks_ptb.schemas.task_schemas import TaskDTO
from tasks_ptb.services.task import create_task
from tasks_ptb.template import render_template


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user

    try:
        user_input = " ".join(context.args).split(",")
        print(user_input)

        data = {
            "user_id": user.id,
            "desc": user_input[0],
            "deadline": user_input[1],
            "completed": user_input[2],
        }
        print(data)
        task_dto = TaskDTO(**data)
    except Exception as e:
        print(e)
        await send_response(
            update, context, response=render_template("task_incorrect_input.j2")
        )
        return

    created_task = await create_task(task_dto)
    await update.message.reply_text("Задача успешно добавлена")
