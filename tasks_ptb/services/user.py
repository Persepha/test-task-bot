from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from tasks_ptb.config import logger
from tasks_ptb.db.database import connection
from tasks_ptb.db.models import User
from tasks_ptb.schemas.user_schemas import UserDto


@connection
async def create_user(session, user_dto: UserDto) -> Optional[User]:
    try:
        user = await session.scalar(select(User).filter_by(id=user_dto.id))

        if not user:
            data = user_dto.dict()
            new_user = User(**data)

            session.add(new_user)
            await session.commit()
            logger.info(f"Registered user with ID {user_dto.id}!")
            return None
        else:
            logger.info(f"User with ID {user_dto.id} not found!")
            return user
    except SQLAlchemyError as e:
        logger.error(f"Error  while registration: {e}")
        print(e)
        await session.rollback()
