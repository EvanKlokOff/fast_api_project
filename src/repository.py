from DBmanager import session_factory
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy import delete


class repository:
    model = None
    schema = None

    @classmethod
    async def add(cls, item: schema) -> int:
        async with session_factory() as session:
            item_dict = item.model_dump()
            item = cls.model(**item_dict)
            session.add(item)
            # функция присвоит item id
            await session.flush()
            await session.commit()
            return item.id
    @classmethod
    async def get_one_or_none(cls, **filters) -> Optional[schema]:
        async with session_factory() as session:
            query = query = select(
                cls.model
            ).filter_by(**filters)
            result = await session.execute(query)


    @classmethod
    async def get_all(cls, **filters) -> List[schema]:
        async with session_factory() as session:
            query = select(
                cls.model
            ).filter_by(**filters)
            result = await session.execute(query)
            items = result.scalars().all()
            items_schemas = [cls.schema.model_validate(item) for item in items]
            return items_schemas

    @classmethod
    async def delete_all(cls, **filters) -> None:
        async with session_factory() as session:
            query = delete(cls.model).filter_by(**filters)
            await session.execute(query)
            await session.commit()
