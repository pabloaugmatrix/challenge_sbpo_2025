import unittest

from src.entities.item.item import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item(101, 5)

    def test_get_id(self):
        self.assertEqual(self.item.get_id(), 101)

    def test_get_item_quantity(self):
        self.assertEqual(self.item.get_item_quantity(), 5)

    def test_str_representation(self):
        self.assertEqual(self.item.__str__(), 101)

    def test_initialize_item(self):
        item = Item(202, 10)
        self.assertEqual(item.get_id(), 202)
        self.assertEqual(item.get_item_quantity(), 10)
