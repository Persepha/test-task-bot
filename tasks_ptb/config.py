import logging
from pathlib import Path

from decouple import config

TELEGRAM_BOT_TOKEN = config("TOKEN")

SQLALCHEMY_DATABASE_URI = "sqlite+aiosqlite:///db.sqlite3"

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

logger = logging.getLogger(__name__)
