from sqlalchemy.exc import IntegrityError

from app.database.database import SessionLocal
from app.models.user_model import User
from app.auth.security import (
    hash_password,
    verify_password
)


def create_user(
    username: str,
    email: str,
    password: str
):

    db = SessionLocal()

    try:

        hashed_password = hash_password(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.add(new_user)

        db.commit()

        db.refresh(new_user)

        return {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }

    except IntegrityError:

        db.rollback()

        return {
            "error": "Usuário ou email já cadastrado"
        }

    finally:

        db.close()


def login_user(
    email: str,
    password: str
):

    db = SessionLocal()

    try:

        user = db.query(User).filter(
            User.email == email
        ).first()

        if not user:

            return {
                "error": "Usuário não encontrado"
            }

        valid_password = verify_password(
            password,
            user.password
        )

        if not valid_password:

            return {
                "error": "Senha inválida"
            }

        return {
            "message": "Login realizado com sucesso",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }

    finally:

        db.close()