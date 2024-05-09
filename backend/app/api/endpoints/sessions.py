from fastapi import APIRouter

router = APIRouter()

@router.get("/sessions")
def read_users():
    return {"message": "in sessions"}