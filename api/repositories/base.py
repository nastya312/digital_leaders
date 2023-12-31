from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, async_session: AsyncSession):
        self.async_session = async_session

    async def execute_and_commit(self, stmt, values=None):
        try:
            result = await self.async_session.execute(stmt, values)
            await self.async_session.commit()
            return result
        except:
            await self.async_session.rollback()
            await self.async_session.close()

    async def execute(self, stmt):
        try:
            return await self.async_session.execute(stmt)
        except:
            await self.async_session.rollback()