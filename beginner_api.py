#Create a web API using FastAPI with a route to products.
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()
class Product(BaseModel):
    id: int
    name: str
    price: float
class ProductList(BaseModel):
    products: List[Product]
@app.get("/products", response_model=ProductList)
async def get_products():
    return ProductList(products=[
        Product(id=1, name="Laptop", price=999.99),
        Product(id=2, name="Smartphone", price=499.99),
        Product(id=3, name="Tablet", price=299.99)
    ])
@app.get("/")
async def root():
    return {"message": "Welcome to the Product API!"}
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    products = [
        Product(id=1, name="Laptop", price=999.99),
        Product(id=2, name="Smartphone", price=499.99),
        Product(id=3, name="Tablet", price=299.99)
    ]
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}
@app.post("/products", response_model=Product)
async def create_product(product: Product):
    # In a real application, you would save the product to a database here.
    return product