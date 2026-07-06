import json
from pathlib import Path
from typing import List, Dict

Data_File = Path(__file__).parent.parent / "data" / "dummy.json"


def load_products() -> List[Dict]:
    if not Data_File.exists():
        return []
    with open(Data_File, "r", encoding="utf-8") as file:
        return json.load(file)


def get_all_products() -> List[Dict]:
    return load_products()


def save_product(products: List[Dict]) -> None:
    with open(Data_File, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=2, ensure_ascii=False)


def add_product(product: Dict) -> Dict:
    products = load_products()

    if any(p["sku"] == product["sku"] for p in products):
        raise ValueError("Product with the same SKU already exists")

    products.append(product)
    save_product(products)
    return product


def del_product(sku: str) -> Dict:
    products = load_products()

    products = [p for p in products if p["sku"] != sku]
    save_product(products)


def change_product(product_id: str, update_data: Dict):
    products = load_products()

    for index, product in enumerate(products):
        if product_id == product["id"]:
            for key, value in update_data.items():
                if value is None:
                    continue

                if isinstance(value, dict) and isinstance(product.get(key), dict):
                    product[key].update(value)
                else:
                    product[key] = value

            products[index] = product
            save_product(products)
            return product
    raise ValueError("product not found!")
