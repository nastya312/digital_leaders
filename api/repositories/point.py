from datetime import datetime, date as date_dt
from uuid import UUID

from sqlalchemy import select, insert, update, delete

from models.point import Point
from repositories.base import BaseRepository
from schemas.point import PointCreateUpdate, PointRead


class PointRepository(BaseRepository):

    async def _get(self, id: UUID) -> Point:
        stmt = select(Point).where(Point.id == id)
        point = (await self.execute(stmt)).scalars().one()
        return point

    async def _get_all(self) -> Point:
        stmt = select(Point)
        points = (await self.execute(stmt)).scalars().all()
        return points

    async def _create(self, point_to_create: PointCreateUpdate) -> UUID:
        stmt = insert(Point).values(**point_to_create.dict(exclude_unset=True)).returning(Point.id)
        result = await self.execute_and_commit(stmt)
        point_id = result.scalars().one() if result else None
        return point_id

    async def _update(self, point_to_update: PointCreateUpdate) -> Point:
        stmt = update(Point).where(Point.id == Point.id)\
            .values(**point_to_update.dict(exclude_unset=True, exclude={'id'})).returning(Point)

        point = (await self.execute_and_commit(stmt)).scalars().first()
        return point

    async def delete(self, id: UUID) -> bool:
        stmt = delete(Point).where(Point.id == id).returning(Point.id)
        point = (await self.execute_and_commit(stmt)).scalars().first()

        return bool(point)
