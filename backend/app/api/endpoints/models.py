from fastapi import APIRouter

router = APIRouter()

@router.get("/models")
def read_users():
    return {"message": "Fetching all models"}