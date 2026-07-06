from datetime import datetime
from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException, Query, Path
from services.products import get_all_products, add_product, del_product, change_product

from schema.product import Product, product_update

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, world!"}


@app.get("/get_products")
def get_products():
    products = get_all_products()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return get_all_products()


@app.get("/list_products")
def list_products(
    name: str = Query(
        default=None,
        description="Name of the product to filter by",
        min_length=1,
        max_length=50,
    ),
    sort_by_price: bool = Query(
        default=False, description="Sort products by price in ascending order"
    ),
    order: str = Query(
        default="asc",
        description="Order of sorting: 'asc' for ascending, 'desc' for descending",
    ),
    limit: int = Query(
        default=5, description="Limit the number of products returned", ge=1, le=100
    ),
    offset: int = Query(default=0, description="Offset for pagination"),
):

    products = get_all_products()

    if name:
        niddle = name.strip().lower()
        products = [p for p in products if niddle in p.get("name", "").lower()]

        if not products:
            raise HTTPException(
                status_code=404, detail="No products found with the given name."
            )

        total = len(products)

        if sort_by_price:
            products.sort(key=lambda x: x.get("price", 0), reverse=(order == "desc"))

        return {
            "total": total,
            "products on the page": len(products[offset : offset + limit]),
            "products": products[offset : offset + limit],
        }

    return "hey"


@app.get("/get_product/{product_id}")
def get_product_by_id(
    product_id: str = Path(
        default=...,
        description="The ID of the product to retrieve",
        min_length=1,
        max_length=50,
    )
):
    products = get_all_products()
    for p in products:
        if p.get("id") == product_id:
            return p

    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/add_product", status_code=201)
def add_product_in_file(product: Product):
    product_dict = product.model_dump(mode="json")
    product_dict["id"] = str(uuid4())
    product_dict["created_at"] = datetime.utcnow().isoformat() + "Z"

    try:
        add_product(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return product.model_dump(mode="json")


@app.delete("/delete_product/{sku}")
def remove_product(sku: str):
    try:
        del_product(sku)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/update_product/{product_id}")
def update_product(
    product_id: UUID = Path(..., description="Product UUID"),
    payload: product_update = ...,
):
    try:
        update_product = change_product(
            str(product_id), payload.model_dump(mode="json", exclude_unset=True)
        )
        return update_product
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
