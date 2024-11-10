from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str
    arroz: int


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr