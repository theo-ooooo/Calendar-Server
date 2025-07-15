from enum import Enum
from fastapi import status


class ErrorCode(Enum):
    """에러 코드 정의"""

    def __init__(self, http_status: int, message: str):
        self.http_status = http_status
        self.message = message

    # Common
    METHOD_NOT_ALLOWED = (status.HTTP_405_METHOD_NOT_ALLOWED, "지원하지 않는 HTTP method 입니다.")
    INTERNAL_SERVER_ERROR = (status.HTTP_500_INTERNAL_SERVER_ERROR, "서버 오류, 관리자에게 문의하세요")
    BAD_REQUEST = (status.HTTP_400_BAD_REQUEST, "잘못된 요청입니다.")
    FORBIDDEN = (status.HTTP_403_FORBIDDEN, "잘못된 접근 입니다.")
    UNAUTHORIZED = (status.HTTP_401_UNAUTHORIZED, "인증이 실패했습니다.")
    NOT_FOUND = (status.HTTP_404_NOT_FOUND, "요청한 리소스를 찾을 수 없습니다.")

    # Member/User
    USER_NOT_FOUND = (status.HTTP_404_NOT_FOUND, "존재하지 않는 회원입니다.")
    USER_EXISTS = (status.HTTP_409_CONFLICT, "존재하는 회원입니다.")
    USER_ALREADY_DELETED = (status.HTTP_409_CONFLICT, "이미 탈퇴한 회원 입니다.")

    # Auth
    AUTH_UNAUTHORIZED = (status.HTTP_401_UNAUTHORIZED, "아이디 또는 비밀번호를 확인해주세요")
    AUTH_SERVER_ERROR = (status.HTTP_500_INTERNAL_SERVER_ERROR, "시큐리티 인증 정보를 찾을수 없습니다.")
    AUTH_FAILED = (status.HTTP_401_UNAUTHORIZED, "인증에 실패하였습니다.")
    AUTH_TOKEN_EXPIRED = (status.HTTP_401_UNAUTHORIZED, "Token이 만료 되었습니다.")
    AUTH_REFRESH_TOKEN_EXPIRED = (status.HTTP_401_UNAUTHORIZED, "RefreshToken이 만료되었습니다.")


    @property
    def code(self) -> str:
        return self.name


    def __str__(self) -> str:
        return f"{self.code}: {self.message}"