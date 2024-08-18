from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


class item_filter(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class Item_to_add(BaseModel):
    name: str
    price: float = Field(..., ge=0)
    description: Optional[str]


class Item(Item_to_add):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime

