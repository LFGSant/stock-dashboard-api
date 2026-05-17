from fastapi import FastAPI

from app.routes.stock_routes import router as stock_router
from app.routes.user_routes import router as user_router
from app.routes.favorite_routes import router as favorite_router

from app.database.database import engine
from app.database.database import Base

from app.models.user_model import User
from app.models.favorite_stock_model import FavoriteStock


app = FastAPI()
app.include_router(favorite_router)


Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "API funcionando!"}


app.include_router(stock_router)
app.include_router(user_router)