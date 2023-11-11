from uuid import UUID

from repositories.location import LocationRepository
from schemas.location import LocationRead, LocationCreateUpdate
from pydantic import parse_obj_as


class LocationService(LocationRepository):

    async def get(self, id: UUID) -> LocationRead:
        location = LocationRead.from_orm(await self._get(id))
        return location

    async def get_all(self) -> list[LocationRead]:
        locations = await self._get_all()
        return parse_obj_as(list[LocationRead], locations)

    async def create(self, location_to_create: LocationCreateUpdate) -> UUID | None:
        location_id = await self._create(location_to_create)
        if not location_id:
            return None
        return location_id

    async def update(self, location_to_update: LocationCreateUpdate) -> LocationRead:

        location = await self._update(location_to_update)
        return LocationRead.from_orm(location)

