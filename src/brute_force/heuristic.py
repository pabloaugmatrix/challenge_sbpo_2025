from copy import deepcopy
import itertools
from os import access
import random
from statistics import quantiles
from src.entities.objective_function.objective_function import ObjectiveFunction
from src.entities.warehouse.warehouse import Warehouse
from src.entities.wave.wave import Wave
from src.brute_force.utils import *


def getNewWave(wave: Wave, backlog, listOrder):
    newWave = Wave(wave.get_lower_bound(), wave.get_upper_bound())

    newAccessVisited = []
    orderVisited = []
    list = []
    qtd = [0]
    objective_calculator = ObjectiveFunction(newWave)

    for access in wave.get_visited_accesses():
        newAccessVisited.append(access)

    for access in newAccessVisited:

        temp_itensDePedidosAtendidos = newWave.get_itensDePedidosAtendidos_wave().copy()
        items = access.get_items()

        for item in items:
            item_id = item.get_id()
            item_quantidade = item.get_item_quantity()
            temp_itensDePedidosAtendidos[item_id] = temp_itensDePedidosAtendidos.get(item_id, 0) + item_quantidade
            
        if not objective_calculator.capacidadeMax(temp_itensDePedidosAtendidos, listOrder, list, qtd, newWave):
            break

        for order in backlog:
            for i in range(0, len(list)):
                if order.get_id() == list[i] and order.get_id() not in orderVisited:
                    orderVisited.append(order.get_id())
                    newWave.add_order(order)
                            
        newWave.add_itensDePedidosAtendidos_wave(temp_itensDePedidosAtendidos)
        newWave.add_visited_access(access)
        newWave.add_itemsMax(qtd[0])
        qtd[0] = 0
        
    newWave.add_score_wave(objective_calculator.calculate_objective())

    return newWave

def getWave(accesses, backlog, listOrder, wave: Wave):
    list = []
    qtd = [0]
    orderVisited = []
    objective_calculator = ObjectiveFunction(wave)

    for access in accesses:
        if access.get_id() in wave.get_visited_accesses():
            continue

        temp_itensDePedidosAtendidos = wave.get_itensDePedidosAtendidos_wave().copy()
        items = access.get_items()

        for item in items:
            item_id = item.get_id()
            item_quantidade = item.get_item_quantity()
            temp_itensDePedidosAtendidos[item_id] = temp_itensDePedidosAtendidos.get(item_id, 0) + item_quantidade
            
            
        if not objective_calculator.capacidadeMax(temp_itensDePedidosAtendidos, listOrder, list, qtd, wave):
            break

        for order in backlog:
            for i in range(0, len(list)):
                if order.get_id() == list[i] and order.get_id() not in orderVisited:
                    orderVisited.append(order.get_id())
                    wave.add_order(order)
                            
        wave.add_itensDePedidosAtendidos_wave(temp_itensDePedidosAtendidos)
        wave.add_visited_access(access)
        wave.add_itemsMax(qtd[0])
        qtd[0] = 0
        
    wave.add_score_wave(objective_calculator.calculate_objective())

    return wave    

def refineWave(wave: Wave, accesses, backlog, listOrder):
    bestScore = wave.get_score_wave()
    tempWave = deepcopy(wave)
    bestWave = deepcopy(wave)

    accessList = tempWave.get_visited_accesses()

    accessVisited = []
    accessVisitedID = []
    accessNotVisited = []

    for access in accessList:
        accessVisited.append(access)
        accessVisitedID.append(access.get_id())

    for acess in accesses:
        if acess.get_id() not in accessVisitedID:
            accessNotVisited.append(acess)

    for access in tempWave.get_visited_accesses():
        for newAccess in accessNotVisited:

            tempWave.remove_visited_access(access)
            if newAccess not in tempWave.get_visited_accesses():
                tempWave.add_visited_access(newAccess)

            newWave = getNewWave(tempWave, backlog, listOrder)

            if newWave and newWave.get_score_wave() > bestScore:
                bestWave = newWave
                bestScore = newWave.get_score_wave()
    
    return bestWave

def waveGulosa(wave: Wave, backlog, listOrder, accesses):
    accesses = sortAccess(accesses)

    return getWave(accesses, backlog, listOrder, wave)

def waveRandom(wave: Wave, backlog, listOrder, accesses):
    random.shuffle(accesses)

    return getWave(accesses, backlog, listOrder, wave)

def heuristic(warehouse: Warehouse, wave: Wave):
    backlog = warehouse.get_backlog().get_orders()
    listOrder = getOrderList(backlog)
    accesses = deepcopy(warehouse.get_accesses())

    wave = waveGulosa(wave, backlog, listOrder, accesses)
    # wave = waveRandom(wave, backlog, listOrder, accesses)

    printWave(wave)
    
    bestWave = refineWave(wave, accesses, backlog, listOrder)

    printWave(bestWave)