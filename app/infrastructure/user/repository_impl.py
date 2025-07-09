# app/infrastructure/user/repository_impl.py
import traceback

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.user.entity import User
from app.domain.user.repository import UserRepository
from app.infrastructure.db.models import User as UserModel

class UserRepositoryImpl(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User) -> User:
        model = UserModel(uid=user.uid, provider=user.provider, email=user.email)
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return User(
            id=model.id,
            uid=model.uid,
            provider=model.provider,
            email=model.email,
            nickname=model.nickname
        )

    async def get_by_uid(self, uid: str, provider: str) -> User | None:
        result = await self.session.execute(
            select(UserModel).where(UserModel.uid == uid, UserModel.provider == provider)
        )
        model: UserModel | None = result.scalar_one_or_none()
        if model is None:
            return None
        return User(
            id=model.id,
            uid=model.uid,
            provider=model.provider,
            email=model.email,
            nickname=model.nickname
        )

    async def get_by_user_id(self, user_id) -> User | None:
        result = await self.session.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        model: UserModel | None = result.scalar_one_or_none()
        if model is None:
            return None
        return User(
            id=model.id,
            uid=model.uid,
            provider=model.provider,
            email=model.email,
            nickname=model.nickname
        )