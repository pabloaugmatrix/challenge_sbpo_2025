from src.entities.warehouse.warehouse import Warehouse
from src.entities.wave.wave import Wave


def build_wave_with_orders_and_accesses(warehouse: Warehouse, wave: Wave) -> Wave:
    # Adicionando os pedidos à wave
    for i in [0, 1, 2, 4]:
        wave.add_order(warehouse.get_backlog().get_order(i))
    # Adicionando os corredores visitados
    for access in [1, 3]:
        wave.add_visited_access(warehouse.get_access(access))
    return wave
