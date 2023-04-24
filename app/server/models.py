from pydantic import BaseModel, constr
from datetime import datetime
from typing import List

class UserBaseSchema(BaseModel):
    sub_number: str | None = None
    name: str
    email: str
    password: constr(min_length=8)
    birthday: str | None = None
    region: str | None = None
    termconditions: bool = False
    document: str | None = None
    photo: str | None = None
    video: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    # class Config:
    #     orm_mode = True

class UpdateUserSchema(BaseModel):
    name: str
    birthday: str
    region: str
    termconditions: bool = False
    document: str
    photo: str
    video: str
    updated_at: datetime | None = None

    # class Config:
    #     orm_mode = True

class UserResponse(BaseModel):
    user: UserBaseSchema | None = None

class ListUserResponse(BaseModel):
    sub_number: str  | None = None
    results: int
    users: List[UserBaseSchema]
