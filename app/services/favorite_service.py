from app.database.database import SessionLocal

from app.models.favorite_stock_model import FavoriteStock


def add_favorite_stock(user_id: int, symbol: str):

    db = SessionLocal()

    favorite = FavoriteStock(
        user_id=user_id,
        symbol=symbol
    )

    db.add(favorite)

    db.commit()

    db.refresh(favorite)

    db.close()

    return {
        "message": "Ativo favorito adicionado",
        "symbol": symbol,
        "user_id": user_id
    }