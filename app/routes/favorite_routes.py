from fastapi import APIRouter, Depends

from app.services.favorite_service import add_favorite_stock
from app.auth.dependencies import get_current_user_id

router = APIRouter()


@router.post("/favorites")
def create_favorite(
    symbol: str,
    user_id: int = Depends(get_current_user_id)
):

    return add_favorite_stock(
        user_id,
        symbol
    )