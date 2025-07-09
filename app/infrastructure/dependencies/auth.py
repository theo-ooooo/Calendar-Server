
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.domain.user.entity import User
from app.infrastructure.auth.jwt_token_service import JwtTokenService
from app.infrastructure.db.database import get_session
from app.infrastructure.user.repository_impl import UserRepositoryImpl


async def get_current_user(
        token: str = Depends(OAuth2PasswordBearer(tokenUrl="token")),
        session: AsyncSession = Depends(get_session)) -> User:
    try:
        print("token", token)
        payload = JwtTokenService().verify_token(token)
        user_id = payload.get("sub")
        print("userId", user_id)
        print("payload", payload)

        if user_id is None:
            raise credentials_exception()

        user = await UserRepositoryImpl(session).get_by_user_id(int(user_id))

        if not user:
            raise credentials_exception()

        return user


    except JWTError:
        raise credentials_exception()

def require_login(current_user: User = Depends(get_current_user)) -> User:
    return current_user


def credentials_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )