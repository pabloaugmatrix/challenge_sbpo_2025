from src.entities.access.access import Access
from src.entities.backlog.backlog import Backlog


class Warehouse:
    """
    Representa um galpão.

    Atributos:
        accesses (list[Access]): Lista de corredores dispostos no galpão.
        backlog (Backlog): Backlog com os pedidos pendentes.
    """

    def __init__(self, accesses: list[Access], backlog: Backlog) -> None:
        """
        Inicializa um objeto do tipo Warehouse.
        :param accesses: Lista de corredores dipostos no galpão.
        :param backlog: Backlog com os pedidos pendentes.
        """
        self.__accesses = accesses
        self.__backlog = backlog

    def get_accesses(self) -> list[Access]:
        """
        :return: (list[Access])Lista de corredores dispostos no galpão.
        """
        return self.__accesses

    def get_backlog(self) -> Backlog:
        """
        :return:(Backlog) Backlog com os pedidos pendentes.
        """
        return self.__backlog
