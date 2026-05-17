from fastapi import APIRouter

from app.services.stock_service import (
    get_stock_data,
    get_multiple_stocks
)

router = APIRouter()


@router.get("/stock/{symbol}")
def stock(symbol: str):

    return get_stock_data(symbol)


@router.get("/stocks")
def multiple_stocks(symbols: str):

    return get_multiple_stocks(symbols)