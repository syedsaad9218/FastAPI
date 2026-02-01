from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get("/")
def first_api_call():
    return "hello world"

products = [
    Products(id=1, name="phone", description="IOS", price=999, quntity=5),
    Products(id=2, name="laptop", description="Lenevo", price=99, quntity=4),
    Products(id=3, name="computer", description="Acer", price=889, quntity=3)
]

@app.get("/products")
def All_products():
    return products

@app.post("/produts/post")
def Add_products(product : Products):
    products.append(product)
    return product

@app.put("/products/put")
def update_products(id : int, product : Products):
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

