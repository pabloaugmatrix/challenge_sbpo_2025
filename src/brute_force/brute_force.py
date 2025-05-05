from src.entities.wave.wave import Wave
from copy import deepcopy


class ObjectiveFunction:
    def __init__(self, wave: Wave):
        self.__wave = wave

    def calculate_objective(self):
        """
        Busca quantidade de corredores e pedidos no subconjunto
        para então calcular a função objetivo(corredores / pedidos).
        :return: Valor da função objetivo(corredores / pedidos).
        """
        # accesses_quantity = self.__wave.get_accesses_quantity()
        # orders_quantity = self.__wave.get_orders_quantity()
        # return accesses_quantity / orders_quantity

        accesses_quantity = self.__wave.get_accesses_quantity()
        orders_quantity = self.__wave.get_itemsMax()
        return orders_quantity / accesses_quantity

    def capacidadeMax(self, itensDePedidosAtendidos, listOrder, list_ids, qtd, wave: Wave):
        consumed_items = {}
        temp_qtd = 0

        for order in listOrder:
            order_id = order['id']
            order_items = order['listOrder']

            pedido_atendido = all(
                (itensDePedidosAtendidos.get(id_pedido, 0) - consumed_items.get(id_pedido, 0)) >= qtd_pedido
                for id_pedido, qtd_pedido in order_items.items()
            )

            if pedido_atendido:
                for id_pedido, qtd_pedido in order_items.items():
                    consumed_items[id_pedido] = consumed_items.get(id_pedido, 0) + qtd_pedido

                temp_qtd += sum(order_items.values())

                if order_id not in list_ids:
                    list_ids.append(order_id)

        qtd[0] = temp_qtd

        upper_bound = wave.get_upper_bound()
        if upper_bound is not None:
            return temp_qtd <= upper_bound

        lower_bound = wave.get_lower_bound()
        if lower_bound is not None:
            return temp_qtd >= lower_bound

        return True