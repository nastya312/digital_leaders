from datetime import datetime, date as date_dt
from uuid import UUID

from sqlalchemy import select, insert, update, delete

from models.grade import Grade
from repositories.base import BaseRepository
from schemas.grade import GradeCreateUpdate, GradeRead


class GradeRepository(BaseRepository):

    async def _get(self, id: UUID) -> Grade:
        stmt = select(Grade).where(Grade.id == id)
        grade = (await self.execute(stmt)).scalars().one()
        return grade

    async def _get_all(self) -> Grade:
        stmt = select(Grade)
        grades = (await self.execute(stmt)).scalars().all()
        return grades

    async def _create(self, grade_to_create: GradeCreateUpdate) -> UUID:
        stmt = insert(Grade).values(**grade_to_create.dict(exclude_unset=True)).returning(Grade.id)
        result = await self.execute_and_commit(stmt)
        grade_id = result.scalars().one() if result else None
        return grade_id

    async def _update(self, grade_to_update: GradeCreateUpdate) -> Grade:
        stmt = update(Grade).where(Grade.id == grade_to_update.id)\
            .values(**grade_to_update.dict(exclude_unset=True, exclude={'id'})).returning(Grade)
        grade = (await self.execute_and_commit(stmt)).scalars().first()
        return grade

    async def delete(self, id: UUID) -> bool:
        stmt = delete(Grade).where(Grade.id == id).returning(Grade.id)
        grade = (await self.execute_and_commit(stmt)).scalars().first()

        return bool(grade)
