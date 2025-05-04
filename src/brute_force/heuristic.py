from os import access
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
    
    print(listOrder)
    return listOrder

def getWaveGulosa(warehouse: Warehouse, wave: Wave):
    backlog = warehouse.get_backlog().get_orders()
    accesses = warehouse.get_accesses()
    accesses = sortAccess(accesses)
    listOrder = getOrder(backlog)

    list = []
    qtd = [0]
    orderVisited = []
    objective_calculator = ObjectiveFunction(wave)

    for access in accesses:
        temp_itensDePedidosAtendidos = wave.get_itensDePedidosAtendidos_wave().copy()
        items = access.get_items()

        for item in items:
            item_id = item.get_id()
            item_quantidade = item.get_item_quantity()
            temp_itensDePedidosAtendidos[item_id] = temp_itensDePedidosAtendidos.get(item_id, 0) + item_quantidade
            
            
        if not objective_calculator.capacidadeMax(temp_itensDePedidosAtendidos, listOrder, list, qtd, wave):
            for order in backlog:
                for i in range(0, len(list)):
                    if order.get_id() == list[i] and order.get_id() not in orderVisited:
                        orderVisited.append(order.get_id())
                        wave.add_order(order)
            break

        for order in backlog:
            for i in range(0, len(list)):
                if order.get_id() == list[i] and order.get_id() not in orderVisited:
                    orderVisited.append(order.get_id())
                    wave.add_order(order)
                    

        wave.add_itensDePedidosAtendidos_wave(temp_itensDePedidosAtendidos)
        wave.add_visited_access(access)
        
    wave.add_score_wave(objective_calculator.calculate_objective())

    for access in wave.get_visited_accesses():
        print(wave.get_accesses_quantity())    
    for access in wave.get_orders():
        print(wave.get_orders_quantity())    
    print(wave.get_score_wave())    

def getAccessList(warehouse):
    corredores = []
    access = warehouse.get_accesses()

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
    
    print(corredores)
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

    print(orderList)
    return orderList


def refineWave():
    pass

def getWaveRandom():
    pass

def heuristic(warehouse: Warehouse, wave: Wave):
    getWaveGulosa(warehouse, wave)
    getWaveRandom()

    refineWave()