from pydantic import BaseModel, EmailStr

class UserUpdate(BaseModel):
    name:str=None
    mail:EmailStr=None
    oldPassword:str=None
    newPassword:str=None