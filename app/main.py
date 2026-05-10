from fastapi import FastAPI
from app.routes.stock_routes import router as stock_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API funcionando!"}


app.include_router(stock_router)