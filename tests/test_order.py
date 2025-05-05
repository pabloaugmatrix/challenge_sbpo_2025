import unittest

from src.entities.item.item import Item
from src.entities.order.order import Order


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.item1 = Item(item_id=1, item_quantity=2)
        self.item2 = Item(item_id=2, item_quantity=3)
        self.order = Order(order_id=101, items=[self.item1, self.item2])

    def test_get_id(self):
        self.assertEqual(self.order.get_id(), 101)

    def test_get_items(self):
        self.assertEqual(self.order.get_items(), [self.item1, self.item2])

    def test_get_length(self):
        self.assertEqual(self.order.get_length(), 5)

    def test_get_itemid_and_quantity_dict(self):
        expected_dict = {
            1: 2,
            2: 3
        }
        self.assertEqual(self.order.get_itemid_and_quantity_dict(), expected_dict)

    def test_str_representation(self):
        self.assertEqual(self.order.__str__(), self.order.get_id())
