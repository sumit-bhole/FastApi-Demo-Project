from _collections_abc import AsyncGenerator
import uuid

from sqlalchemy import column, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
import datetime

DATABASE_URL = "sqlite+aiosqlite:///./test.db"


class Post(DeclarativeBase):
    __tablename__ = "posts"

    id = column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = column(Text)
    url = column(String, nullable=False)
    file_type = column(String, nullable=False)
    file_name = column(String, nullable=False)
    created_at = column(DateTime, defaul=datetime.utcnow())


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(DeclarativeBase.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker as session:
        yield session
