from src.entities.wave.wave import Wave


class WaveOutputWriter:
    """
    Classe responsavel por formatar e registrar os dados de saida.

    Atributos:
        wave (Wave): Objeto que representa uma wave.
    """

    def __init__(self, wave: Wave):
        """
        Inicializa um objeto do tipo WaveOutputWriter.
        :param wave: Objeto que representa uma wave.
        """
        self.__wave = wave

    def write_to_file(self, filepath: str):
        """
        Busca os dados de saida no objeto wave e os escreve em um arquivo.
        :param filepath: Caminho do arquivo de saida.
        """
        with open(filepath, 'w') as file:
            # Escreve o número de pedidos na wave
            file.write(f"{self.__wave.get_orders_quantity()}\n")
            # Escreve os índices dos pedidos
            for order in self.__wave.get_orders():
                file.write(f"{order.get_id()}\n")
                # Escreve o número de corredores visitados
            visited_accesses = self.__wave.get_visited_accesses()
            file.write(f"{len(visited_accesses)}\n")
            # Escreve os índices dos corredores visitados
            for access in visited_accesses:
                file.write(f"{access}\n")
