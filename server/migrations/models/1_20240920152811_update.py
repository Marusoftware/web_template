from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
    CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(1024) NOT NULL UNIQUE,
    "password" VARCHAR(1024) NOT NULL,
    "mail" VARCHAR(1024) NOT NULL UNIQUE,
    "created_in" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS "token" (
    "token" VARCHAR(1024) NOT NULL  PRIMARY KEY,
    "created_in" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "expired_in" TIMESTAMPTZ NOT NULL,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "token";
        DROP TABLE IF EXISTS "user";"""
