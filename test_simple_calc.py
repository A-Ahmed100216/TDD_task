# Import relevant libraries and modules
from simple_calc import Checker
import unittest
import pytest

# Create a test class with parent unittest.TestCase
class TestChecker(unittest.TestCase):
    # Create an instance of the code class
    checker=Checker()

    # Define test modulus function
    def test_mod(self):
        # If the modulus of 9 and 3 is equal to 0, pass.
        self.assertEqual(self.checker.mod(9,3),0)

    def test_positive(self):
        # If the number is greater than 0, pass.
        self.assertGreater(self.checker.positive(9),0)

