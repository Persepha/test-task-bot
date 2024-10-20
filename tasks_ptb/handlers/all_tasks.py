from telegram import Update
from telegram.ext import ContextTypes

from tasks_ptb.handlers.response import send_response
from tasks_ptb.services.task import get_all_tasks
from tasks_ptb.template import render_template


async def all_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task_list = list(await get_all_tasks())
    if not update.message:
        return

    await send_response(
        update,
        context,
        render_template(
            "task_list.j2",
            {"tasks": task_list, "start_index": None},
        ),
    )
