import itertools
from collections import Counter

from src.entities.warehouse.warehouse import Warehouse
from src.entities.order.order import Order
import igraph as ig


class OrderGraph:
    def __init__(self, warehouse: Warehouse):
        self.__orders = warehouse.get_backlog().get_orders()
        self.__accesses = warehouse.get_accesses()
        self.__graph = ig.Graph()
        self.__init_vertices()
        self.__init_edges()

    def __init_vertices(self):
        for order in self.__orders:
            self.__graph.add_vertex(order.get_id())

    def __get__better_access_combination(self, order_combination: list):
        total_demand = Counter()
        for order in order_combination:
            total_demand.update(order.get_itemid_and_quantity_dict())
        access_combination = []
        accesses = self.__accesses
        for i in range(1, len(accesses) + 1):
            access_combination.extend(itertools.combinations(accesses, i))
        for accesses in access_combination:
            total_stock = Counter()
            for access in accesses:
                total_stock.update(access.get_itemid_and_quantity_dict())
            if all(total_stock[item] >= qtd for item, qtd in total_demand.items()):
                return accesses
        return None

    def __init_weigths(self, order1: Order, order2: Order):
        access_combination = self.__get__better_access_combination([order1, order2])
        return len(access_combination)

    def __init_edges(self):
        order_pair = []
        order_pair.extend(itertools.combinations(self.__orders, 2))
        for order1, order2 in order_pair:
            self.__graph.add_edge(source=order1.get_id(),target= order2.get_id(), weight=self.__init_weigths(order1, order2))
            print(self.__init_weigths(order1, order2))

    def get_graph(self):
        return self.__graph
