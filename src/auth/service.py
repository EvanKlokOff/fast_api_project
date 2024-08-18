from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from src.auth.config import Auth_config
from pydantic import EmailStr
from src.auth.repository import repository as auth_repository

#создание контекста для хэширования
password_context = CryptContext(
                                schemes=["bcrypt"],
                                deprecated="auto"
                                )


def get_password_hash(password: str) -> str:
    return password_context.hash(password)


def verify_password(plain_password: str,
                    hashed_password: str) -> bool:
    return password_context.verify(
                                    plain_password,
                                    hashed_password
                                   )


def create_access_token(data: dict, expired_time: float = 3600) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(seconds=expired_time)
    to_encode.update({"expire": expire})
    encode_jwt = jwt.encode(
                            to_encode,
                            key=Auth_config.SECRET_KEY,
                            algorithm=Auth_config.ALGORITHM
                            )
    return encode_jwt

async def authenticate_user(email: EmailStr, password: str):
    user = await auth_repository.get_all(email=email)
    if not user or verify_password(plain_password=password, hashed_password=user) is False:
        return None
    return user

