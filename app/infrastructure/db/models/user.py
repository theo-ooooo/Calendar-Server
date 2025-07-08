from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.db.session import Base

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    uid: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, index=True, nullable=True)
    provider: Mapped[str] = mapped_column(String)  # 소셜로그인용
    nickname: Mapped[str] = mapped_column(String, index=True, nullable=True)

    __table_args__ = (
        UniqueConstraint("uid", "provider", name="uq_user_uid_provider"),
    )
