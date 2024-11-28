import unittest
from src.kata3 import concatenate


class TestKata3(unittest.TestCase):
    def test_description_example(self):
        words = ["yoda", "best", "has"]
        word = concatenate(words)
        self.assertEqual(word, "yes")

    def test_empty_array(self):
        words = []
        word = concatenate(words)
        self.assertEqual(word, '')
