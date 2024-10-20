from models.product import Product
from typing import List

def extract_prices(products: List[Product]) -> List[int]:
    return [p.price for p in products]
