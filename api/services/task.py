import pickle
import uuid
from datetime import date as date_dt
from typing import Type
from uuid import UUID

from pydantic import parse_obj_as

from repositories.task import TaskRepository
from schemas.task import TaskRead, TaskCreateUpdate


class TaskService(TaskRepository):

    async def get(self, id: UUID) -> TaskRead:
        task = TaskRead.from_orm(await self._get(id))
        return task

    async def get_all(self) -> list[TaskRead]:
        tasks = await self._get_all()
        return parse_obj_as(list[TaskRead], tasks)

    async def get_by_user_and_created_date(self, user_id: UUID, date: date_dt = None) -> list[TaskRead]:
        tasks = await self._get_by_user_and_created_date(user_id, date)
        return parse_obj_as(list[TaskRead], tasks)

    async def create(self, task_to_create: TaskCreateUpdate) -> UUID | None:
        task_id = await self._create(task_to_create)
        if not task_id:
            return None
        return task_id

    async def update(self, task_to_update: TaskCreateUpdate) -> TaskRead:

        task = await self._update(task_to_update)
        return TaskRead.from_orm(task)

