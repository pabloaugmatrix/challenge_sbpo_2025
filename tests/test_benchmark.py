import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from src.utils.benchmark.benchmark import Benchmark


class TestBenchmark(unittest.TestCase):
    def setUp(self):
        self.mock_method = MagicMock()
        self.benchmark = Benchmark(
            method=self.mock_method,
            method_name="mock_method",
            instancename="TestInstance"
        )

    @patch('src.utils.benchmark.benchmark.timeit.timeit', return_value=5.0)
    def test_execution_time(self, mock_timeit):
        result = self.benchmark.execution_time(number=10)
        self.assertEqual(result, 0.5)
        mock_timeit.assert_called_once_with(self.mock_method, number=10)

    def test_execution_time_with_different_number(self):
        with patch('src.utils.benchmark.benchmark.timeit.timeit', return_value=10.0) as mock_timeit:
            result = self.benchmark.execution_time(number=20)
            self.assertEqual(result, 0.5)
            mock_timeit.assert_called_once_with(self.mock_method, number=20)

    @patch('src.utils.benchmark.benchmark.datetime')
    @patch('src.utils.benchmark.benchmark.Path')
    @patch('builtins.open')
    def test_file_print(self, mock_open, mock_path_class, mock_datetime):
        # Mock timestamp
        mock_datetime.now.return_value.strftime.return_value = "20230101_120000"

        # Mock open() context
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file

        # Mock Path behavior
        mock_path_instance = MagicMock()
        mock_path_class.return_value = mock_path_instance
        mock_path_instance.__truediv__.return_value = mock_path_instance
        mock_path_instance.parent.mkdir = MagicMock()

        # Patch execution_time to return 0.5
        with patch.object(self.benchmark, 'execution_time', return_value=0.5):
            self.benchmark.file_print(number=10)

        mock_path_instance.parent.mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_file.write.assert_any_call("method,instance,timestamp,average_time_seconds,executions\n")
        mock_file.write.assert_any_call("mock_method,TestInstance,20230101_120000,0.500000,10\n")
