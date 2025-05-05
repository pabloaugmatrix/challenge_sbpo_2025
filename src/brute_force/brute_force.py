import itertools
from collections import Counter
from src.entities.warehouse.warehouse import Warehouse
from src.entities.wave.wave import Wave


def __viable_orders_combination(warehouse: Warehouse, wave: Wave):
    backlog = warehouse.get_backlog().get_orders()
    order_combination = []
    for i in range(1, len(backlog) + 1):
        order_combination.extend(itertools.combinations(backlog, i))
    viable_list = []
    for combination in order_combination:
        total_len = sum(order.get_length() for order in combination)
        if wave.get_lower_bound() <= total_len <= wave.get_upper_bound():
            viable_list.append(combination)
    return viable_list


def __get__better_access_combination(warehouse: Warehouse, wave: Wave, order_combination: list):
    total_demand = Counter()
    for order in order_combination:
        total_demand.update(order.get_itemid_and_quantity_dict())
    access_combination = []
    accesses = warehouse.get_accesses()
    for i in range(1, len(accesses) + 1):
        access_combination.extend(itertools.combinations(accesses, i))
    for accesses in access_combination:
        total_stock = Counter()
        for access in accesses:
            total_stock.update(access.get_itemid_and_quantity_dict())
        if all(total_stock[item] >= qtd for item, qtd in total_demand.items()):
            return accesses
    return None


def brute_force(warehouse: Warehouse, wave: Wave):
    order_combinations = __viable_orders_combination(warehouse, wave)
    viable_dict = {}
    objective = float('inf')
    for combination in order_combinations:
        access_combination = __get__better_access_combination(warehouse, wave, combination)
        if access_combination:
            viable_dict[combination] = access_combination
    for orders_tuple, accesses_list in viable_dict.items():
        total_order_len = sum(order.get_length() for order in orders_tuple)
        total_access_len = sum(access.get_length() for access in accesses_list)
        if total_access_len == 0:
            continue
        score = total_access_len / total_order_len
        if score < objective:
            objective = score
            wave.empty_orders()
            wave.empty_visited_accesses()
            for order in orders_tuple:
                wave.add_order(order)
            for access in accesses_list:
                wave.add_visited_access(access)
    return wave
