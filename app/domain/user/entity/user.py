# app/domain/user/user.py
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class User:
    uid: str
    provider: str
    email: Optional[str] = None
    nickname: Optional[str] = None
    id: Optional[int] = None
