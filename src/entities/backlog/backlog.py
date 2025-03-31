from src.entities.order.order import Order

class Backlog:
    """
    Representa o backlog de pedidos do galpão.

    Attributos:
        orders (list[Order]): lista de pedidos no backlog.
    """

    def __init__(self, orders: list[Order]) -> None:
        self.orders = orders

    def get_orders(self) -> list[Order]:
        return self.orders

    def get_order(self, order_id: int) -> Order:
        for order in self.orders:
            if order.order_id == order_id:
                return order
