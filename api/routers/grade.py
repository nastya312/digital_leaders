from database.postgresql import get_async_session
from schemas.grade import GradeCreateUpdate, GradeRead
from services.auth import current_active_user
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, Path
import uuid
from models.user import User
from services.grade import GradeService

api_router = APIRouter(tags=["auth"])


@api_router.post("/auth/grade/")
async def create_grade(grade: GradeCreateUpdate, user: User = Depends(current_active_user),
                       session: AsyncSession = Depends(get_async_session)):
    service = GradeService(session)
    result = await service.create(grade)
    return result if result else {}


@api_router.patch("/auth/grade/")
async def update_grade(grade: GradeCreateUpdate, user: User = Depends(current_active_user),
                       session: AsyncSession = Depends(get_async_session)) -> GradeRead:
    service = GradeService(session)
    return await service.update(grade)


@api_router.get("/auth/grade/{grade_id}/")
async def get_grade(grade_id: uuid.UUID, user: User = Depends(current_active_user),
                    session: AsyncSession = Depends(get_async_session)) -> GradeRead:
    service = GradeService(session)
    return await service.get(grade_id)


@api_router.get("/auth/grades/")
async def get_grades(session: AsyncSession = Depends(get_async_session),
                     user: User = Depends(current_active_user)) -> list[GradeRead]:
    service = GradeService(session)
    return await service.get_all()


@api_router.delete("/{grade_id}/")
async def delete_grade(grade_id: uuid.UUID = Path(),
                      user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)):
    service = GradeService(session)
    status = await service.delete(grade_id)
    return {'status': status} if status else False