from tortoise import Model
from tortoise.fields import *

class User(Model):
    id=UUIDField(pk=True)
    name=CharField(1024, unique=True)
    password=CharField(1024)
    mail=CharField(1024, unique=True)
    created_in=DatetimeField(auto_now_add=True)
    tokens:ReverseRelation["Token"]

class Token(Model):
    token=CharField(1024, pk=True)
    created_in=DatetimeField(auto_now_add=True)
    expired_in=DatetimeField()
    user:ForeignKeyRelation[User]=ForeignKeyField("models.User", related_name="tokens")