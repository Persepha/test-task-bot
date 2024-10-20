from telegram import Update
from telegram.ext import ContextTypes

from tasks_ptb.services.task import delete_task_by_id


async def delete_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    try:
        task_id = int("".join(context.args))
    except Exception as e:
        print(e)
        await update.message.reply_text("Некорректный ID задачи")
        return

    await delete_task_by_id(task_id)
    await update.message.reply_text(f"Задача с ID {task_id} успешно удалена")
