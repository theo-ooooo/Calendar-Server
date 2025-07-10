from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.domain.user.entity.user import User
from app.infrastructure.auth.repository.redis_refresh_token_store import RedisRefreshTokenStore
from app.infrastructure.auth.service.jwt_token_service import JwtTokenService
from app.infrastructure.db.database import get_session
from app.infrastructure.redis.client import redis_client
from app.infrastructure.user.repository_impl import UserRepositoryImpl
from app.usecases.auth.create_token_pair import CreateTokenPairUseCase
from app.usecases.auth.re_issue_token import ReIssueTokenUseCase
from app.usecases.user.create_or_get_social_user import CreateOrGetSocialUserUseCase


def get_jwt_token_service() -> JwtTokenService:
    """JWT 토큰 서비스 의존성"""
    return JwtTokenService()


def get_refresh_token_store() -> RedisRefreshTokenStore:
    """리프레시 토큰 저장소 의존성"""
    return RedisRefreshTokenStore(redis_client)


def get_user_repository(session: AsyncSession = Depends(get_session)) -> UserRepositoryImpl:
    """사용자 리포지토리 의존성"""
    return UserRepositoryImpl(session)


def get_create_token_use_case(
    jwt_service: JwtTokenService = Depends(get_jwt_token_service),
    token_store: RedisRefreshTokenStore = Depends(get_refresh_token_store)
) -> CreateTokenPairUseCase:
    """토큰 생성 유스케이스 의존성"""
    return CreateTokenPairUseCase(jwt_service, token_store)


def get_reissue_token_use_case(
    jwt_service: JwtTokenService = Depends(get_jwt_token_service),
    token_store: RedisRefreshTokenStore = Depends(get_refresh_token_store)
) -> ReIssueTokenUseCase:
    """토큰 재발급 유스케이스 의존성"""
    return ReIssueTokenUseCase(jwt_service, token_store)


def get_social_user_use_case(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
) -> CreateOrGetSocialUserUseCase:
    """소셜 사용자 생성/조회 유스케이스 의존성"""
    return CreateOrGetSocialUserUseCase(user_repository)

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