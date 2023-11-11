from datetime import datetime, date as date_dt
from uuid import UUID

from sqlalchemy import select, insert, update, delete

from models.task_type import TaskType
from repositories.base import BaseRepository
from schemas.task_type import TaskTypeCreateUpdate, TaskTypeRead


class TaskTypeRepository(BaseRepository):

    async def _get(self, id: UUID) -> TaskType:
        stmt = select(TaskType).where(TaskType.id == id)
        task_type = (await self.execute(stmt)).scalars().one()
        return task_type

    async def _get_all(self) -> TaskType:
        stmt = select(TaskType)
        task_types = (await self.execute(stmt)).scalars().all()
        return task_types

    async def _create(self, task_type_to_create: TaskTypeCreateUpdate) -> UUID:
        stmt = insert(TaskType).values(**task_type_to_create.dict(exclude_unset=True)).returning(TaskType.id)
        result = await self.execute_and_commit(stmt)
        task_type_id = result.scalars().one() if result else None
        return task_type_id

    async def _update(self, task_type_to_update: TaskTypeCreateUpdate) -> TaskType:
        stmt = update(TaskType).where(TaskType.id == TaskType.id)\
            .values(**task_type_to_update.dict(exclude_unset=True, exclude={'id'})).returning(TaskType)

        task_type = (await self.execute_and_commit(stmt)).scalars().first()
        return task_type

    async def delete(self, id: UUID) -> bool:
        stmt = delete(TaskType).where(TaskType.id == id).returning(TaskType.id)
        task_type = (await self.execute_and_commit(stmt)).scalars().first()

        return bool(task_type)
