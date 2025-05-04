from copy import deepcopy
import itertools
from os import access
import random
from statistics import quantiles
from src.entities.objective_function.objective_function import ObjectiveFunction
from src.entities.warehouse.warehouse import Warehouse
from src.entities.wave.wave import Wave

def sortAccess(accesses):
    listAccess = list(accesses)
    
    listAccess.sort(key=lambda access: access.get_length(), reverse=True)
    listAccess.sort(key=lambda access: access.get_length_max_item(), reverse=True)

    return listAccess

def getOrder(backlog):
    listOrder = []

    for order in backlog:
        pedido = {
            'id': order.get_id(),
            'listOrder': order.get_itemid_and_quantity_dict()
        }
        listOrder.append(pedido)
    
    return listOrder

def getAccessList(warehouse):
    corredores = []
    access = deepcopy(warehouse.get_accesses())

    for acess in access:
        qtd = 0
        corredor = {
            'id': acess.get_id(),
            'qtdItemAtendido': 0,
            'itens': [],
            'maxItem': 0
        }

        items = acess.get_items()

        for item in items:
            qtd += item.get_item_quantity()
            corredor['itens'].append(item.get_id())
            corredor['itens'].append(item.get_item_quantity())

        corredor['qtdItemAtendido'] = len(corredor['itens'])/2
        corredor['maxItem'] = qtd
        corredores.append(corredor)
    
    return corredores

def getOrderList(warehouse: Warehouse):
    backlog = warehouse.get_backlog().get_orders()
    orderList = []

    for orders in backlog:
        order = {
            'id': orders.get_id(),
            'orderList': orders.get_itemid_and_quantity_dict()
        }
        orderList.append(order)

    return orderList

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
            print(qtd)
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
    print(wave.get_itemsMax())
        
    wave.add_score_wave(objective_calculator.calculate_objective())

    for access in wave.get_visited_accesses():
        print(f'Access: {access.get_id()}')    
    print()
    for orders in wave.get_orders():
        print(f'Orders: {orders.get_id()}')    
    print(f'Score: {wave.get_score_wave()}') 

    print(f'Corredor visitado: {wave.get_accesses_quantity()}')   
    print(f'Pedido coletado: {wave.get_orders_quantity()}')    
    print(f'Score: {wave.get_score_wave()}')     


def waveGulosa(warehouse: Warehouse, wave: Wave):
    backlog = warehouse.get_backlog().get_orders()
    listOrder = getOrder(backlog)
    
    accesses = deepcopy(warehouse.get_accesses())
    accesses = sortAccess(accesses)

    getWave(accesses, backlog, listOrder, wave)

    
def refineWave():
    pass

def waveRandom(warehouse: Warehouse, wave: Wave):
    backlog = warehouse.get_backlog().get_orders()
    listOrder = getOrder(backlog)

    accesses = deepcopy(warehouse.get_accesses())
    random.shuffle(accesses)

    getWave(accesses, backlog, listOrder, wave)

def heuristic(warehouse: Warehouse, wave: Wave):
    # waveGulosa(warehouse, wave)
    waveRandom(warehouse, wave)

    refineWave()