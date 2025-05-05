from src.entities.wave.wave import Wave


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
        if orders_quantity == 0:
            raise ZeroDivisionError
        return accesses_quantity / orders_quantity
