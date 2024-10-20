from datetime import datetime
from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    async_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from tasks_ptb.config import SQLALCHEMY_DATABASE_URI

metadata = MetaData()

engine = create_async_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, echo=True)

async_session_maker = sessionmaker(engine, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    pass


def connection(func):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            return await func(session, *args, **kwargs)

    return wrapper
