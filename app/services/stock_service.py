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


def get_multiple_stocks(symbols: str):

    stock_list = symbols.split(",")

    results = []

    for symbol in stock_list:

        stock = yf.Ticker(symbol.strip())

        data = stock.history(period="1d")

        if data.empty:
            continue

        results.append({
            "symbol": symbol.strip(),
            "price": float(data["Close"].iloc[-1])
        })

    return results