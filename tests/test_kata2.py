import unittest
from src.kata2 import get_total
from src.kata1 import Dictionary


class TestKata2(unittest.TestCase):
    def setUp(self):
        self.costs = Dictionary()

    def test_description_example(self):
        self.costs.newentry('socks', 5)
        self.costs.newentry('shoes', 60)
        self.costs.newentry('sweater', 30)
        items_bought = ['socks', 'shoes']
        tax = 0.09
        total = get_total(self.costs, items_bought, tax)
        self.assertEqual(total, 70.85)

    def test_item_not_in_costs(self):
        self.costs.newentry('socks', 5)
        self.costs.newentry('shoes', 60)
        self.costs.newentry('sweater', 30)
        items_bought = ['socks', 'shoes', 'key']
        tax = 0.09
        total = get_total(self.costs, items_bought, tax)
        self.assertEqual(total, 70.85)

    def test_null_key(self):
        self.costs.newentry('socks', 5)
        self.costs.newentry('shoes', 60)
        self.costs.newentry('sweater', 30)
        items_bought = ['socks', 'shoes', None]
        tax = 0.09
        total = get_total(self.costs, items_bought, tax)
        self.assertEqual(total, 70.85)
