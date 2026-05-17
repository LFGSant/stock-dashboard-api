from fastapi import APIRouter

from app.services.user_service import create_user

router = APIRouter()


@router.post("/users")
def create_new_user(username: str, email: str):

    return create_user(username, email)