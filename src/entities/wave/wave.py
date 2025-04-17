from src.entities.order.order import Order


class Wave:
    """
    Representa um um subconjunto de pedidos do backlog selecionados para serem
    processados (ou roteados) juntos.

    Atributos:
        lower_bound (int): Limite inferior do subconjunto de pedidos.
        upper_bound (int): Limite superior do subconjunto de pedidos.
        orders (list[Order]): Lista de pedidos no subconjunto.
        visited_accesses (list[int]): Lista de corredores visitados no subconjunto.
    """

    def __init__(self, lower_bound: int, upper_bound: int):
        """
        Inicializa um objeto do tipo Wave.
        :param lower_bound: Limite inferior do subconjunto de pedidos.
        :param upper_bound: Limite superior do subconjunto de pedidos.
        """
        self.__lower_bound = lower_bound
        self.__upper_bound = upper_bound
        self.__orders = []
        self.__visited_accesses = []

    def get_lower_bound(self) -> int:
        """
        :return: (int) Limite inferior do subconjunto de pedidos.
        """
        return self.__lower_bound

    def get_upper_bound(self) -> int:
        """
        :return: (int) Limite superior do subconjunto de pedidos.
        """
        return self.__upper_bound

    def add_order(self, order: Order):
        """
        Adiciona um pedido ao subconjunto.
        :param order: Pedido a ser adicionado ao subconjunto.
        """
        self.__orders.append(order)

    def get_orders_quantity(self) -> int:
        """
        :return:(int) Quantidade de pedidos no subconjunto.
        """
        return len(self.__orders)

    def add_visited_access(self, access: int):
        """
        Adiciona o id de um corredor visitado ao subconjunto.
        :param access: Id do coredor visitado.
        """
        self.__visited_accesses.append(access)

    def get_visited_accesses(self) -> list[int]:
        """
        :return:(list[int]) Lista de IDs dos corredores visitados no subconjunto.
        """
        return self.__visited_accesses

    def get_orders(self) -> list[Order]:
        """
        :return:(list[Order]) Lista de pedidos no subconjunto.
        """
        return self.__orders

    def empty_orders(self):
        """
        Esvazia lista de pedidos no subconjunto.
        """
        self.__orders = []

    def empty_visited_accesses(self):
        """
        Esvazia lista de corredores visitados no subconjunto.
        """
        self.__visited_accesses = []
