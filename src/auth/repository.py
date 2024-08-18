from src.auth.models import User
from src.repository import repository as base_repository
from src.auth.schemas import SUserRegister


class repository(base_repository):
    schema = SUserRegister
    model = User
