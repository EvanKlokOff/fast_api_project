from .schemas import item_filter
from typing import Annotated
from fastapi import Depends


async def _filter_dependency(filter: item_filter) -> dict[str, str]:
    return filter.model_dump()


filter_dependency = Annotated[dict, Depends(_filter_dependency)]