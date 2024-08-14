from DBmanager import session_factory, base
from pydantic import BaseModel
from typing import List
from sqlalchemy import select
from sqlalchemy import delete


class repository:
    @classmethod
    async def add(cls, model: base, schema: BaseModel) -> int:
        async with session_factory() as session:
            item_dict = schema.model_dump()
            item = model(**item_dict)
            session.add(item)
            # функция присвоит item id
            await session.flush()
            await session.commit()
            return item.id

    @classmethod
    async def get_items_by_filter(cls, model: base, schema: BaseModel, **filters) -> List[BaseModel]:
        async with session_factory() as session:
            query = select(
                model
            ).filter_by(filters)
            result = await session.execute(query)
            items = result.scalars().all()
            items_schemas = [schema.model_validate(item) for item in items]
            return items_schemas

    @classmethod
    async def delete_users_by_filter(cls, model: base, **filter) -> None:
        async with session_factory() as session:
            query = delete(model
            ).filter_by(filter)
            await session.execute(query)
            await session.commit()
