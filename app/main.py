from fastapi import FastAPI

from app.api import router as v1_router

app = FastAPI()


# 전체 v1 경로로 묶기
app.include_router(v1_router, prefix="/api/v1")
@app.get("/")
def read_root():
    return {"Hello": "World"}