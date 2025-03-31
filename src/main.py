import sys
from pathlib import Path
from src.utils.data_loader.data_loader import DataLoader
from src.utils.wave_output_writer.wave_output_writer import WaveOutputWriter

if __name__ == '__main__':
    """
        (Linux)
        O programa deve ser executado na raiz do projeto com o comando:
        python3 -m src.main.py instance_number.txt
    """
    if len(sys.argv) < 2:
        print("Usage: python3 -m src.main.py instance_number.txt")
        sys.exit(1)
    # Pré processamento dos dados
    input_file_name = sys.argv[1]
    input_file_path = Path('data/input/') / input_file_name
    data = DataLoader(input_file_path)
    warehouse, wave = data.load_data()
    #Visualização dos dados de entrada
    data.view_data(input_file_name, warehouse, wave)
    # TESTE DE RESULTADO PARA INSTANCIA 20(Conforme o exemplo do desafio):
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
