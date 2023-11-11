from repositories.user import get_user_manager
from schemas.user import UserRead, UserCreateUpdate, RoleEnum
from services.auth import fastapi_users, auth_backend, current_active_user

from models.user import User

from fastapi import APIRouter, Depends, HTTPException, Request, status

from fastapi_users import exceptions, models, schemas
from fastapi_users.manager import BaseUserManager, UserManagerDependency


api_router = APIRouter(tags=["auth"])

api_router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)


@api_router.get("/auth/verify")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"user_id": user.id}


@api_router.post("/api/register")
async def register(
    request: Request,
    user_create: UserCreateUpdate,
    user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
):
    try:
        created_user = await user_manager.create(
            user_create, safe=(True if user_create.role_id == RoleEnum.EMPLOYEE else False), request=request
        )

    except exceptions.UserAlreadyExists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    except exceptions.InvalidPasswordException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return UserRead.from_orm(created_user)
