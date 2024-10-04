from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id:UUID
    expired_in:datetime

class User(BaseModel):
    id:UUID
    name:str
    mail:EmailStr