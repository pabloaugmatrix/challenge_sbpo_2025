import unittest

from src.entities.access.access import Access
from src.entities.backlog.backlog import Backlog
from src.entities.warehouse.warehouse import Warehouse


class TestWarehouse(unittest.TestCase):
    def setUp(self):
        self.access1 = Access(1, [])
        self.access2 = Access(2, [])
        self.backlog = Backlog([])
        self.warehouse = Warehouse([self.access1, self.access2], self.backlog)

    def test_get_accesses(self):
        self.assertEqual(self.warehouse.get_accesses(), [self.access1, self.access2])

    def test_get_access_by_id(self):
        access = self.warehouse.get_access(1)
        self.assertEqual(access, self.access1)

    def test_get_backlog(self):
        self.assertEqual(self.warehouse.get_backlog(), self.backlog)

    def test_get_access_invalid_id(self):
        with self.assertRaises(ValueError):
            self.backlog.get_order(99)
