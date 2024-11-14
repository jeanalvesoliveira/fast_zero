from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str
    arroz: int


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# Este schema está herdando de UserSchema
# Assim ele possuí todos os atributos
# de UserSchema
class UserDb(UserSchema):
    id: int


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
