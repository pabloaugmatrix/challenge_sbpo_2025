from src.entities.wave.wave import Wave


class WaveOutputWriter:
    def __init__(self, wave: Wave):
        self.wave = wave

    def write_to_file(self, filename: str):
        with open(filename, 'w') as file:
            # Escreve o número de pedidos na wave
            file.write(f"{self.wave.get_orders_quantity()}\n")

            # Escreve os índices dos pedidos
            for order in self.wave.get_orders():
                file.write(f"{order.get_id()}\n")  # Acessando o ID do pedido

            # Escreve o número de corredores visitados
            visited_accesses = self.wave.get_visited_accesses()
            file.write(f"{len(visited_accesses)}\n")

            # Escreve os índices dos corredores visitados
            for access in visited_accesses:
                file.write(f"{access}\n")
