from django.test import SimpleTestCase
from . import calc


class TestSample(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(10, 5)
        self.assertEqual(res, 15)

    def test_substract_numbers(self):
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)
