from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user_service import (
    create_user,
    login_user
)

router = APIRouter()


@router.post("/users")
def create_new_user(
    username: str,
    email: str,
    password: str
):

    return create_user(
        username,
        email,
        password
    )


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    return login_user(
        form_data.username,
        form_data.password
    )