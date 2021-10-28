from pydantic import BaseModel


class LogInDetails(BaseModel):
    email: str
    password: str


class SignUpDetails(BaseModel):
    email: str
    password: str
    name: str
