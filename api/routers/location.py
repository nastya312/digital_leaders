from database.postgresql import get_async_session
from schemas.location import LocationCreateUpdate, LocationRead
from services.auth import current_active_user
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, Path
import uuid
from models.user import User
from services.location import LocationService

api_router = APIRouter(tags=["auth"])


@api_router.post("/auth/location/")
async def create_location(location: LocationCreateUpdate, user: User = Depends(current_active_user),
                       session: AsyncSession = Depends(get_async_session)):
    service = LocationService(session)
    result = await service.create(location)
    return result if result else {}


@api_router.patch("/auth/location/")
async def update_location(location: LocationCreateUpdate, user: User = Depends(current_active_user),
                       session: AsyncSession = Depends(get_async_session)) -> LocationRead:
    service = LocationService(session)
    return await service.update(location)


@api_router.get("/auth/location/{location_id}/")
async def get_location(location_id: uuid.UUID, user: User = Depends(current_active_user),
                    session: AsyncSession = Depends(get_async_session)) -> LocationRead:
    service = LocationService(session)
    return await service.get(location_id)


@api_router.get("/auth/locations/")
async def get_locations(user: User = Depends(current_active_user),
                     session: AsyncSession = Depends(get_async_session)) -> list[LocationRead]:
    service = LocationService(session)
    return await service.get_all()


@api_router.delete("/{location_id}/")
async def delete_location(location_id: uuid.UUID = Path(),
                      user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)):
    service = LocationService(session)
    status = await service.delete(location_id)
    return {'status': status} if status else False