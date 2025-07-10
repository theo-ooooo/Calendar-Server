from fastapi import APIRouter, Depends

from app.api.v1.user.schema import UserResponse
from app.domain.user.entity.user import User
from app.infrastructure.dependencies.auth import require_login

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def get_me(user: User = Depends(require_login)):
    return UserResponse.from_entity(user)