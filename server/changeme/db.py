from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from .models import db as db_models
from .config import Settings

settings=Settings()

DB_CONFIG={
    "connections": {"default":settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": [db_models, "aerich.models"],
            "default_connection": "default",
        },
    },
}

def register_db(app:FastAPI):
    register_tortoise(app=app, config=DB_CONFIG)
