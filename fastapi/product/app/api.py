from fastapi import FastAPI, Request
import time
from .models.product import Product
from .models.product_response import ProductResponse

app = FastAPI()


@app.get("/health")
def healthcheck():
    return 'UP'


@app.post("/v1/products")
async def post_products(request: Request, product: Product = None)
    print(time.time_ns())
    return ProductResponse(id=product.id, name=product.name, description=product.description)