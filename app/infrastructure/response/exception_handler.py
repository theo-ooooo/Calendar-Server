import logging
from typing import Union

from starlette.responses import JSONResponse
from fastapi import Request, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.domain.exceptions import DomainException, ErrorCode

logger = logging.getLogger(__name__)


def create_error_response(error_code: str, message: str, status_code: int, **kwargs) -> JSONResponse:
    return JSONResponse({"error_code": error_code, "message": message, **kwargs}, status_code=status_code)

async def domain_exception_handler(request: Request, exc: DomainException):
    return create_error_response(error_code=exc.error_code.code, message=exc.detail, status_code=exc.status_code, **exc.extra_data)





async def http_exception_handler(request: Request, exc: Union[HTTPException, StarletteHTTPException]) -> JSONResponse:
    """HTTP 예외 핸들러"""
    logger.warning(f"HTTP exception occurred: {exc.status_code} - {exc.detail}")

    # HTTPException의 detail이 dict인 경우 (BaseHTTPException에서 발생)
    if isinstance(exc.detail, dict):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": "error",
                "message": exc.detail.get("message", str(exc.detail)),
                "error": {
                    "code": exc.detail.get("error_code", "HTTP_ERROR"),
                    **{k: v for k, v in exc.detail.items() if k not in ["message", "error_code"]}
                }
            }
        )

    # 일반 HTTPException
    return create_error_response(
        error_code="HTTP_ERROR",
        message=str(exc.detail),
        status_code=exc.status_code
    )


async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """일반 예외 핸들러"""
    logger.error(f"Unexpected error occurred: {str(exc)}", exc_info=True)

    return create_error_response(
        error_code=ErrorCode.INTERNAL_SERVER_ERROR.code,
        message=ErrorCode.INTERNAL_SERVER_ERROR.message,
        status_code=ErrorCode.INTERNAL_SERVER_ERROR.http_status
    )