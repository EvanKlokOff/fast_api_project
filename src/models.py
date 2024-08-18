from typing import Annotated
from sqlalchemy.orm import mapped_column
from datetime import datetime
from sqlalchemy import text


intpk = Annotated[int, mapped_column(primary_key=True)]

created_at = Annotated[
                        datetime,
                        mapped_column(
                            server_default=text("timezone('utc', now())")
                            )
                        ]

updated_at = Annotated[
                        datetime,
                        mapped_column(
                            server_default=text("timezone('utc', now())"),
                            onupdate=datetime.utcnow
                        )
                        ]
