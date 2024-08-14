from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class item_filter(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class Item_to_add(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


class Item(Item_to_add):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime

