from fastapi import APIRouter, Depends

from app.api.v1.auth.dependencies import require_login
from app.api.v1.user.schema import UserResponse
from app.domain.user.entity.user import User
from app.infrastructure.response.response_handler import ApiResponse

router = APIRouter()


@router.get("/me")
async def get_me(user: User = Depends(require_login)):
    return ApiResponse.success(data=UserResponse.from_entity(user))