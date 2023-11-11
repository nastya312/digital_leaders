from datetime import datetime, date as date_dt
from uuid import UUID

from sqlalchemy import select, insert, update, delete

from models.task import Task
from repositories.base import BaseRepository
from schemas.task import TaskCreateUpdate, TaskRead


class TaskRepository(BaseRepository):

    async def _get(self, id: UUID) -> Task:
        stmt = select(Task).where(Task.id == id)
        task = (await self.execute(stmt)).scalars().one()
        return task

    async def _get_all(self) -> Task:
        stmt = select(Task)
        tasks = (await self.execute(stmt)).scalars().all()
        return tasks

    async def _get_by_user_and_created_date(self, user_id: UUID, created_at: date_dt = None) -> list[Task]:
        stmt = select(Task).where(Task.user_id == str(user_id))
        if created_at:
            start = datetime.combine(date=created_at, time=datetime.min.time())
            end = datetime.combine(date=created_at, time=datetime.max.time())
            stmt = stmt.where(Task.datetime.between(start, end))
        tasks = (await self.execute(stmt)).scalars().all()
        return tasks

    async def _create(self, task_to_create: TaskCreateUpdate) -> UUID:
        stmt = insert(Task).values(**task_to_create.dict(exclude_unset=True)).returning(Task.id)
        result = await self.execute_and_commit(stmt)
        task_id = result.scalars().one() if result else None
        return task_id

    async def _update(self, task_to_update: TaskCreateUpdate) -> Task:
        stmt = update(Task).where(Task.id == task_to_update.id)\
            .values(**task_to_update.dict(exclude_unset=True, exclude={'id'})).returning(Task)

        task = (await self.execute_and_commit(stmt)).scalars().first()
        return task

    async def delete(self, id: UUID) -> bool:
        stmt = delete(Task).where(Task.id == id).returning(Task.id)
        task = (await self.execute_and_commit(stmt)).scalars().first()

        return bool(task)
