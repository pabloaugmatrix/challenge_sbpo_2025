# tests/test_wave.py

import unittest

from src.entities.access.access import Access
from src.entities.item.item import Item
from src.entities.order.order import Order
from src.entities.wave.wave import Wave


class TestWave(unittest.TestCase):

    def setUp(self):
        self.order1 = Order(1, [])
        self.order2 = Order(2, [])
        self.item1 = Item(1, 0)
        self.access1 = Access(1, [])

    def test_initialize_wave(self):
        wave = Wave(10, 20)
        self.assertEqual(wave.get_lower_bound(), 10)
        self.assertEqual(wave.get_upper_bound(), 20)
        self.assertEqual(wave.get_orders_quantity(), 0)
        self.assertEqual(wave.get_accesses_quantity(), 0)

    def test_add_and_retrieve_order(self):
        wave = Wave(10, 20)
        order = self.order1
        wave.add_order(order)
        self.assertEqual(wave.get_orders_quantity(), 1)
        self.assertIn(order, wave.get_orders())

    def test_empty_orders(self):
        wave = Wave(10, 20)
        order = self.order1
        wave.add_order(order)
        wave.empty_orders()
        self.assertEqual(wave.get_orders_quantity(), 0)
        self.assertEqual(wave.get_orders(), [])

    def test_add_and_retrieve_visited_access(self):
        wave = Wave(10, 20)
        access = self.access1
        wave.add_visited_access(access)
        self.assertEqual(wave.get_accesses_quantity(), 1)
        self.assertIn(access, wave.get_visited_accesses())

    def test_empty_visited_accesses(self):
        wave = Wave(10, 20)
        access = self.access1
        wave.add_visited_access(access)
        wave.empty_visited_accesses()
        self.assertEqual(wave.get_accesses_quantity(), 0)
        self.assertEqual(wave.get_visited_accesses(), [])

    def test_multiple_orders(self):
        wave = Wave(0, 50)
        order1 = self.order1
        order2 = self.order2
        wave.add_order(order1)
        wave.add_order(order2)
        self.assertEqual(wave.get_orders_quantity(), 2)
        self.assertIn(order1, wave.get_orders())
        self.assertIn(order2, wave.get_orders())
