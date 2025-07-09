from fastapi import APIRouter
from app.api.v1.auth.router import router as auth_router
from app.api.v1.user.router import router as user_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth")
router.include_router(user_router, prefix="/users")
