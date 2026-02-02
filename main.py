from fastapi import FastAPI, Depends
from schemas import ProductBase, ProductResponse, ProductCreate
from database import get_db, engine
import models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def first_api_call():
    return "hello world"

products = [
    ProductBase(id=1, name="phone", description="IOS", price=999, quntity=5),
    ProductBase(id=2, name="laptop", description="Lenevo", price=99, quntity=4),
    ProductBase(id=3, name="computer", description="Acer", price=889, quntity=3)
]

@app.post("/products", response_model=ProductResponse)
def All_products(product: ProductCreate, db : Session = Depends(get_db)):
    db_product = models.Product_db(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

@app.get("/product_details")
def product_detail():
    return products



@app.post("/produts/post")
def Add_products(product : ProductBase):
    products.append(product)
    return product

@app.put("/products/put")
def update_products(id : int, product : ProductBase):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product

    return "update successful"

@app.delete("/products/delete")
def delete_products(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "deleted"
        


