from datetime import datetime, date as date_dt
from uuid import UUID

from sqlalchemy import select, insert, update, delete

from models.location import Location
from repositories.base import BaseRepository
from schemas.location import LocationCreateUpdate, LocationRead


class LocationRepository(BaseRepository):

    async def _get(self, id: UUID) -> Location:
        stmt = select(Location).where(Location.id == id)
        location = (await self.execute(stmt)).scalars().one()
        return location

    async def _get_all(self) -> Location:
        stmt = select(Location)
        locations = (await self.execute(stmt)).scalars().all()
        return locations

    async def _create(self, location_to_create: LocationCreateUpdate) -> UUID:
        stmt = insert(Location).values(**location_to_create.dict(exclude_unset=True)).returning(Location.id)
        result = await self.execute_and_commit(stmt)
        location_id = result.scalars().one() if result else None
        return location_id

    async def _update(self, location_to_update: LocationCreateUpdate) -> Location:
        stmt = update(Location).where(Location.id == Location.id)\
            .values(**location_to_update.dict(exclude_unset=True, exclude={'id'})).returning(Location)

        location = (await self.execute_and_commit(stmt)).scalars().first()
        return location

    async def delete(self, id: UUID) -> bool:
        stmt = delete(Location).where(Location.id == id).returning(Location.id)
        location = (await self.execute_and_commit(stmt)).scalars().first()

        return bool(location)
