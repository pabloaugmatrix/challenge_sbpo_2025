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
        accesses_quantity = self.__wave.get_accesses_quantity()
        orders_quantity = self.__wave.get_orders_quantity()
        return accesses_quantity / orders_quantity
    
    def capacidadeMax(self, itensDePedidosAtendidos, listOrder, list, qtd, wave: Wave):
        temp_itensDePedidosAtendidos = deepcopy(itensDePedidosAtendidos)
        temp_orderDic = deepcopy(listOrder)

        for order in temp_orderDic:
            listOrder = order['listOrder']

            pedido_atendido = True
            for id_pedido, qtd_pedido in listOrder.items():
                if temp_itensDePedidosAtendidos.get(id_pedido, 0) < qtd_pedido:
                    pedido_atendido = False
                    continue

            if pedido_atendido:
                for id_pedido, qtd_pedido in listOrder.items():
                    temp_itensDePedidosAtendidos[id_pedido] -= qtd_pedido
                    qtd[0] += qtd_pedido
                    if order['id'] not in list:
                        list.append(order['id'])
        
        if wave.get_upper_bound() is not None:
            if not qtd[0] < wave.get_upper_bound():
                list.pop()
            return qtd[0] < wave.get_upper_bound()
        if wave.get_lower_bound() is not None:
            return qtd[0] > wave.get_lower_bound()
    
