from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_team():
    return {"message": "create team"}