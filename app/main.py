from fastapi import FastAPI

from app.api import router as v1_router


def create_app() -> FastAPI:
    """FastAPI 앱 생성 및 설정"""

    app = FastAPI(
        title="Calendar Server",
        description="Calendar Server API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.include_router(v1_router, prefix="/api/v1")

    return app

app = create_app()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)