from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.auth.security import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)


def get_current_user_id(
    token: str = Depends(oauth2_scheme)
):

    user_id = decode_access_token(token)

    if user_id is None:

        raise HTTPException(
            status_code=401,
            detail="Token inválido ou expirado"
        )

    return user_id