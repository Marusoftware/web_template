from fastapi import APIRouter

router=APIRouter()

from .auth import router as auth_router
router.include_router(auth_router, prefix="/auth")
