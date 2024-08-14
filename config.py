from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class config(BaseSettings):
    DB_PORT: int
    DB_NAME: str
    DB_PASSWORD: int
    DB_HOST: str
    DB_USER_NAME: str
    DB_DRIVER_NAME: str

    @property
    def db_url(self):
        return URL.create(
            drivername=self.DB_DRIVER_NAME,
            username=self.DB_USER_NAME,
            password=self.DB_PASSWORD,  # plain (unescaped) text
            host=self.DB_HOST,
            database=self.DB_NAME,
            port=self.DB_PORT
        )
    model_config = SettingsConfigDict(env_file="env.env")


Config = config()
