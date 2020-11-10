# Import relevant libraries and modules
from simple_calc import SimpleCalc
import unittest
import pytest

# Create a test class with parent unittest.TestCase
class TestCalc(unittest.TestCase):
    # Create an instance of the code class
    calc=SimpleCalc()

    # Define test modulus function
    def test_mod(self):
        # If the modulus of 9 and 3 is equal to 0, pass.
        self.assertEqual(self.calc.mod(9,3),0)

    def test_positive(self):
        # If the number is greater than 0, pass.
        self.assertGreater(self.calc.positive(9),0)

