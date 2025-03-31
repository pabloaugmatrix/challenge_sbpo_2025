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
