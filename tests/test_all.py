import unittest

# Import test modules
from tests.test_kata1 import TestKata1
from tests.test_kata2 import TestKata2
from tests.test_kata3 import TestKata3


# Create a test suite
def suite():
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()

    # Add test cases from each test class
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestKata1))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestKata2))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestKata3))

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
