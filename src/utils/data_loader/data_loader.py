from src.entities.access.access import Access
from src.entities.backlog.backlog import Backlog
from src.entities.item.item import Item
from src.entities.order.order import Order
from src.entities.warehouse.warehouse import Warehouse
from src.entities.wave.wave import Wave


class DataLoader:
    """
    Classe responsavel por manipular os dados de entrada.

    Atributos:
        filepath (str): Caminho do arquivo de entrada.
    """

    def __init__(self, filepath):
        """
        Inciailiza um objeto do tipo DataLoader.
        :param filepath: Caminho do arquivo de entrada.
        """
        self.__filepath = filepath

    def load_data(self):
        """
        Abre e itera sobre o arquivo de entrada e retorna os dados devidamente instanciados.
        :return:
            warehouse (Warehouse): Instancia do objeto Warehouse.
            wave (Wave): Instancia do objeto Wave.
        """
        with open(self.__filepath, 'r') as file:
            lines = file.readlines()
        # Lê a primeira linha que contêm respectivamente:
        # o = quantidade de pedidos
        # i = quantidade de itens
        # a = quantidade de corredores
        o, i, a = map(int, lines[0].split())
        # Cria lista de pedidos(orders) para o backlog
        orders = []
        line_index = 1
        for order_id in range(o):
            data = list(map(int, lines[line_index].split()))
            line_index += 1
            items = [Item(data[j], data[j + 1]) for j in range(1, len(data), 2)]
            order = Order(order_id, items)
            orders.append(order)
        # Cria Backlog com a lista de pedidos (orders)
        backlog = Backlog(orders=orders)
        # Cria lista de corredores (Accesses) para o galpão(Warehouse)
        accesses = []
        for access_id in range(a):
            data = list(map(int, lines[line_index].split()))
            line_index += 1
            items = [Item(data[j], data[j + 1]) for j in range(1, len(data), 2)]
            accesses.append(Access(access_id, items))
        # Lê os limites(upper/lower bound) e cria a Wave
        LB, UB = map(int, lines[line_index].split())
        wave = Wave(LB, UB)
        # Cria o Warehouse com a lista de corredores(Acesses) e Backlog
        warehouse = Warehouse(accesses, backlog)
        return warehouse, wave

    def view_data(self, filename, warehouse: Warehouse, wave: Wave):
        """
        Busca os dados instanciados em Warehouse e Wave e imprime na tela.
        :param filename: Nome do arquivo de entrada.
        :param warehouse: Objeto Warehouse.
        :param wave: Objeto Wave.
        """
        print(f"Arquivo de entrada: {filename}")
        print("BACKLOG:")
        for order in warehouse.get_backlog().get_orders():
            print(f"Pedido {order.get_id()}: Itens [{', '.join(str(item.get_id()) for item in order.get_items())}]")
        print("CORREDORES:")
        for access in warehouse.get_accesses():
            print(f"Corredor {access.get_id()}: Itens [{', '.join(str(item.get_id()) for item in access.get_items())}]")
        print(f"Limite inferior: {wave.get_lower_bound()}")
        print(f"Limite superior: {wave.get_upper_bound()}")
