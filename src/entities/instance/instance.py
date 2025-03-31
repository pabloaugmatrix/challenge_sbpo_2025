from src.entities.order.order import Order


class Instance:
    __order_quantity: int
    __item_quantity: int
    __access_quantity: int
    def __init__(self, order_quantity: int, item_quantity: int, access_quantity: int):
        self.__order_quantity = order_quantity
        self.__item_quantity = item_quantity
        self.__access_quantity = access_quantity

    def get_order_quantity(self) -> int:
        return self.__order_quantity
    def get_item_quantity(self) -> int:
        return self.__item_quantity
    def get_access_quantity(self) -> int:
        return self.__access_quantity