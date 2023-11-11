from database.postgresql import get_async_session
from models.user import User
from repositories.user import UserRepository
from schemas.user import UserRead, UserCreateUpdate, RoleEnum
from services.auth import fastapi_users, current_active_user

from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

api_router = APIRouter(tags=["auth"])

api_router.include_router(
    fastapi_users.get_users_router(UserRead, UserCreateUpdate),
    prefix="/auth",
)

@api_router.get("/employees")
async def get_employees(user: User = Depends(current_active_user),
                        session: AsyncSession = Depends(get_async_session)) -> list[UserRead]:
    if user.role_id != RoleEnum.MANAGER:
        raise HTTPException(status_code=403)
    service = UserRepository(session)
    return await service.get_employees()