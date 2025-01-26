from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)
from typing import AsyncGenerator
from core.config import settings


class DataBaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        max_overflow: int = 10,
        pool_size: int = 5,
    ):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size,
        )

        self.session_factory: async_sessionmaker[AsyncEngine] = (
            async_sessionmaker(  # noqa
                bind=self.engine,
                expire_on_commit=False,
                autoflush=False,
                autocommit=False,
            )
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DataBaseHelper(
    url=str(settings.database.url),
    echo=settings.database.echo,
    echo_pool=settings.database.echo_pool,
    max_overflow=settings.database.max_overflow,
    pool_size=settings.database.pool_size,
)
