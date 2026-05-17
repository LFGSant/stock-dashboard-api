from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class FavoriteStock(Base):

    __tablename__ = "favorite_stocks"

    id = Column(Integer, primary_key=True, index=True)

    symbol = Column(String, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))