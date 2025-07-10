from dataclasses import dataclass
from typing import Optional


@dataclass
class SocialUser:
    uid: str
    provider: str
    email: Optional[str]
    nickname: Optional[str]
