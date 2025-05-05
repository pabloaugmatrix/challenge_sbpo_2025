import unittest

from src.entities.access.access import Access
from src.entities.item.item import Item


class TestAccess(unittest.TestCase):

    def setUp(self):
        self.item1 = Item(1, 10)
        self.item2 = Item(2, 15)
        self.item3 = Item(3, 5)

    def test_initialize_access(self):
        access = Access(1, [self.item1, self.item2, self.item3])
        self.assertEqual(access.get_id(), 1)
        self.assertEqual(access.get_items(), [self.item1, self.item2, self.item3])

    def test_retrieve_access_length(self):
        access = Access(1, [self.item1, self.item2, self.item3])
        self.assertEqual(access.get_length(), 30)

    def test_retrieve_itemid_and_quantity(self):
        access = Access(1, [self.item1, self.item2, self.item3])
        expected_result = {1: 10, 2: 15, 3: 5}
        self.assertEqual(access.get_itemid_and_quantity_dict(), expected_result)

    def test__str__(self):
        access = Access(1, [self.item1, self.item2, self.item3])
        self.assertEqual(access.__str__(), 1)
