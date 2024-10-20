from telegram import Update
from telegram.ext import ContextTypes

from tasks_ptb.handlers.response import send_response
from tasks_ptb.template import render_template


async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, response=render_template("help.j2"))
