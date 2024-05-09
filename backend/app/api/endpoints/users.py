from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def read_users():
    return {"message": "Fetching all users"}