from src.entities.item.item import Item


class Access:
    """
    Representa um corredor.

    Atributos:
        itens (list[Item]): Lista de itens que o corredor tem acesso.

        id (int): Identificador unico do corredor.
    """

    def __init__(self, id: int, items: list[Item]):
        """
        Inicializa um objeto do tipo Access.
        :param id: Identificador unico do corredor.
        :param items: Lista de itens que o corredor tem acesso.
        """
        self.__items = items
        self.__id = id

    def get_id(self) -> int:
        """
        :return: (int)Identificador unico do corredor.
        """
        return self.__id

    def get_items(self) -> list[Item]:
        """
        :return: (list[Item])Lista de itens que o corredor tem acesso.
        """
        return self.__items

    def get_length(self) -> int:
        """
        :return: (int)somatorio das quantidades dos itens do pedido.
        """
        len = 0
        for item in self.__items:
            len += item.get_item_quantity()
        return len

    def get_itemid_and_quantity_dict(self) -> dict:
        """
        Itera sobre os itens do corredor.
        :return: (dict) Dicionario (Item ID : Item Quantity).
        """
        dict = {}
        for item in self.__items:
            dict[item.get_id()] = item.get_item_quantity()
        return dict

    def __str__(self):
        """
        :return: Id do corredor.
        """
        return self.__id