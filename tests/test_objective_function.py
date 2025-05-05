import unittest

from src.entities.access.access import Access
from src.entities.item.item import Item
from src.entities.objective_function.objective_function import ObjectiveFunction
from src.entities.order.order import Order
from src.entities.wave.wave import Wave


class TestObjectiveFunction(unittest.TestCase):
    def setUp(self):
        self.wave = Wave(lower_bound=1, upper_bound=10)
        self.objective_function = ObjectiveFunction(self.wave)
        self.item1 = Item(1, 10)
        self.item2 = Item(2, 15)
        self.item3 = Item(3, 5)
        self.order1 = Order(101, [self.item1, self.item2])
        self.order2 = Order(102, [self.item3])
        self.order3 = Order(103, [self.item1, self.item3])
        self.access1 = Access(1, [self.item1, self.item2, self.item3])
        self.access2 = Access(2, [self.item1, self.item2])
        self.access3 = Access(3, [self.item1, self.item3])

    def test_calculate_objective_with_valid_values(self):
        self.wave.add_visited_access(self.access1)
        self.wave.add_visited_access(self.access2)
        self.wave.add_order(self.order1)
        self.wave.add_order(self.order2)
        expected_result = self.wave.get_itemsMax()/self.wave.get_accesses_quantity()
        self.assertEqual(self.objective_function.calculate_objective(), expected_result)

    def test_calculate_objective_when_no_orders(self):
        self.wave.add_visited_access(self.access1)
        self.assertEqual(self.objective_function.calculate_objective(), 0 / 1)

    def test_calculate_objective_with_no_accesses(self):
        self.wave.add_order(self.order1)
        self.wave.add_order(self.order2)
        with self.assertRaises(ZeroDivisionError):
            self.objective_function.calculate_objective()

    def test_calculate_objective_with_multiple_orders_and_accesses(self):
        self.wave.add_visited_access(self.access1)
        self.wave.add_visited_access(self.access2)
        self.wave.add_visited_access(self.access3)
        self.wave.add_order(self.order1)
        self.wave.add_order(self.order2)
        self.wave.add_order(self.order3)
        expected_result = self.wave.get_itemsMax() / self.wave.get_accesses_quantity()
        self.assertAlmostEqual(self.objective_function.calculate_objective(), expected_result)
