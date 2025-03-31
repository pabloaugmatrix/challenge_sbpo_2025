from src.entities.order.order import Order


class Backlog:
    """
    Representa o backlog de pedidos do galpão.

    Atributos:
        orders (list[Order]): lista de pedidos no backlog.
    """

    def __init__(self, orders: list[Order]) -> None:
        """
        Inicializa um objeto do tipo Backlog.
        :param orders: Lista de pedidos no backlog.
        """
        self.__orders = orders

    def get_orders(self) -> list[Order]:
        """
        :return: (list[Order]) Lista de pedidos no backlog.
        """
        return self.__orders

    def get_order(self, order_id: int) -> Order:
        """
        Itera pelos pedidos no backlog e retorna o pedido com o id informado.
        :param order_id: Id do pedido a ser buscado.
        :return: (Order) Pedido com o id informado.
        """
        for order in self.__orders:
            if order.get_id() == order_id:
                return order
