

from src.entities.item.item import Item

class Order:
    __id: int
    __items: list[Item]

    def __init__(self, order_id: int, items: list[Item]):
        self.order_id = order_id
        self.__items = items

    def get_id(self) -> int:
        return self.order_id

    def get_items(self) -> list[Item]:
        return self.__items
