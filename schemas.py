from pydantic import BaseModel

class ProductBase(BaseModel):
    id : int 
    name : str 
    description : str
    price : float 
    quntity : int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        model_config = {
            "from_attributes": True
        }