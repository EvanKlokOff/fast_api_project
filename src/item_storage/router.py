from fastapi import APIRouter
from .schemas import Item_to_add
from .repository import repository as item_repository


router = APIRouter(
    prefix="/item_storage",
    tags=["item_storage"]
)


@router.post("")
async def add_item(item: Item_to_add) -> dict[str, int]:
    item_id = await item_repository.add_item(item)
    return {"item_id": item_id}


@router.get("")
async def get_items():
    items = await item_repository.get_all_items()
    return items


@router.delete("")
async def delete_items():
    await item_repository.delete_all_items()
