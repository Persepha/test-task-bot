import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from tasks_ptb import handlers
from tasks_ptb.config import TELEGRAM_BOT_TOKEN
from tasks_ptb.db.database import Base, engine

COMMAND_HANDLERS = {
    "start": handlers.start,
    "help": handlers.help_,
    "tasks": handlers.all_tasks,
    "add": handlers.add_task,
    "del": handlers.delete_task,
    "upd": handlers.update_task,
}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="bot.log",
)


if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN wasn't implemented in .env")


if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))

    application.run_polling()
