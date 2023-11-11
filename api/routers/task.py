import datetime
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, Path

from database.postgresql import get_async_session
from models.user import User
from schemas.task import TaskCreateUpdate, TaskRead
from services.auth import current_active_user
from services.task import TaskService

api_router = APIRouter(tags=["task"])


@api_router.post("/task/task")
async def create_task(task: TaskCreateUpdate, user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)):
    service = TaskService(session)
    result = await service.create(task)
    return result if result else {}


@api_router.patch("/task/task")
async def update_task(task: TaskCreateUpdate, user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)) -> TaskRead:
    service = TaskService(session)
    return await service.update(task)


@api_router.get("/task/task/{task_id}")
async def get_task(task_id: uuid.UUID = Path(), user: User = Depends(current_active_user),
                   session: AsyncSession = Depends(get_async_session)) -> TaskRead:
    service = TaskService(session)
    return await service.get(task_id)


@api_router.get("/task/tasks")
async def get_tasks(user: User = Depends(current_active_user),
                    session: AsyncSession = Depends(get_async_session)) -> list[TaskRead]:
    service = TaskService(session)
    return await service.get_all()


@api_router.get("/task/tasks/{user_id}")
async def get_tasks(user_id: uuid.UUID = Path(), user: User = Depends(current_active_user),
                    date: datetime.datetime = datetime.datetime.now(),
                    session: AsyncSession = Depends(get_async_session)) -> list[TaskRead]:
    service = TaskService(session)
    return await service.get_by_user_and_created_date(user_id, date)


@api_router.delete("/task/{task_id}")
async def delete_task(task_id: uuid.UUID = Path(),
                      user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)):
    service = TaskService(session)
    status = await service.delete(task_id)
    return {'status': status} if status else False