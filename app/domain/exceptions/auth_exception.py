from typing import Optional

from app.domain.exceptions.base_exception import DomainException
from app.domain.exceptions.error_code import ErrorCode


class AuthException(DomainException):


    @classmethod
    def unauthorized(cls, detail: Optional[str] = None) -> 'AuthException':
        return cls(error_code=ErrorCode.UNAUTHORIZED, code="UNAUTHORIZED", message=detail or "Unauthorized")

    @classmethod
    def server_error(cls, detail: Optional[str] = None) -> 'AuthException':
        return cls(ErrorCode.AUTH_SERVER_ERROR, detail)

    @classmethod
    def failed(cls, detail: Optional[str] = None) -> 'AuthException':
        return cls(ErrorCode.AUTH_FAILED, detail)

    @classmethod
    def token_expired(cls, detail: Optional[str] = None) -> 'AuthException':
        return cls(ErrorCode.AUTH_TOKEN_EXPIRED, detail)

    @classmethod
    def refresh_token_expired(cls, detail: Optional[str] = None) -> 'AuthException':
        return cls(ErrorCode.AUTH_REFRESH_TOKEN_EXPIRED, detail)