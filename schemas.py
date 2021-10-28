from pydantic import BaseModel


class LogInDetails(BaseModel):
    username: str
    password: str


class SignUpDetails(BaseModel):
    username: str
    password: str
    name: str
