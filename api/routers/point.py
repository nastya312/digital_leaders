import datetime
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, Path

from database.postgresql import get_async_session
from models.user import User
from schemas.point import PointCreateUpdate, PointRead
from services.auth import current_active_user
from services.point import PointService

api_router = APIRouter(tags=["task"])


@api_router.post("/task/point/")
async def create_point(point: PointCreateUpdate, user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)):
    service = PointService(session)
    result = await service.create(point)
    return result if result else {}


@api_router.patch("/task/point/")
async def update_point(point: PointCreateUpdate, user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)) -> PointRead:
    service = PointService(session)
    return await service.update(point)


@api_router.get("/point/point/{point_id}/")
async def get_point(point_id: uuid.UUID = Path(), user: User = Depends(current_active_user),
                   session: AsyncSession = Depends(get_async_session)) -> PointRead:
    service = PointService(session)
    return await service.get(point_id)


@api_router.get("/task/points/")
async def get_points(user: User = Depends(current_active_user),
                    session: AsyncSession = Depends(get_async_session)) -> list[PointRead]:
    service = PointService(session)
    return await service.get_all()


@api_router.delete("/task/{point_id}/")
async def delete_point(point_id: uuid.UUID = Path(),
                      user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)):
    service = PointService(session)
    status = await service.delete(point_id)
    return {'status': status} if status else False