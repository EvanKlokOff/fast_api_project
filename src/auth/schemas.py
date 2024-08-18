from pydantic import BaseModel, EmailStr, Field, ConfigDict


class SUserRegister(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str = Field(
                            min_length=5,
                            max_length= 30,
                            description="username"
                            )
    email: EmailStr = Field(description="email address")
    password: str = Field(
                            min_length=5,
                            description="password which has length greater than 5"
                        )
