import yfinance as yf


def get_stock_data(symbol: str):

    stock = yf.Ticker(symbol)

    info = stock.info

    if "symbol" not in info:
        return {"error": "Ativo não encontrado"}

    data = stock.history(period="1d")

    if data.empty:
        return {"error": "Sem dados disponíveis"}

    return {
        "symbol": info["symbol"],
        "company": info.get("shortName"),
        "price": float(data["Close"].iloc[-1])
    }