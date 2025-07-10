from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.database import get_session
from app.infrastructure.user.repository_impl import UserRepositoryImpl
from app.usecases.user.create_user import CreateUserUseCase
from app.usecases.user.get_user_by_uid import GetUserByUIDUseCase


def get_user_repository(session: AsyncSession = Depends(get_session)) -> UserRepositoryImpl:
    """사용자 리포지토리 의존성"""
    return UserRepositoryImpl(session)


def get_create_user_use_case(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
) -> CreateUserUseCase:
    """사용자 생성 유스케이스 의존성"""
    return CreateUserUseCase(user_repository)


def get_user_by_uid_use_case(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
) -> GetUserByUIDUseCase:
    """UID로 사용자 조회 유스케이스 의존성"""
    return GetUserByUIDUseCase(user_repository)