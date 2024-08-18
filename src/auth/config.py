from pydantic_settings import BaseSettings, SettingsConfigDict


class auth_config(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file="src/auth/env.env")


Auth_config = auth_config()