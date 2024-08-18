from src.DBmanager import base
from sqlalchemy.orm import Mapped, mapped_column
from src.auth.roles import Roles
from src.models import intpk, created_at, updated_at


class User(base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_time: Mapped[created_at]
    updated_time: Mapped[updated_at]
    role: Mapped[Roles] = mapped_column(server_default=Roles.USER, nullable=False)
