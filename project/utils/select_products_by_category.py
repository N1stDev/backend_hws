from models.product import Product
from typing import List

def select_products_by_category(products: List[Product], category: str) -> List[Product]:
    return [p for p in products if p.category==category]
