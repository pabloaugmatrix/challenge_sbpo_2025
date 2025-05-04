import sys
from pathlib import Path
from src.utils.benchmark.benchmark import Benchmark
from src.utils.data_loader.data_loader import DataLoader
from src.utils.wave_output_writer.wave_output_writer import WaveOutputWriter
from src.brute_force.brute_force import brute_force
from src.brute_force.heuristic import heuristic
from src.mockup import result_instance_0020

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
    # Visualização dos dados de entrada
    # data.view_data(input_file_name, warehouse, wave)
    # TESTE DE RESULTADO PARA INSTANCIA 20(Conforme o exemplo do desafio):
    # (ENQUANTO AINDA NAO HA NENHUM SOLVER)
    # wave = build_wave_with_orders_and_accesses(warehouse, wave)

    # benchmark = Benchmark(lambda: brute_force(warehouse, wave), "brute_force", input_file_name)
    # benchmark.file_print()

    heuristic(warehouse, wave)

    wave = result_instance_0020.build_wave_with_orders_and_accesses(warehouse, wave)
    # Gerando o arquivo de saída
    output_writer = WaveOutputWriter(wave)
    output_file_name = 'resultado_' + input_file_name
    output_file_path = Path('data/output/') / output_file_name
    output_writer.write_to_file(output_file_path)
