import unittest
from src.kata1 import Dictionary


# Tests for Dictionary
class TestKata1(unittest.TestCase):
    def setUp(self):
        self.d = Dictionary(20)

    def test_insertion_and_retrieval(self):
        key = 'Apple'
        obj = 'A fruit that grows on trees'
        self.d.newentry(key, obj)
        self.assertEqual(self.d.look(key), obj)

    def test_non_existant_key(self):
        key = 'Banana'
        self.assertEqual(self.d.look(key), f"Can't find entry for {key}")

    def test_update_value(self):
        key = 'Apple'
        new_value = 'new value'
        self.d.newentry(key, 'A fruit that grows on trees')
        self.d.newentry(key, new_value)
        self.assertEqual(self.d.look(key), new_value)

    def test_collision_handling(self):
        # Insert and retrieve more values than positions
        key_count = 40
        for i in range(key_count):
            key = 'key'+str(i)
            obj = 'value'+str(i)
            self.d.newentry(key, obj)
        for i in range(key_count):
            key = 'key'+str(i)
            obj = 'value'+str(i)
            self.assertEqual(self.d.look(key), obj)

    def test_removal(self):
        key = 'Apple'
        self.d.newentry(key, 'A fruit that grows on trees')
        self.d.remove(key)
        self.assertEqual(self.d.look(key), f"Can't find entry for {key}")

    def test_null(self):
        key = None
        obj = None
        self.d.newentry(key, obj)
        self.assertEqual(self.d.look(key), obj)
