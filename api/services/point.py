from uuid import UUID

from repositories.point import PointRepository
from schemas.point import PointRead, PointCreateUpdate
from pydantic import parse_obj_as


class PointService(PointRepository):

    async def get(self, id: UUID) -> PointRead:
        point = PointRead.from_orm(await self._get(id))
        return point

    async def get_all(self) -> list[PointRead]:
        points = await self._get_all()
        return parse_obj_as(list[PointRead], points)

    async def create(self, point_to_create: PointCreateUpdate) -> UUID | None:
        point_id = await self._create(point_to_create)
        if not point_id:
            return None
        return point_id

    async def update(self, point_to_update: PointCreateUpdate) -> PointRead:

        point = await self._update(point_to_update)
        return PointRead.from_orm(point)

