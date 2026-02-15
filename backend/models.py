from database import Base
from sqlalchemy import Column, Integer, String, Float

class Product_db(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quntity = Column(Integer)