from typing import Optional, Dict, Any

from app.domain.exceptions.error_code import ErrorCode


class DomainException(Exception):
    """도메인 예외 기본 클래스"""
    def __init__(self, error_code: ErrorCode, detail: Optional[str] = None, **kwargs):
        self.error_code = error_code
        self.detail = detail
        self.extra_data = kwargs
        super().__init__(self.detail)

    @property
    def status_code(self) -> int:
        return self.error_code.http_status

    @property
    def code(self) -> str:
        return self.error_code.code

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error_code": self.code,
            "message": self.detail or self.error_code.message,
            "status_code": self.status_code,
            **self.extra_data,
        }