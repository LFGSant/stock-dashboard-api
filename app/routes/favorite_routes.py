from fastapi import APIRouter

from app.services.favorite_service import add_favorite_stock

router = APIRouter()


@router.post("/favorites")
def create_favorite(user_id: int, symbol: str):

    return add_favorite_stock(user_id, symbol)