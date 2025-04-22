import timeit
from pathlib import Path
from datetime import datetime


class Benchmark:
    def __init__(self, method, method_name: str, instancename: str):
        self.__method = method
        self.__method_name = method_name
        self.__instancename = instancename

    def execution_time(self, number=10):
        total_time = timeit.timeit(self.__method, number=number)
        return total_time / number

    def file_print(self, number=10):
        avg_time = self.execution_time(number)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"benchmark_{self.__method_name}_{self.__instancename}_{timestamp}.csv"
        filepath = Path('data/output') / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as file:
            file.write("method,instance,timestamp,average_time_seconds,executions\n")
            file.write(f"{self.__method_name},{self.__instancename},{timestamp},{avg_time:.6f},{number}\n")
