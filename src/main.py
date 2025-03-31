import sys
from pathlib import Path

from src.entities.item.item import Item
from src.entities.order.order import Order
from src.entities.wave.wave import Wave
from src.utils.data_loader.data_loader import DataLoader
from src.utils.wave_output_writer.wave_output_writer import WaveOutputWriter

if __name__ ==  '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py instance_name.txt")
        sys.exit(1)
    input_file_name = sys.argv[1]
    input_file_path = Path('data/input/') / input_file_name
    data = DataLoader(input_file_path)
    warehouse, wave = data.load_data()

    # TESTE DE RESULTADO PARA INSTANCIA 20:
    # (ENQUANTO AINDA NAO HA NENHUM SOLVER)

    # Recuperando pedidos do backlog
    order0 = warehouse.get_backlog().get_order(0)
    order1 = warehouse.get_backlog().get_order(1)
    order2 = warehouse.get_backlog().get_order(2)
    order4 = warehouse.get_backlog().get_order(4)

    # Adicionando os pedidos à wave
    wave.add_order(order0)
    wave.add_order(order1)
    wave.add_order(order2)
    wave.add_order(order4)

    # Adicionando os corredores visitados
    wave.add_visited_access(1)
    wave.add_visited_access(3)

    # Gerando o arquivo de saída
    output_writer = WaveOutputWriter(wave)
    output_file_name = 'resultado_' + input_file_name
    output_file_path = Path('data/output/') / output_file_name
    output_writer.write_to_file(output_file_path)



