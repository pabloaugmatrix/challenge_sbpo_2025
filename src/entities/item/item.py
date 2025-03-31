

class Item:
    __id: int
    __item_quantity: int

    def __init__(self, item_id: int, item_quantity: int):
        self.item_id = item_id
        self.__item_quantity = item_quantity

    def get_id(self) -> int:
        return self.item_id

    def get_item_quantity(self) -> int:
        return self.__item_quantity
