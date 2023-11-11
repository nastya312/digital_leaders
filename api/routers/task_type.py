import datetime
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, Path

from database.postgresql import get_async_session
from models.user import User
from schemas.task_type import TaskTypeCreateUpdate, TaskTypeRead
from services.auth import current_active_user
from services.task_type import TaskTypeService

api_router = APIRouter(tags=["task"])


@api_router.post("/task/task_type/")
async def create_task_type(task_type: TaskTypeCreateUpdate, user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)):
    service = TaskTypeService(session)
    result = await service.create(task_type)
    return result if result else {}


@api_router.patch("/task/task_type/")
async def update_task_type(task_type: TaskTypeCreateUpdate, user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)) -> TaskTypeRead:
    service = TaskTypeService(session)
    return await service.update(task_type)


@api_router.get("/task_type/task_type/{task_type_id}/")
async def get_task_type(task_type_id: uuid.UUID = Path(), user: User = Depends(current_active_user),
                   session: AsyncSession = Depends(get_async_session)) -> TaskTypeRead:
    service = TaskTypeService(session)
    return await service.get(task_type_id)


@api_router.get("/task/task_types/")
async def get_task_types(user: User = Depends(current_active_user),
                    session: AsyncSession = Depends(get_async_session)) -> list[TaskTypeRead]:
    service = TaskTypeService(session)
    return await service.get_all()


@api_router.delete("/task/{task_type_id}/")
async def delete_task_type(task_type_id: uuid.UUID = Path(),
                      user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)):
    service = TaskTypeService(session)
    status = await service.delete(task_type_id)
    return {'status': status} if status else False