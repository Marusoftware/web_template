from typing import List
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter, Depends, Request

from ..exceptions import APIError

from ..models.response.user import User, Token
from ..models.request.auth import UserCreate
from ..models.db.user import User as UserDB
from ..models.db import Token as TokenDB
from ..config import Settings
import secrets
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

from tortoise.expressions import Q

router=APIRouter(tags=["Auth"])
oauth=OAuth2PasswordBearer(tokenUrl="/api/v1/auth/signin")
crypt=CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user(token: oauth=Depends()): # type: ignore
    token:TokenDB=await TokenDB.get(token=token).prefetch_related("user")
    return token.user

@router.post("/signin", response_model=Token)
async def signin(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    user=await UserDB.get_or_none(Q(name=form_data.username) | Q(mail=form_data.username))
    if user is None:
        raise APIError(detail="Password or Username is wrong.")
    if user.password is not None:
        if not crypt.verify(form_data.password,user.password):
            raise APIError(detail="Password or Username is wrong.")
        token=await TokenDB.create(token=secrets.token_hex(32), user=user, expired_in=datetime.now(tz=timezone(offset=Settings().timedelta))+timedelta(hours=2))
        if "users" not in request.session:
            request.session["users"]=[]
        request.session["users"].append({"name":user.name, "id":str(user.id), "token":token.token, "expired_in":token.expired_in.isoformat()})
        return Token(access_token=token.token, token_type="bearer", user_id=user.id, expired_in=token.expired_in)

@router.post("/signup", response_model=User)
async def signup(user:UserCreate):
    if await UserDB.exists(Q(name=user.name) | Q(mail=user.mail)):
        raise APIError(detail="Password or Username is wrong.")
    return await UserDB.create(name=user.name, mail=user.mail, password=crypt.hash(user.password.get_secret_value()))

@router.post("/signout")
async def signout(request:Request, token:str =Depends(oauth)):
    if "users" in request.session:
        request.session["users"]=[user for user in request.session["users"] if user["token"]!=token]
    await TokenDB.filter(token=token).delete()

@router.get("/session", response_model=List[Token])
async def session(request:Request):
    if not "users" in request.session:
        return []
    return [Token(access_token=user["token"], token_type="bearer", user_id=user["id"], expired_in=user["expired_in"]) for user in request.session["users"] if await TokenDB.exists(token=user["token"])]