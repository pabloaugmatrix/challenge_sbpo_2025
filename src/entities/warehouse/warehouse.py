from src.entities.access.access import Access
from src.entities.backlog import Backlog


class Warehouse:
    __accesses: list[Access]
    __backlog: Backlog

    def __init__(self, accesses: list[Access]) -> None:
        self.__accesses = accesses
        self.__backlog = Backlog()

    def get_accesses(self) -> list[Access]:
        return self.__accesses

    def get_backlog(self) -> Backlog:
        return self.__backlog