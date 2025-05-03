from src.entities.item.item import Item


class Order:
    """
    Representa um pedido.

    Atributos:
        order_id (int): Identificador unico do pedido.
        items (list[Item]): Lista de itens do pedido.
    """

    def __init__(self, order_id: int, items: list[Item]):
        """
        Inicializa um objeto do tipo Order.
        :param order_id: Identificador unico do pedido.
        :param items: Lista de itens do pedido.
        """
        self.__order_id = order_id
        self.__items = items

    def get_id(self) -> int:
        """
        :return: (int)Identificador unico do pedido.
        """
        return self.__order_id

    def get_items(self) -> list[Item]:
        """
        :return: (list[Item])Lista de itens do pedido.
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
        Itera sobre os itens do pedido.
        :return: (dict) Dicionario (Item ID : Item Quantity).
        """
        dict = {}
        for item in self.__items:
            dict[item.get_id()] = item.get_item_quantity()
        return dict

    def __str__(self):
        """
        :return: Id do pedido.
        """
        return self.__order_id
