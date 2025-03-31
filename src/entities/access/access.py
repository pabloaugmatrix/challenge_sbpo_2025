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
