from fastapi import FastAPI, Request, HTTPException
import time
from models.product import Product
from models.product_response import ProductResponse

app = FastAPI()


@app.get("/health")
def healthcheck():
    return 'UP'


@app.post("/v1/products")
async def post_products(request: Request, product: Product = None):
    print(product)
    if product.id is None:
        HTTPException(status_code=400, detail=f'Product id not found {product.__repr__}')
    return ProductResponse(id=product.id, name=product.name, description=product.description)