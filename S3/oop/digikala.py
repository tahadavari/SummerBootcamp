class User:
    pass


class Category:
    pass


class Seller:
    pass


class Product:
    pass


class OrderItem:
    def __init__(self, product, count):
        self.product = product
        self.count = count
