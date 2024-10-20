import logging
from datetime import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from tasks_ptb.config import logger
from tasks_ptb.db.database import connection
from tasks_ptb.db.models import Task, User
from tasks_ptb.schemas.task_schemas import TaskDTO, UpdateTaskDTO


@connection
async def get_all_tasks(session):
    query = select(Task).order_by(Task.id)
    result = await session.execute(query)

    return result.scalars().all()


@connection
async def create_task(session, task_dto: TaskDTO) -> Optional[Task]:
    try:
        user = await session.scalar(select(User).filter_by(id=task_dto.user_id))
        if not user:
            logger.error(f"User with ID {task_dto.user_id} not found.")
            return None

        data = task_dto.dict()
        new_task = Task(**data)

        session.add(new_task)
        await session.commit()
        logger.info(f"Task for user with ID {task_dto.user_id} successfully added!")
        return new_task
    except SQLAlchemyError as e:
        logger.error(f"Error while adding new task: {e}")
        await session.rollback()


@connection
async def delete_task_by_id(session, task_id: int) -> Optional[Task]:
    try:
        note = await session.get(Task, task_id)
        if not note:
            logger.error(f"Task with ID {task_id} not found.")
            return None

        await session.delete(note)
        await session.commit()
        logger.info(f"Task with ID {task_id} successfully deleted.")
        return note
    except SQLAlchemyError as e:
        logger.error(f"Error while deleting task: {e}")
        await session.rollback()
        return None


@connection
async def update_task_by_id(
    session, task_id: int, update_dto: TaskDTO
) -> Optional[Task]:
    try:
        task = await session.scalar(select(Task).filter_by(id=task_id))

        if not task:
            logger.error(f"Task with ID {task_id} not found.")
            return None

        data = update_dto.dict(exclude_unset=True)

        for field in data:
            if getattr(task, field) != data[field]:
                setattr(task, field, data[field])

        await session.commit()
        logger.info(f"Task with ID {task_id} successfully updated!")
        return task
    except SQLAlchemyError as e:
        logger.error(f"Error while updating task: {e}")
        await session.rollback()
