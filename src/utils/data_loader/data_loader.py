from src.entities.access.access import Access
from src.entities.backlog.backlog import Backlog
from src.entities.item.item import Item
from src.entities.order.order import Order
from src.entities.warehouse.warehouse import Warehouse
from src.entities.wave.wave import Wave


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.warehouse = None

    def load_data(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        # 1. Ler a primeira linha
        o, i, a = map(int, lines[0].split())

        # 2. Criar lista de pedidos
        orders = []
        line_index = 1
        for order_id in range(o):
            data = list(map(int, lines[line_index].split()))
            line_index += 1
            k = data[0]
            items = [Item(data[j], data[j + 1]) for j in range(1, len(data), 2)]
            order = Order(order_id, items)
            orders.append(order)

        # 3. Criar Backlog com a lista de pedidos
        backlog = Backlog(orders=orders)

        # 4. Criar lista de corredores (Access)
        accesses = []
        for access_id in range(a):
            data = list(map(int, lines[line_index].split()))
            line_index += 1
            l = data[0]
            items = [Item(data[j], data[j + 1]) for j in range(1, len(data), 2)]
            accesses.append(Access(access_id, items))

        # 5. Ler os limites da wave
        LB, UB = map(int, lines[line_index].split())
        wave = Wave( LB, UB)

        # 6. Criar Warehouse e associar backlog e corredores
        self.warehouse = Warehouse(accesses, backlog)
        return self.warehouse, wave
