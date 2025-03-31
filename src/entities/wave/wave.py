from src.entities.order.order import Order


class Wave:
    __orders: list[Order]
    __lower_bound: int
    __upper_bound: int
    def __init__(self, lower_bound: int, upper_bound: int):
        self.__lower_bound = lower_bound
        self.__upper_bound = upper_bound

    def get_lower_bound(self) -> int:
        return self.__lower_bound

    def get_upper_bound(self) -> int:
        return self.__upper_bound
