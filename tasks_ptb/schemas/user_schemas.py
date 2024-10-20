from pydantic import BaseModel


class UserDto(BaseModel):
    id: int
    username: str
    full_name: str
