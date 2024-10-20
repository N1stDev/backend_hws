class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category: str):
        self.category = new_category

    def edit_price(self, new_price: float):
        self.price = new_price

    def set_sale(self, sale: float):
        self.sale = sale

    def cancel_sale(self):
        self.sale = 0

    def get_price(self) -> float:
        # Это не тупо геттер - тут надо учесть скидку и еще то, что скидка указана в процентах
        return self.price - self.price * self.sale / 100

    def __repr__(self):
        return f"{self.name} - {self.get_price()}"
