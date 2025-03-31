from src.entities.order.order import Order


class Wave:
    __orders: list[Order]
    __visited_accesses: list[int]
    __lower_bound: int
    __upper_bound: int
    def __init__(self, lower_bound: int, upper_bound: int):
        self.__lower_bound = lower_bound
        self.__upper_bound = upper_bound
        self.__orders = []  # Inicializa a lista de pedidos
        self.__visited_accesses = []  # Inicializa a lista de corredores visitados

    def get_lower_bound(self) -> int:
        return self.__lower_bound

    def get_upper_bound(self) -> int:
        return self.__upper_bound

    def add_order(self, order: Order):
        self.__orders.append(order)

    def get_orders_quantity(self) -> int:
        return len(self.__orders)

    def add_visited_access(self, access: int):
        self.__visited_accesses.append(access)

    def get_visited_accesses(self) -> list[int]:
        return self.__visited_accesses

    def get_orders(self) -> list[Order]:
        return self.__orders