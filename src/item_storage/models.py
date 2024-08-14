from datetime import datetime
from DBmanager import base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated, Optional
from sqlalchemy import text

intpk = Annotated[int, mapped_column(primary_key=True)]

created_at = Annotated[datetime,
        mapped_column(
            server_default=text("timezone('utc', now())")
        )
     ]

updated_at = Annotated[datetime,
        mapped_column(
            server_default=text("timezone('utc', now())"),
            onupdate=datetime.utcnow
        )
    ]


class ItemORM(base):
    __tablename__ = "items"

    id: Mapped[intpk]
    name: Mapped[str]
    price: Mapped[float]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    description: Mapped[Optional[str]]
