"""
Sample tests for math functions to verify that
automated testing works.
"""
from django.test import SimpleTestCase

from app import maths


class MathTests(SimpleTestCase):
    """Test the Maths module."""

    def test_multiply_numbers(self):
        """Test multiplying numbers."""
        res = maths.multiply(3, 3)

        self.assertEqual(res, 9)

    def test_power_of_numbers(self):
        """Test raising number to the power of."""
        res = maths.power_of(2, 2)

        self.assertEqual(res, 4)
