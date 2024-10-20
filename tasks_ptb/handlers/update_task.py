from telegram import Update
from telegram.ext import ContextTypes

from tasks_ptb.handlers.response import send_response
from tasks_ptb.schemas.task_schemas import UpdateTaskDTO
from tasks_ptb.services.task import delete_task_by_id, update_task_by_id
from tasks_ptb.template import render_template


async def update_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user

    try:
        user_input = " ".join(context.args).split(",")
        print(user_input)

        data = {
            "desc": user_input[1],
            "deadline": user_input[2],
            "completed": user_input[3],
        }
        task_id = int(user_input[0])

        task_dto = UpdateTaskDTO(**data)
    except Exception as e:
        print(e)
        await send_response(
            update, context, response=render_template("task_update_incorrect_input.j2")
        )
        return

    created_task = await update_task_by_id(task_id, task_dto)
    await update.message.reply_text("Задача успешно обновлена")
