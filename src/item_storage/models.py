from src.DBmanager import base
from sqlalchemy.orm import Mapped
from typing import Optional
from src.models import intpk, created_at, updated_at


class ItemORM(base):
    __tablename__ = "items"

    id: Mapped[intpk]
    name: Mapped[str]
    price: Mapped[float]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    description: Mapped[Optional[str]]
