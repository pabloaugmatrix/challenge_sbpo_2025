from src.entities.item.item import Item

class Access:
    __id: int
    __items: list[Item]

    def __init__(self, id: int, items: list[Item]):
        self.__items = items
        self.__id = id

    def get_id(self) -> int:
        return self.__id

    def get_items(self) -> list[Item]:
        return self.__items