class Item:
    """
    Representa um item.

    Atributos:
        item_id (int): Identificador unico do item.
        item_quantity (int): Quantidade de itens do item.
    """

    def __init__(self, item_id: int, item_quantity: int):
        """
        Inicializa um objeto do tipo Item.
        :param item_id: Identificador unico do item.
        :param item_quantity: Quantidade de itens do item.
        """
        self.__item_id = item_id
        self.__item_quantity = item_quantity

    def get_id(self) -> int:
        """
        :return: (int)Identificador unico do item.
        """
        return self.__item_id

    def get_item_quantity(self) -> int:
        """
        :return: (int)Quantidade de itens do item.
        """
        return self.__item_quantity

    def __str__(self):
        """
        :return: Id do item.
        """
        return self.__item_id
