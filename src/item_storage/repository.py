from DBmanager import session_factory
from src.item_storage.schemas import Item_to_add, Item
from typing import List
from src.item_storage.models import ItemORM
from sqlalchemy import select
from sqlalchemy import delete


class repository:
    @classmethod
    async def add_item(cls, item: Item_to_add) -> int:
        async with session_factory() as session:
            item_dict = item.model_dump()
            item_ = ItemORM(**item_dict)
            session.add(item_)
            await session.flush()
            await session.commit()
            return item_.id

    @classmethod
    async def get_all_items(cls) -> List[Item]:
        async with session_factory() as session:
            query = select(
                ItemORM
            )
            result = await session.execute(query)
            items = result.scalars().all()
            items_schemas = [Item.model_validate(item) for item in items]
            return items_schemas

    @classmethod
    async def delete_all_items(cls) -> None:
        async with session_factory() as session:
            query = delete(ItemORM
            )
            await session.execute(query)
            await session.commit()

    # @classmethod
    # async def get_items_by_filters(cls, filters: dict) -> List[Item]:
    #     print(filters)
    #     async with session_factory() as session:
    #         query = select(
    #             ItemORM
    #         ).filter_by(**filters)
    #         result = await session.execute(query)
    #         items = result.scalars().all()
    #         items_schemas = [Item.model_validate(item) for item in items]
    #         return items_schemas
    #
    # @classmethod
    # async def delete_users_by_filters(cls, filters: dict) -> None:
    #     async with session_factory() as session:
    #         query = delete(ItemORM
    #         ).filter_by(**filters)
    #         await session.execute(query)
    #         await session.commit()
