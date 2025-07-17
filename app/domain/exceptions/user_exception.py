from typing import Optional

from app.domain.exceptions.base_exception import DomainException
from app.domain.exceptions.error_code import ErrorCode


class UserException(DomainException):

    @classmethod
    def user_not_found(cls, user_id: Optional[str] = None) -> 'UserException':
        return cls(
            error_code=ErrorCode.USER_NOT_FOUND,
            code="USER_NOT_FOUND",
            message=f"User not found: {user_id}" if user_id else "User not found",
        )

    @classmethod
    def user_exists(cls, user_id: Optional[str] = None) -> 'UserException':
        return cls(
            error_code=ErrorCode.USER_EXISTS,
            code="USER_EXISTS",
            message=f"User already exists: {user_id}" if user_id else "User already exists",
        )

    @classmethod
    def user_already_deleted(cls, user_id: Optional[str] = None) -> 'UserException':
        return cls(
            error_code=ErrorCode.USER_ALREADY_DELETED,
            code="USER_ALREADY_DELETED",
            message=f"User already deleted: {user_id}" if user_id else "User already deleted",
        )