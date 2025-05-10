from copy import deepcopy
import random
import cProfile
from src.entities.objective_function.objective_function import ObjectiveFunction
from src.entities.warehouse.warehouse import Warehouse
from src.utils.benchmark.benchmark import Benchmark
from src.entities.wave.wave import Wave
from src.brute_force.utils import *

def process_accesses(wave: Wave, accesses, backlog, listOrder):
    orderVisited = set()
    list_set = []
    qtd = [0]
    objective_calculator = ObjectiveFunction(wave)

    for access in accesses:
        if access and access.get_id() in [a.get_id() for a in wave.get_visited_accesses()]:
            continue

        temp_items = wave.get_itensDePedidosAtendidos_wave().copy()
        for item in access.get_items():
            item_id = item.get_id()
            temp_items[item_id] = temp_items.get(item_id, 0) + item.get_item_quantity()

        if not objective_calculator.capacidadeMax(temp_items, listOrder, list_set, qtd, wave):
            break

        for order in backlog:
            if order.get_id() not in list_set and order.get_id() not in orderVisited and order not in wave.get_orders():
                orderVisited.add(order.get_id())
                wave.add_order(order)

        wave.add_itensDePedidosAtendidos_wave(temp_items)
        wave.add_visited_access(access)
        wave.add_itemsMax(qtd[0])
        qtd[0] = 0

    wave.add_score_wave(objective_calculator.calculate_objective())
    return wave

def getWave(accesses, backlog, listOrder, wave: Wave):
    return process_accesses(wave, accesses, backlog, listOrder)

def refineWave(wave: Wave, accesses, backlog, listOrder, max_swaps=10):
    bestWave = wave
    bestScore = wave.get_score_wave()

    visited_ids = {a.get_id() for a in wave.get_visited_accesses()}
    access_not_visited = [a for a in accesses if a.get_id() not in visited_ids]

    epoch = 0
    for access in wave.get_visited_accesses():
        for new_access in access_not_visited:
            if epoch >= max_swaps:
                break
            nova_ids = visited_ids.copy()
            nova_ids.remove(access.get_id())
            nova_ids.add(new_access.get_id())

            nova_accesses = [a for a in accesses if a.get_id() in nova_ids]
            nova_wave = Wave(wave.get_lower_bound(), wave.get_upper_bound())

            nova_wave = process_accesses(nova_wave, nova_accesses, backlog, listOrder)

            if nova_wave and nova_wave.get_score_wave() > bestScore:
                bestWave = nova_wave
                bestScore = nova_wave.get_score_wave()
            epoch += 1

    return bestWave

def waveGulosa(wave: Wave, backlog, listOrder, accesses):
    accesses = sortAccess(accesses)
    return getWave(accesses, backlog, listOrder, wave)

def waveRandom(wave: Wave, backlog, listOrder, accesses):
    random.shuffle(accesses)
    return getWave(accesses, backlog, listOrder, wave)

def heuristic(warehouse: Warehouse, wave: Wave, input_file_name):
    backlog = warehouse.get_backlog().get_orders()
    listOrder = getOrderList(backlog)
    accesses = deepcopy(warehouse.get_accesses())    

    # benchmark = Benchmark(lambda: waveRandom(wave, backlog, listOrder, accesses), "waveRandom", input_file_name)
    # benchmark.file_print()
    # printWave(wave, 'Aleatoria ')

    benchmark = Benchmark(lambda: waveGulosa(wave, backlog, listOrder, accesses), "waveGulosa", input_file_name)
    benchmark.file_print()
    printWave(wave, 'Gulosa ')
    
    # profiler = cProfile.Profile()
    # profiler.enable()
    benchmark = Benchmark(lambda: refineWave(wave, accesses, backlog, listOrder), "refineWave", input_file_name)
    benchmark.file_print()
    bestWave = refineWave(wave, accesses, backlog, listOrder)
    
    # # profiler.disable()
    # # profiler.print_stats(sort='cumtime')
    
    printWave(bestWave, 'Refinamento ')