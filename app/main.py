from fastapi import FastAPI

from app.api import router as v1_router
from fastapi import FastAPI, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.domain.exceptions import DomainException
from app.infrastructure.response.exception_handler import (
    domain_exception_handler,
    http_exception_handler,
    general_exception_handler
)


def create_app() -> FastAPI:
    """FastAPI 앱 생성 및 설정"""

    app = FastAPI(
        title="Calendar Server",
        description="Calendar Server API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_exception_handler(DomainException, domain_exception_handler)

    # HTTP 예외 핸들러
    from fastapi import HTTPException
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)

    # 일반 예외 핸들러
    app.add_exception_handler(Exception, general_exception_handler)

    app.include_router(v1_router, prefix="/api/v1")

    return app

app = create_app()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)