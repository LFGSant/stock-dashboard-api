from sqlalchemy.exc import IntegrityError

from app.database.database import SessionLocal
from app.models.user_model import User


def create_user(username: str, email: str):

    db = SessionLocal()

    try:

        new_user = User(
            username=username,
            email=email
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