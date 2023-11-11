from fastapi import APIRouter

from routers.auth import api_router as auth_routers
from routers.user import api_router as user_routers
from routers.grade import api_router as grade_routers
from routers.location import api_router as location_routers

from routers.task import api_router as task_routers
from routers.point import api_router as point_routers
from routers.task_type import api_router as task_type_routers

from settings import api_settings

api_router = APIRouter(prefix=api_settings.URL)
api_router.include_router(auth_routers)
api_router.include_router(user_routers)
api_router.include_router(grade_routers)
api_router.include_router(location_routers)
api_router.include_router(task_routers)
api_router.include_router(point_routers)
api_router.include_router(task_type_routers)
