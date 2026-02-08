from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import get_db, engine

# create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def first_api_call():
    return "hello world"

# CREATE product
@app.post("/products", response_model=schemas.ProductResponse)
def add_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    db_product = models.Product_db(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# READ all products
@app.get("/products", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product_db).all()

# READ product by id
@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    for product in db.query(models.Product_db).all():
        if product.id == product_id:
            return product

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

# UPDATE product
@app.put("/products/{product_id}")
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    for db_product in db.query(models.Product_db).all():
        if db_product.id == product_id:
            db_product.name = product.name
            db_product.description = product.description
            db_product.price = product.price
            db_product.quntity = product.quntity
            db.commit()
            return {"message": "Product updated successfully"}

# DELETE product
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    for db_product in db.query(models.Product_db).all():
        if db_product.id == product_id:
            db.delete(db_product)
            db.commit()
    
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return {"message": "Product deleted successfully"}
