from models.product import Product
from typing import List

def get_ordered_products_by_price(products: List[Product]) -> List[Product]:
    return sorted(products, key=lambda x: x.price, reverse=True)
