from uuid import UUID

from repositories.grade import GradeRepository
from schemas.grade import GradeRead, GradeCreateUpdate
from pydantic import parse_obj_as


class GradeService(GradeRepository):

    async def get(self, id: UUID) -> GradeRead:
        grade = GradeRead.from_orm(await self._get(id))
        return grade

    async def get_all(self) -> list[GradeRead]:
        grades = await self._get_all()
        return parse_obj_as(list[GradeRead], grades)

    async def create(self, grade_to_create: GradeCreateUpdate) -> UUID | None:
        grade_id = await self._create(grade_to_create)
        if not grade_id:
            return None
        return grade_id

    async def update(self, grade_to_update: GradeCreateUpdate) -> GradeRead:

        grade = await self._update(grade_to_update)
        return GradeRead.from_orm(grade)

