import unittest

from src.entities.backlog.backlog import Backlog
from src.entities.item.item import Item
from src.entities.order.order import Order


class TestBacklog(unittest.TestCase):
    def setUp(self):
        self.item1 = Item(1, 10)
        self.item2 = Item(2, 20)
        self.item3 = Item(3, 15)
        self.order1 = Order(101, [self.item1, self.item2])
        self.order2 = Order(102, [self.item3])
        self.backlog = Backlog([self.order1, self.order2])

    def test_get_orders(self):
        orders = self.backlog.get_orders()
        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0].get_id(), 101)
        self.assertEqual(orders[1].get_id(), 102)

    def test_get_order(self):
        order = self.backlog.get_order(101)
        self.assertEqual(order.get_id(), 101)
        self.assertEqual(order.get_items(), [self.item1, self.item2])

    def test_get_order_not_in_backlog(self):
        with self.assertRaises(ValueError):
            self.backlog.get_order(999)

