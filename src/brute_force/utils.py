from copy import deepcopy
from src.entities.wave.wave import Wave

def sortAccess(accesses):
    listAccess = list(accesses)
    
    listAccess.sort(key=lambda access: access.get_length(), reverse=True)
    listAccess.sort(key=lambda access: access.get_length_max_item(), reverse=True)

    return listAccess

def getOrderList(backlog):
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

def printWave(wave: Wave):
    orderList = []
    accessList = []

    for access in wave.get_visited_accesses():
        accessList.append(access.get_id())    
    for orders in wave.get_orders():
        orderList.append(orders.get_id())  

    orderList.sort()
    accessList.sort()
    print()
    print('-'*8+' Resultado '+'-'*8)
    print(f"Access: {accessList}")
    print(f"Orders: {orderList}")
    print(f'Score: {wave.get_score_wave()}') 
    print(f'Corredor visitado: {wave.get_accesses_quantity()}')   
    print(f'Pedido coletado: {wave.get_orders_quantity()}')    
    print(f'Score: {wave.get_score_wave()}') 
