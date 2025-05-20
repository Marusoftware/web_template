from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
import contextlib

from .exceptions import APIError, Forbidden, NotFound
from .config import Settings

from tortoise.contrib.fastapi import RegisterTortoise
from .db import DB_CONFIG

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with RegisterTortoise(app, config=DB_CONFIG, use_tz=True, timezone=settings.TZ):
        yield

def custom_generate_unique_id(route: APIRoute):
    return f"{f'{route.tags[0]}-'if len(route.tags) else ''}{route.name}"

app = FastAPI(
    title="changeme",
    description="changeme",
    version="0.0.1",
    root_path="/api/v1",
    generate_unique_id_function=custom_generate_unique_id,
    responses={400: {"model": APIError}, 
               401: {"model": Forbidden},
               404: {"model": NotFound}}
)

@app.exception_handler(APIError)
async def api_error_handler(request: Request, error: APIError):
    raise HTTPException(error.status_code, detail=error.detail)

settings=Settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*",],
    allow_credentials=True,
    allow_methods=["*",],
    allow_headers=["*",],
)

from starlette.middleware.sessions import SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET)

from .routes import router
app.include_router(router)

if settings.SERVE_STATIC is not None:
    with open(f"{settings.SERVE_STATIC}/index.html", "r") as index_file:
        index=index_file.read()
    import os

    @app.get('/{full_path:path}')
    async def spa(full_path:str):
        if full_path=="": full_path="index.html"
        full_path = os.path.normpath(f"{settings.SERVE_STATIC}/{full_path}")
        if not full_path.startswith(settings.SERVE_STATIC): # type: ignore
            raise Forbidden(status_code=403, detail="Forbidden")
        if os.path.exists(full_path):
            return FileResponse(full_path)
        else:
            return HTMLResponse(index)