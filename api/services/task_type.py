from uuid import UUID

from repositories.task_type import TaskTypeRepository
from schemas.task_type import TaskTypeRead, TaskTypeCreateUpdate
from pydantic import parse_obj_as


class TaskTypeService(TaskTypeRepository):

    async def get(self, id: UUID) -> TaskTypeRead:
        task_type = TaskTypeRead.from_orm(await self._get(id))
        return task_type

    async def get_all(self) -> list[TaskTypeRead]:
        task_types = await self._get_all()
        return parse_obj_as(list[TaskTypeRead], task_types)

    async def create(self, task_type_to_create: TaskTypeCreateUpdate) -> UUID | None:
        task_type_id = await self._create(task_type_to_create)
        if not task_type_id:
            return None
        return task_type_id

    async def update(self, task_type_to_update: TaskTypeCreateUpdate) -> TaskTypeRead:

        task_type = await self._update(task_type_to_update)
        return TaskTypeRead.from_orm(task_type)

