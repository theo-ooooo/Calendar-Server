from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_200_OK

from app.api.v1.auth import schema
from app.api.v1.auth.schema import UserResponse
from app.infrastructure.db.database import get_session
from app.infrastructure.user.repository_impl import UserRepositoryImpl
from app.usecases.user.create_user import CreateUserUseCase
from app.usecases.user.get_user_by_uid import GetUserByUIDUseCase

router = APIRouter()

@router.post("/{provider}", status_code=HTTP_200_OK)
async def social_login(provider: str, body: schema.LoginRequest, session: AsyncSession = Depends(get_session)):
    repository = UserRepositoryImpl(session)
    user_response = await GetUserByUIDUseCase(repository).execute(uid=body.uid, provider=provider)

    if user_response:
        return user_response

    create_user = CreateUserUseCase(repository)

    new_user = await create_user.execute(uid=body.uid, provider=provider, email=body.email)

    print("new_user", new_user)

    return UserResponse.from_entity(new_user)