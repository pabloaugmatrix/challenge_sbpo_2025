from src.entities.order.order import Order

class Backlog:
    Orders: list[Order]

    def __init__(self, orders: list[Order]) -> None:
        self.orders = orders

    def get_orders(self) -> list[Order]:
        return self.orders
