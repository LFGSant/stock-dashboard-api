from sqlalchemy.exc import IntegrityError

from app.database.database import SessionLocal
from app.models.user_model import User
from app.auth.security import hash_password


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