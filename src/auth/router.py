from fastapi import APIRouter
from src.auth.schemas import SUserRegister
from src.auth.repository import repository as auth_repository
from fastapi import HTTPException, status
from src.auth.service import get_password_hash

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
    )


@router.post("/register")
async def register_user(user_data: SUserRegister) -> dict:
    user = await auth_repository.get_all(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    user_to_add = SUserRegister(**user_dict)
    await auth_repository.add(user_to_add)
    return {'message': 'Вы успешно зарегистрированы!'}
